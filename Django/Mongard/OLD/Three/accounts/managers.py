from django.contrib.auth.models import BaseUserManager, UserManager


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email, first_name, last_name, password):
        if not phone_number:
            raise ValueError("User must have Phone Number")

        if not phone_number:
            raise ValueError("User must have Phone Number")

        if not phone_number:
            raise ValueError("User must have Phone Number")

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, first_name, last_name, password):

        user = self.create_user(
            phone_number=phone_number,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user