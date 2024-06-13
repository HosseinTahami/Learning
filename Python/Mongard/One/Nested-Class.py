"""
    Nested Class
"""


class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        heart = self.Heart()
        print(f"Hello, my name is {self.name}!")
        heart.pump()

    class Heart:

        def pump(self):
            print(f"The heart is Pumping!")


ali = Person("Ali")
ali.introduce()

print('----------------------')

hossein_heart = Person("Hossein").Heart()
hossein_heart.pump()


"""
    Link:
        https://www.mongard.ir/one_part/163/python-nested-classes/
"""
