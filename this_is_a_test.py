import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
@pytest.mark.nondestructive
def test_first_test(selenium,base_url):
    #input[name='username']
    #input[name='password']
    #button[type='submit']
    # chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('window-size=1920x1080')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # edge_options= Options()
    # edge_options.add_argument("--disable-extensions")
    # #edge_options.add_argument("--headless")
    # edge_options.add_argument('window-size=1920x1080')
    # driver = webdriver.Edge(options=edge_options)
    time.sleep(5)
    print((selenium.current_url))
    # selenium.get(base_url)
    # WebDriverWait(selenium,10).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//button[@class='vjs-big-play-button']"))).click()
    # WebDriverWait(selenium, 10).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//button[@class='vjs-play-control']"))).click()
    # followers= WebDriverWait(selenium, 10).until(EC.visibility_of_element_located(('xpath',"//a[contains(@href,'followers')]")),message="not found")
    # followers.click()
    #
    # time.sleep(3)
    # WebDriverWait(selenium, 20).until(EC.visibility_of_element_located(('xpath', "//input[name='username']")),
    #                                   message="not found").send_keys('rohitanand1614')
    # # selenium.find_element_by_xpath().send_keys('rohitanand1614')
    # selenium.find_element_by_css_selector("input[name='password']").send_keys('ilvtobemyslf')
    # selenium.find_element_by_css_selector("button[type='submit']").click()
    # time.sleep(3)
    # selenium.get(base_url)
    # followers = WebDriverWait(selenium, 10).until(
    #     EC.visibility_of_element_located(('xpath', "//a[contains(@href,'followers')]")), message="not found")
    # followers.click()
    # #aria-label='Followers'
    # followers_window = WebDriverWait(selenium, 10).until(
    #     EC.visibility_of_element_located(('xpath', "//div[@aria-label='Followers']")), message="not found")
    # selenium.find_element_by_xpath("(//h1[text()='Followers']/following::li)[1]").click()
    # followers_list = selenium.find_elements_by_xpath("//h1[text()='Followers']/following::li")
    # while(True):
    #     actions = ActionChains(selenium)
    #     actions.key_down(keys.Keys.PAGE_DOWN)
    #     time.sleep(2)
    #     updated_followers_list=selenium.find_elements_by_xpath("//h1[text()='Followers']/following::li")
    #     if(len(updated_followers_list)==len(followers_list)):
    #         for account in updated_followers_list:
    #             profile_links=updated_followers_list.find_elements_by_tag_name('a')
    #             print(profile_links[2].text)
    #
    #
