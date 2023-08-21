class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

        def fullname(self):
            return " {} {}".format(self.first, self.last)

        @property
        def email(self):
            return "{}.{}@email.com".format(self.first, self.last)
