from bin.common import MyEnum


class Manager:

    class Users(MyEnum):
        put = "post_test"


class JsonNameName:

    def __init__(self):
        self.method = "GET"
        self.type

    def method(self, method):
        self.method = method
        return self

    def to_file_name(self):
        return



print(Manager.Users.post)
