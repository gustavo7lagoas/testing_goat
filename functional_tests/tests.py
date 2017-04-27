from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = self.browser.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WedriverException) as e:
                if time.time() - stat_time > MAX_WAIT:
                    raise #!/usr/bin/env python
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Gustavo has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy food" into a text box
        inputbox.send_keys('Buy food')

        # When he hits enter, the page updates, and now the pages lists
        # "1: Buy food" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy food')
        # There is still a text box inviting him to add another item. He
        # enters "User mushrooms to do a strogonoff"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('User mushrooms to do a strogonoff')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his lists
        self.wait_for_row_in_list_table('1: Buy food')
        self.wait_for_row_in_list_table('2: User mushrooms to do a strogonoff')

        # Gustavo wonders wheter the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect
        self.fail('Finish the test!')

    # He visits that URL - his to-do list is still there

    # Satisfied, he goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Gustavo start anew todo list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # He notices that his list has a unique URL
        gustavo_list_url = self.browser.current_url
        self.assertRegex(gustavo_list_url, '/lists/.+')

        # Now a new user Fran, comes along to the site

        ## New browser to new cookie META-COMMENT
        self.browser.quit()
        self.browser = webdriver.Chrome

        # Fran visits the home page. There is no sign of Gustavo's
        # list
        self.browser.get(live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacoce feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Fran starts a new list by entering a new item. She
        # is less interesting than Gustavo's
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Fran gets his own unique URL
        fran_list_url = self.browser.current_url
        self.assertRegex(fran_list_url, '/lists/.+')
        self.assertNotEqual(gustavo_list_url, fran_list_url)

        # Again there is no trace of Gustavo's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied she goes back to sleep
