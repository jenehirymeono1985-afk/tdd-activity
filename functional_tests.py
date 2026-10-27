from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # This runs before the test starts to open the browser
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # This runs after the test finishes to close the browser
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Outline the use case (Step 22)
        # We navigate to the homepage of our local server
        self.browser.get('http://localhost:8000')

        # Check that the title has "To-Do" instead of the Django install page (Step 23)
        self.assertIn('To-Do', self.browser.title)


if __name__ == '__main__':
    unittest.main()