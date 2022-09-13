from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils

class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINKS_TEXT = 'Women, Men, Kids, Home, Beauty, Shoes, Handbags, Jewelry, Furniture, Toys, Gifts, Trending, Sale'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        #nav_links_text = [link.text for link in nav_links] # about list comprehension https://webdevblog.ru/kogda-ispolzovat-list-comprehension-v-python/
        nav_links_text = self.get_text_from_webelements(nav_links)
        #return ", ".join(nav_links_text)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)