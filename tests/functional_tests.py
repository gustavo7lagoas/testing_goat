from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Gustavo has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        self.fail('Finish the test!')

    # He is inveted to enter a to-do item straight away

    # He types "Buy food" into a text box

    # When he hits enter, the page updates, and now the pages lists
    # "1: Buy food" as an item in a to-do lists

    # There is still a text box inviting him to add another item. He
    # enters "Use mushrooms to a strogonoff"

    # The page updates again, and now shows both items on his lists

    # Gustavo wonders wheter the site will remember his list. Then he sees
    # that the site has generated a unique URL for him -- there is some
    # explanatory text to that effect

    # He visits that URL - his to-do list is still there

    # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
