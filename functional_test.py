# this test is based on the book "Test Driven Development with Python by Percival. This is for self learning purposes
# only - any reference to the code is purely incidental and should be treated as such. Not to be used
# without original author's permission"
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

# Edith heard about a new to-do list app called the goat and goes to check it's home page out
        self.browser.get('http://localhost:8000')


# She noticies the page title and header mentioned to-dolists
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!!')

# She is invited to enter a to-do item

# She types "Purchase new bike tyres" and hits enter

# the web page now displays "1: Purchase bike tyres" and offers another opportuinity to add an item

# She types "Install new bike tyres" and hits enter

# The web page now displays both items 1 and 2

# The site provides a unique URL her on the page and explains how she can return to it

# She closes her browser, launches the webpage with unique URL again and she is brought back to her list intact

#satisfied, she closes the browser finally

if __name__ == '__main__':
    unittest.main()


