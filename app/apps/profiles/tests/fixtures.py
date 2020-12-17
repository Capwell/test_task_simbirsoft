from django.contrib.auth import get_user_model
from django.test import TestCase


class Settings(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user = get_user_model()
        cls.user_one = user.objects.create_user(email='3@py.py', password='1')
