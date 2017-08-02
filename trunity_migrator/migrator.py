from trunity_migrator import settings
from trunity_2_client import Client as Trunity2Client

from trunity_3_client import (
    initialize_session_from_creds,
    TopicsClient,
    ContentsClient,
    ContentType,
)


class RootTopicIdError(IOError):
    """
    Raise when can't find root topic in Trunity 2
    """
    pass


class Migrator(object):

    def __init__(self, trunity_2_login, trunity_2_password,
                 trunity_3_login, trunity_3_password):

        self._trunity_2_client = Trunity2Client(
            trunity_2_login, trunity_2_password
        )

        trunity_3_session = initialize_session_from_creds(
            trunity_3_login, trunity_3_password
        )
        self._topics_client = TopicsClient(trunity_3_session)
        self._contents_client = ContentsClient(trunity_3_session)

        self._trunity_3_side_id = settings.TRUNITY_3_SITE_ID

        self._trunity_2_root_topic_id, self._trunity_2_site_id = None, None
        self._cur_topic_id = None

    def _get_trunity_2_site_info(self, site_name):
        """
        Returns root_topic_id and site_id.
        :param site_name:
        :return:
        """
        sites = self._trunity_2_client.get_user_sites('All')
        for site in sites:
            if site['name'] == site_name:
                return site['rootTopic'], site['siteId']

        raise RootTopicIdError(
            "Can't retrieve Trunity 2 book info by book name!"
        )

    def upload_content(self, title, body, topic_id=None):
        print("Uploading content: {}".format(title), end='')

        self._contents_client.list.post(
            site_id=settings.TRUNITY_3_SITE_ID,
            content_title=title,
            content_type=ContentType.ARTICLE,
            text=body,
            topic_id=topic_id,
        )

        print('\t\t[SUCCESS!]')

    def _create_chapter(self, title, topic_id=None, short_name=None):
        print('Creating new chapter: {}'.format(title), end='')

        new_chapter_id = self._topics_client.list.post(
            site_id=self._trunity_3_side_id,
            name=title,
            topic_id=topic_id,
            short_name=short_name,
        )

        print('\t\t[SUCCESS!]')

        return new_chapter_id

    def _get_topic_joins(self, topic_id):
        return self._trunity_2_client.get_topic_joins(
            self._trunity_2_site_id, topic_id
        )

    @staticmethod
    def _get_type_of_join(join):
        return join.get('type', None)

    def _is_join_is_content(self, join):

        content_type = self._get_type_of_join(join)

        if content_type in settings.CONTENT_TYPES:
            return True
        else:
            return False

    def _is_join_is_chapter(self, join):

        content_type = self._get_type_of_join(join)

        if content_type == 'topics':
            return True
        else:
            return False

    def _get_upper_topic_id(self, topic_id):
        pass

    def _upload_topic_joins(self, topic_joins):

        for join in topic_joins:
            if self._is_join_is_content(join):

                self.upload_content(
                    title=join['title'],
                    body=join['body'],
                    topic_id=self._cur_topic_id
                )

            elif self._is_join_is_chapter(join):

                self._cur_topic_id = self._create_chapter(
                    title=join['title'],
                    topic_id=self._cur_topic_id,
                    short_name=None,  # TODO: add short_name
                )

                topic_joins = self._get_topic_joins(join['_id'])
                # recursion call:
                self._upload_topic_joins(topic_joins)

        # self._cur_topic_id = self._upper_dir(self._cur_topic_id)

    def migrate_book(self, book_title, new_book_title):
        self._trunity_2_root_topic_id, self._trunity_2_site_id = \
            self._get_trunity_2_site_info(book_title)

        root_topic_joins = self._get_topic_joins(self._trunity_2_root_topic_id)

        self._upload_topic_joins(root_topic_joins)


if __name__ == '__main__':

    migrator = Migrator(
        trunity_2_login=settings.TRUNITY_2_LOGIN,
        trunity_2_password=settings.TRUNITY_2_PASSWORD,
        trunity_3_login=settings.TRUNITY_3_LOGIN,
        trunity_3_password=settings.TRUNITY_3_PASSWORD,
    )

    # print(migrator._trunity_2_root_topic_id)

    migrator.migrate_book(
        settings.TRUNITY_2_BOOK_NAME,
        settings.TRUNITY_3_BOOK_NAME
    )

