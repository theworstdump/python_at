import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
    # def test_homepage(self):
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(10)
    #     element1 = driver.find_element(By.CSS_SELECTOR, '#id_123')
    #
    #     wait = WebDriverWait(driver, 15)
    #     element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_123')))
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        # homepage_nav.driver.delete_cookie('ak_bmsc')
        # actual_links = homepage_nav.get_nav_links_text()
        # expected_links = homepage_nav.NAV_LINKS_TEXT
        # assert expected_links == actual_links, 'Validating Nav Links Text'
        cookies = homepage_nav.driver.get_cookies()
        # print(cookies)
        cookies_names = [cookie['name'] for cookie in cookies]
        #print('-------------')
        #print(cookies_names)
        for indx in range(12):
            # homepage_nav.driver.delete_all_cookies()
            homepage_nav.get_nav_links()[indx].click()
            # homepage_nav.driver.delete_cookie('ak_bmsc')
            # for cookie_name in cookies_names:
            #     homepage_nav.driver.delete_cookie(cookie_name)
            #     homepage_nav.driver.refresh()
            #     homepage_nav.is_visible('tag_name', 'h1', cookie_name)
            # time.sleep(1.5)
        #homepage_nav.get_nav_link_by_name('Women').click()



