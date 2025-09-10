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


fakers = Fakers()
