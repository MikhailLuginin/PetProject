import random
import re

from faker import Faker


class Fakers:

    def __init__(self, locale="ru_RU"):
        self.fake = Faker(locale)

    def fake_name(self):
        return self.fake.name()

    def fake_email(self):
        return self.fake.email()

    def fake_password(self):
        return self.fake.password()

    @staticmethod
    def fake_phone():
        phone = random.randint(10000000, 99999999999999999999)
        return str(phone)

    def fake_company(self):
        return self.fake.company()


fakers = Fakers()
