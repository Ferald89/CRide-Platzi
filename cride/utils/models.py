"""Django models utilities """

# Django
from django.db import models


class CRideModel(models.Model):
    """Comparte Ride base Model.
    CrideModel acts as an abstract base class drom wich every
    other model in the project will inherit. This class provdes
    every tables with the following attributes
    +createdd(DateTime): Store the datetime the object was created
    +modified (DateTime): Store the last datetime the object was modified
    """

    created = models.DateTimeField(
              'created at',
              auto_now_add=True,
              help_text='DateTime on wich the object was created'
              )
    modified = models.DateTimeField(
              'modified at',
              auto_now=True,
              help_text='DateTime on wich the object was last modiefed'
              )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
