# Third Party
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.urls import reverse


class MyAccoutManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        first_name,
        last_name,
        birthdate,
        gender,
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
        if not gender:
            raise ValueError("User must have an gender")
        if not birthdate:
            raise ValueError("User must have an birthday")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        username,
        first_name,
        last_name,
        birthdate,
        gender,
        password,
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            gender=gender,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_member = True
        user.is_board = True
        user.is_coach = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    MALE = "M"
    FEMALE = "F"
    DIVERS = "D"
    GENDER = [(MALE, "Mann"), (FEMALE, "Frau"), (DIVERS, "Divers")]

    email = models.EmailField(
        verbose_name=" E-Mail", max_length=60, unique=True
    )
    username = models.CharField(
        verbose_name="Nutzername", max_length=30, unique=True
    )
    date_joined = models.DateTimeField(
        verbose_name="Anmeldedatum", auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name="Letzter Login", auto_now=True
    )
    is_admin = models.BooleanField(verbose_name="Admin", default=False)
    is_active = models.BooleanField(verbose_name="Aktiv", default=True)
    is_member = models.BooleanField(verbose_name="Mitglied", default=True)
    is_board = models.BooleanField(verbose_name="Vorstand", default=False)
    is_staff = models.BooleanField(default=False)
    is_coach = models.BooleanField(verbose_name="Trainer", default=False)
    is_superuser = models.BooleanField(verbose_name="SuperUser", default=False)
    first_name = models.CharField(verbose_name="Vorname", max_length=30)
    last_name = models.CharField(verbose_name="Nachname", max_length=30)
    gender = models.CharField(
        verbose_name="Geschlecht", max_length=5, choices=GENDER, default=DIVERS
    )
    birthdate = models.DateField(verbose_name="Geburstag")

    USERNAME_FIELD = "email"  # Set Login Field to E-Mail
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "birthdate",
        "gender",
    ]

    objects = MyAccoutManager()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    def has_perm(self, prem, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return True

    def get_absolute_url(self):
        return reverse("account:profil_view", kwargs={"user.id": self.pk})
