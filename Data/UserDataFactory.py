from faker import Faker

class UserDataFactory:
    fake = Faker()

    @staticmethod
    def create_user():
        return {
            "name": UserDataFactory.fake.name(),
            "email": UserDataFactory.fake.email(),
            "phone": UserDataFactory.fake.numerify('6########')
        }