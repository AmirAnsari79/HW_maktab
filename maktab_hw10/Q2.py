import json
class User(json.JSONEncoder):
    def __init__(self, name, age, pas, phone, email=None):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception
        self.pas = pas
        if phone.startswith('09') and len(phone) == 11:
            self.phone = phone
        else:
            raise Exception
        self.email = email

    def default(self, obj):
        if isinstance(obj, User):
            return {
                'name': self.name, 'age': self.age, 'password': self.pas, 'phone': self.phone, 'email': self.email}

        else:
            return super().default(obj)

    def register(self, ):
        # read and append
        with open() as f:
            pass
        with open('Q2.json', 'w')as f:
            json.dump(self.default(self), f, indent=4, separators=(",", ":"))
            f.write(',')


us = User('amir', 12, 'amir67', '09011111111')
us1 = User('ali', 19, 'ali98', '09011111122')
us.register()
us1.register()
