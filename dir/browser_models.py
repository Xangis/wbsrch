from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileDownload(models.Model):
    filename = models.CharField(max_length=80, null=False, blank=False)
    count = models.IntegerField(null=False, blank=False)
    version = models.DecimalField(decimal_places=4, max_digits=8, null=False, blank=False)
    enabled = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.filename

