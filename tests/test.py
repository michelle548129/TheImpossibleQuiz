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
            SQLALCHAMEY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "this is my secret key",
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
        self.driver.get(f'http://localhost:5050/user_page')
        db.create_all()
        test_item = ('Snickers', 56.00, 'Nutty caramel', 25)('Kitkat', 30.00, 'Wafer chocolate', 45)
        test_user = ('Michelle', 'michelle548129@icloud.com', '12 The Alders, Hounslow, Hounslow'), ('bob', 'bob3445@yahoo.co.uk', '15 Willow Lane, London, LE3 5TY')


    def tearDown(self):
        self.driver.quit()
        db.drop_all()
    
      def test_server_running(self):
        response = urlopen('http://localhost:5050/user_page')
        self.assertEqual(response.code, 200)

   
 def test_add_user(self):
        for i in self.TEST_CASES:
            self.submit_input(i)
            users = user.query.filter_by(user_name=case[0]).all()
            self.assertNotEqual(users, None)

def test_add_item(self):
        for i in self.TEST_CASES:
            self.submit_input(i)
            items = user.query.filter_by(item_name=case[0]).all()
            self.assertNotEqual(users, None)
    
def submit_input(self, case):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/select[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/select[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[2])
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[3])
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[4]').send_keys(case[4])
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

class TestUpdateQuantity(TestBase):
    def test_updatequantity_get(self):
        response = self.client.get(url_for('update_quantity', pk = 1))
        self.assert200(response)
        self.assertIn(b'Quantity', response.data)

    def test_updatequantity_post(self):
        response = self.client.post(
        url_for('update_quantity', pk = 1),
        data = dict(quantity = "Updated quantity", quantity_desc = "updated quantity for testing"))
        self.assert200(response)
        self.assertIn(b'quantity has been updated successfully!', response.data)
        self.assertNotEqual(quantity.query.filter_by(quantity = "Updated quantity").first(), None)


class TestDeleteItem(TestBase):
    def test_deleteitem_get(self):
        response = self.client.get(url_for('delete_item', pk = 2))
        self.assert200(response)
        self.assertIn(b'Item has been deleted successfully!', response.data)
        self.assertEqual(item.query.filter_by(item_name = 'Test item').first(),None)