from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email, username, first_name, last_name, password):

        if not phone_number:
            raise ValueError("Phone number is mandatory")

        if not username:
            raise ValueError("Username is mandatory")

        if not email:
            raise ValueError("Email is mandatory")

        if not first_name:
            raise ValueError("First name is mandatory")

        if not last_name:
            raise ValueError("Last name is mandatory")

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, email, first_name, last_name, password):

        user = self.create_user(
            phone_number,
            email,
            username,
            first_name,
            last_name,
            password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
