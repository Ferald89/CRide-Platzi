"""User Models."""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utiliate
from cride.utils.models import CRideModel


class User(CRideModel,AbstractUser):
    """User mode.
    Extend from django's Abstact User,Change the username field
    to email and add some extra fields
    """
    email = models.EmailField(
         'email address',
         unique = True,
         error_messages={
            'unique' : 'A user with tha email already exise.'
         }
    )

    phone_regex = RegexValidator(
         regex = r'\+?1?\d{9,15}$',
         message = "Phone number must be entered in the format: +9999999. up to 15 digits allowed."
    )

    phone_number = models.CharField(validators=[phone_regex],max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    is_client = models.BooleanField(
         'client status',
         default = True,
         help_text = (
             'Help easily distinguish users and perfom queries. '
             'Clients are the main type of user.'
         )
    )
    is_vefied = models.BooleanField(
         'verified',
         default=True,
         help_text = 'Set to true when the user have verified its email adress'
    )

    def ___str__(self):
        return self.username

    def get_short_name(self):
        return self.username
