"""Celery task."""

# Django
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives

# Models
from cride.users.models import User
from cride.rides.models import Ride

# Celery
from celery.decorators import task, periodic_task

# Utilities
from datetime import timedelta
import jwt
import time


def gen_verification_token(user):
    """Create JWT token tha the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
          'user': user.username,
          'exp': int(exp_date.timestamp()),
          'type': 'email_confirmation'
          }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    for i in range(30):
        time.sleep(1)
        print('sleeping', str(i+1))
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Welcome @{}! verify you account to start using Comparte Ride'.format(user.username)
    from_email = 'Comparte Ride <noreply@comparteride.com>'
    content = render_to_string(
              'emails/users/account_verification.html',
              {
                'token': verification_token,
                'user': user
              }
              )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


@periodic_task(name='disable_finished_rides', run_every=timedelta(seconds=5))
def disable_finished_rides():
    """Disable finished rides. """
    now = timezone.now()
    offset = now + timedelta(seconds=5)

    # Update rides that have already finished
    rides = Ride.objects.filter(
            arrival_date__gtte=now,
            arrival_date__lte=offset,
            is_active=True
            )
    rides.update(is_active=False)
