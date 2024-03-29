from django.test import TestCase
from http import HTTPStatus
from django.contrib.auth import get_user_model
from ..models import Client
from ..forms import ClientSignUpForm

class ClientSignUpFormTest(TestCase):
    def setUp(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.username = "johndoe"
        self.email = "john@exemple.com"
        self.password = "123456seven"
        
        self.form_data = {
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "username": self.username,
            "email" : self.email,
            "password1" : self.password,
            "password2" : self.password
        }
        
    def test_valid_input_form_data(self):
        form = ClientSignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid());

        
    def test_invalid_form_with_differents_password_in_input(self):
        form = ClientSignUpForm(data={
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "username": self.username,
            "email" : self.email,
            "password1" : self.password,
            "password2" : "nothong"
        })
        self.assertEqual(form.errors["password2"], ["The two password fields didn’t match."]);


class ClientSignUpViewTests(TestCase):
    def setUp(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.username = "johndoe"
        self.email = "john@exemple.com"
        self.password = "123456seven"
        
        self.form_data = {
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "username": self.username,
            "email" : self.email,
            "password1" : self.password,
            "password2" : self.password
        }
        
    def test_get(self):
        response = self.client.get("/accounts/signup/client/")
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
 
    def test_not_found_get(self):
        response = self.client.get("accounts/signup/client/")
        
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        
    def test_post_success(self):
        response = self.client.post("/accounts/signup/client/", data=self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response['Location'], "/accounts/profile/")
        
    def test_post_error(self):
        response = self.client.post("/accounts/signup/client/", data={
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "username": self.username,
            "email" : self.email,
            "password1" : self.password,
            "password2" : "nothong"
        })
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "The two password fields didn’t match.", html=True)