


from django.db import models



class TimeStampModelMixin(models.Model):
    """
    timestamp (created, updated) fields mixin
    """

    created = models.DateTimeField(auto_now_add=True, verbose_name="created datetime")
    modified = models.DateTimeField(auto_now=True, verbose_name="last modified datetime")

    class Meta:  # pylint: disable=C0115, R0903
        abstract = True
