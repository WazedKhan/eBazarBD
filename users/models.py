from turtle import update
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, password = None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users mush have an email')

        user = self.model(email = self.normalize_email(email) )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password = None):
        """
        Creates and saves a Superuser with the given email and password.
        """
        user = self.create_user(email, password = password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True

        user.save(using = self._db)
        return user



class MyUser(AbstractBaseUser):
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=13, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_sellar = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        if self.name:
            return self.name
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



