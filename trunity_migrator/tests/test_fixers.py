from unittest import TestCase

from bs4 import BeautifulSoup

from trunity_migrator.fixers import fix_img_src


class FixersTestCase(TestCase):

    def test_fix_img_src(self):
        html = '''
        <h1>Hi dude!</h1>
        <p>
            <img alt="" src="/path/to/files/image1.jpg" style="width: 318px; height: 217px;" />
        </p>
        '''

        base_url = 'http://www.trunity.net'

        expected_html = '''
        <h1>Hi dude!</h1>
        <p>
            <img alt="" src="http://www.trunity.net/path/to/files/image1.jpg" style="width: 318px; height: 217px;" />
        </p>
        '''

        result_html = fix_img_src(html, base_url)

        # we use BeautifulSoup to compare html:
        self.assertEqual(
            BeautifulSoup(result_html, "html.parser"),
            BeautifulSoup(expected_html, "html.parser"),
            'html and expected_html are not equal!'
        )