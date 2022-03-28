# from flask_testing import TestCase
# from selenium import webdriver
# from urllib.request import urlopen
# from flask import url_for

# from application import app, db
# from application.models import user, purchase, item
# from application.forms import AddItem, UpdateItem, ChooseItem, AddUser, CreateRequest

# class TestBase(TestCase):
#     def create_app(self): #sets test configurguration
#         app.config.update(
#             SQLALCHAMEY_DATABASE_URI = 'sqlite:///test.db',
#             SECRET_KEY = "this is my secret key",
#             LIVESERVER_PORT = 5000,
#             DEBUG = True,
#             TESTING = True,
#             WTF_CSRF_ENABLED = False
#         )
#         return app

#     def setUp(self): #run before each test
#         chrome_options = webdriver.chrome.options.Options()
#         chrome_options.add_argument('--headless')
#         self.driver = webdriver.Chrome(options = chrome_options)
#         db.create_all()
#         self.driver.get(f'http://localhost:5000/user_page')
#         db.create_all()
#         test_item = ('Snickers', 56.00, 'Nutty caramel', 25),('Kitkat', 30.00, 'Wafer chocolate', 45)
#         test_user = ('Michelle', 'michelle548129@icloud.com', '12 The Alders, Hounslow, Hounslow'), ('bob', 'bob3445@yahoo.co.uk', '15 Willow Lane, London, LE3 5TY')

#         db.session.add(test_item)
#         db.session.add(test_user)
#         db.session.commit()


#     def tearDown(self): #run after each test
#         self.driver.quit()
#         db.drop_all()
    
#     def test_server_running(self):
#         response = urlopen('http://localhost:5000/user_page')
#         self.assertEqual(response.code, 200)

   
#     def test_add_user(self):
#         for i in self.TEST_CASES:
#             self.submit_input(i)
#             users = user.query.filter_by(user_name=case[0]).all()
#             self.assertNotEqual(users, None)

# def test_add_item(self):
#         for i in self.TEST_CASES:
#             self.submit_input(i)
#             items = user.query.filter_by(item_name=case[0]).all()
#             self.assertNotEqual(users, None)
    
# def submit_input(self, case):
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/select[1]').click()
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/select[2]').click()
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[2])
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[3])
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[4]').send_keys(case[4])
#         self.driver.find_element_by_xpath('//*[@id="submit"]').click()

# class TestUpdateQuantity(TestBase):
#     def test_updatequantity_get(self):
#         response = self.client.get(url_for('update_quantity', pk = 1))
#         self.assert200(response)
#         self.assertIn(b'Quantity', response.data)

#     def test_updatequantity_post(self):
#         response = self.client.post(
#         url_for('update_quantity', pk = 1),
#         data = dict(quantity = "Updated quantity", quantity_desc = "updated quantity for testing"))
#         self.assert200(response)
#         self.assertIn(b'quantity has been updated successfully!', response.data)
#         self.assertNotEqual(quantity.query.filter_by(quantity = "Updated quantity").first(), None)


# class TestDeleteItem(TestBase):
#     def test_deleteitem_get(self):
#         response = self.client.get(url_for('delete_item', pk = 2))
#         self.assert200(response)
#         self.assertIn(b'Item has been deleted successfully!', response.data)
#         self.assertEqual(item.query.filter_by(item_name = 'Test item').first(),None)


from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import user, purchase, item
from application.forms import AddItem, UpdateItem, ChooseItem, AddUser, CreateRequest


class TestBase(TestCase):
    def create_app(self): #sets test configuration
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "this is my secret key",
            LIVESERVER_PORT = 5000,
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self): #run before each test
        db.create_all()
        test_item = item(item_name='Sample item', price=56.00,description= 'Sample desc', quantity=25)
        test_item_two = item(item_name='Sample item two', price=56.00,description= 'Sample desc', quantity=25)
        test_user = user(user_name='Sample name', email='Sample email', address='Sample address')

        db.session.add(test_item)
        db.session.add(test_user)
        db.session.commit()


    def tearDown(self): #run after each test
        db.session.remove()
        db.drop_all()
        db.create_all()

class TestHome(TestBase): #testing all the links are there on hompage
    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Home page', response.data)

    def test_home_basket(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Basket', response.data)

    def test_home_admin(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Admin', response.data)

    def test_home_user(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'User', response.data) 



class TestAddItem(TestBase): #testing for adding new item
    def test_item_get(self):
        response = self.client.get(url_for('admin_page'))
        self.assert200(response)
        self.assertIn(b'item_name', response.data)

    def test_item_post(self):
        response = self.client.post(
            url_for('admin_page'),
            data = dict(item_name='Sample item', price=56.00,description= 'Sample desc', quantity=25),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'item_name', response.data)


class TestAddUser(TestBase): #testing for adding new user
    def test_user_get(self):
        response = self.client.get(url_for('user_page'))
        self.assert200(response)
        self.assertIn(b'user_name', response.data)

    def test_create_user(self):
        response = self.client.post(
            url_for('user_page'),
            data = dict(user_name='user_name', email='Sample email', address='Sample address'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'user_name', response.data)


class TestViewAllItems(TestBase): # test for viewing all items
    def test_view_items_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample item', response.data)

class TestUpdateQuantity(TestBase): # test for updating quantity of items
    def test_update_quantity_get(self):
        response = self.client.get(url_for('admin_page'))
        self.assert200(response)
        self.assertIn(b'quantity', response.data)

    def test_update_quantity_post(self):
        response = self.client.post(
        url_for('admin_page'),
        data = dict(item_name='Sample item', price=56.00,description= 'Sample desc', quantity=20))
        self.assert200(response)
        self.assertNotEqual(item.query.filter_by(quantity = 20).first(), None)


class TestDeleteItem(TestBase): # testing for deleting an item
    def test_delete_item_get(self):
        response = self.client.get(url_for('admin_page'))
        self.assert200(response)
        self.assertEqual(item.query.filter_by(item_name = 'Sample item two').first(),None)