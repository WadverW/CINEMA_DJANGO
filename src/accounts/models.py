# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.core.validators import RegexValidator

# phone_number_validator = RegexValidator(
#     regex=r"^\+?[1-9]\d{9,14}$",
#     message="Phone number must be in a correct format -> +380123456789",
# )


# class User(AbstractUser):
#     ...

#     def __str__(self):
#         return self.username


# class ClientProfile(models.Model):
#     GENDER_CHOICES = [
#         ("male", "Мужской"),
#         ("female", "Женский"),
#     ]
#     LANGUAGE_CHOICES = [
#         ("ru", "Русский"),
#         ("uk", "Украинский"),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
#     phone_number = models.CharField(
#         max_length=20, blank=True, validators=[phone_number_validator]
#     )
#     birth = models.DateField(null=True, blank=True)
#     address = models.TextField(blank=True)
#     city = models.CharField(max_length=100, blank=True)
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
#     language = models.CharField(
#         max_length=2, choices=LANGUAGE_CHOICES, default="ru", blank=True
#     )
#     card_number = models.CharField(max_length=20, blank=True)
#     nickname = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return f"Profile of {self.user.username}"


# class Subscription(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="subscriptions"
#     )
#     is_subscribed = models.BooleanField(default=True)
#     subscription_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {'Subscribed' if self.is_subscribed else 'Unsubscribed'}"
