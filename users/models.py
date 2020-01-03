from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "그외"),
    )
    gender = models.CharField(
        default=GENDER_MALE, choices=GENDER_CHOICES, max_length=10, blank=True
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGGE_CHOICES = ((LANGUAGE_ENGLISH, "en"), (LANGUAGE_KOREAN, "kor"))
    langauge = models.CharField(max_length=10, choices=LANGUAGGE_CHOICES, blank=True)

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(blank=True)
    bio = models.TextField(default="", blank=True)
    superhost = models.BooleanField(default=False)
