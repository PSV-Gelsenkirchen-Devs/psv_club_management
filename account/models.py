from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccoutManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        first_name,
        last_name,
        birthdate,
        password=None,
    ):
        if not email:
            raise ValueError("User must have an email adresse")
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have an password")
        if not first_name:
            raise ValueError("User must have an first name")
        if not last_name:
            raise ValueError("User must have an last name")
        if not birthdate:
            raise ValueError("User must have an birthday")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, first_name, last_name, birthdate, password
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    USERNAME_FIELD = "email"  # Set Login Field to E-Mail
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "birthdate"]

    objects = MyAccoutManager()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    def has_perm(self, prem, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return True
