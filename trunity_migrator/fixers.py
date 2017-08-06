from typing import List

from bs4 import BeautifulSoup

from trunity_migrator.utils.static import url_repair


__all__ = (
    'fix_img_src',
    'fix_table_width',
)


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


def fix_table_width(html: str, old_widths: List[str], new_widths=List[str]):
    if len(old_widths) != len(new_widths):
        raise ValueError(
            "old_widths and new_widths must have the same length!"
        )

    soup = BeautifulSoup(html, "html.parser")

    for old_width, new_width in zip(old_widths, new_widths):
        for table_tag in soup.find_all('table', width=old_width):
            table_tag['width'] = new_width

    return soup.decode()
