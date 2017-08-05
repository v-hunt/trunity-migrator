from bs4 import BeautifulSoup

from trunity_migrator.utils.static import url_repair


BASE_FILE_URL = 'http://www.trunity.net'


def fix_img_src(html: str, base_url: str) -> str:
    """
    Search for all <img> tags and add the scheme part for src if src is
    not the absolute url.

    :param html:
    :param base_url: http://trunity.com
    :return: html
    """
    soup = BeautifulSoup(html, "html.parser")
    
    for img in soup.findAll('img'):
        img['src'] = url_repair(img['src'], base_url)

    return soup.decode()
