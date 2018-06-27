from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Create your tests here.

"""
class TestUser(TestCase):
	@classmethod
	def setUpTestData(cls):
		# faker
		user = User.objects.create(
			username="PablitoPregunton",
			email="PablitoPregunton@gmail.com",
			password="zxcvbnm"
		)


	def setUp(self):
		pass

	def testSaveUsers(self):
		saved_users = User.objects.count()
		self.assertEqual(saved_users, 1)
"""

class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

#    def tearDown(self):
#        self.selenium.quit()
#        super(AccountTestCase, self).tearDown()

    def test_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        assert "Inicia Sesión" in selenium.title
        user = selenium.find_element_by_name('email')
        password = selenium.find_element_by_name('password')

        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        user.send_keys('m.danielabap')
        password.send_keys('123456789d')

        #submitting the form
        submit.send_keys(Keys.RETURN)

    def test_login1(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        assert "Inicia Sesión" in selenium.title
        user = selenium.find_element_by_name('email')
        password = selenium.find_element_by_name('password')

        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        user.send_keys('m.danielabap@gmail.com')
        password.send_keys('123456789d')

        #submitting the form
        submit.send_keys(Keys.RETURN)

    def test_register_init(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/register/')
        assert "Registrate" in selenium.title
        #find the form element
        #first_name = selenium.find_element_by_name('id_first_name')
        #last_name = selenium.find_element_by_name('id_last_name')
        full_name = selenium.find_element_by_name('full_name')
        ci = selenium.find_element_by_name('ci')
        sex = selenium.find_element_by_name('sex')
        bday = selenium.find_element_by_name('bday')
        city = selenium.find_element_by_name('cellphone')
        cellphone = selenium.find_element_by_name('city')
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        #first_name.send_keys('Yusuf')
        #last_name.send_keys('Unary')

        full_name.send_keys('test01')
        ci.send_keys('01')
        sex.send_keys('F')
        bday.send_keys('2000/04/05')
        city.send_keys('mérida')
        cellphone.send_keys('2345')
        email.send_keys('test01@gmail.com')
        password1.send_keys('12345678')
        password2.send_keys('12345678')

        #submitting the form
        submit.send_keys(Keys.RETURN)
"""
    def test_register_usertaken(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/register/')
        assert "Registrate" in selenium.title
        #find the form element
        #first_name = selenium.find_element_by_name('id_first_name')
        #last_name = selenium.find_element_by_name('id_last_name')
        full_name = selenium.find_element_by_name('full_name')
        ci = selenium.find_element_by_name('ci')
        sex = selenium.find_element_by_name('sex')
        bday = selenium.find_element_by_name('bday')
        city = selenium.find_element_by_name('cellphone')
        cellphone = selenium.find_element_by_name('city')
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        #first_name.send_keys('Yusuf')
        #last_name.send_keys('Unary')

        full_name.send_keys('test01')
        ci.send_keys('01')
        sex.send_keys('F')
        bday.send_keys('2000/04/05')
        city.send_keys('mérida')
        cellphone.send_keys('2345')
        email.send_keys('test01@gmail.com')
        password1.send_keys('12345678')
        password2.send_keys('12345678')

        #submitting the form
        submit.send_keys(Keys.RETURN)

    def test_register_passworderror(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/register/')
        assert "Registrate" in selenium.title
        #find the form element
        #first_name = selenium.find_element_by_name('id_first_name')
        #last_name = selenium.find_element_by_name('id_last_name')
        full_name = selenium.find_element_by_name('full_name')
        ci = selenium.find_element_by_name('ci')
        sex = selenium.find_element_by_name('sex')
        bday = selenium.find_element_by_name('bday')
        city = selenium.find_element_by_name('cellphone')
        cellphone = selenium.find_element_by_name('city')
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        #first_name.send_keys('Yusuf')
        #last_name.send_keys('Unary')

        full_name.send_keys('test01')
        ci.send_keys('01')
        sex.send_keys('F')
        bday.send_keys('2000/04/05')
        city.send_keys('mérida')
        cellphone.send_keys('2345')
        email.send_keys('test01@gmail.com')
        password1.send_keys('12345678')
        password2.send_keys('12345678')

        #submitting the form
        submit.send_keys(Keys.RETURN)
"""
