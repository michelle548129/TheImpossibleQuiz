from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import user, purchase, item
from application.forms import AddItem, UpdateItem, ChooseItem, AddUser, CreateRequest

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            LIVESERVER_PORT = 5050,
            DEBUG = True,
            TESTING = True
        )
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options = chrome_options)
        db.create_all()
        self.driver.get(f'http://localhost:{self.TEST_PORT}/admin_page')

    def tearDown(self): #run after each test
        self.driver.quit()
        db.drop_all()

    # def test_server_running(self):
    #     response = urlopen('http://localhost:5050/admin_page')
    #     self.assert200(response)
    
class TestAddItem(TestBase):
    TEST_CASES = ('Sample item 1', 56.00, 'Sample desc 1',25),('Sample item 2', 22.00, 'Sample desc 2',12)

    def submit_input(self, case):
        self.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(case[0])
        self.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(case[0])
        self.driver.find_element_by_xpath('/html/body/form/input[3]').send_keys(case[0])
        self.driver.find_element_by_xpath('/html/body/form/input[4]').send_keys(case[0])
        self.driver.find_element_by_xpath('/html/body/form/input[5]').click()

    def test_add_item(self):
        for case in self.TEST_CASES:
            self.submit_input(case)
            i = item.query.filter_by(item_name=case[0])
            self.assertNotEqual(i, None)