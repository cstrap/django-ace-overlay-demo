from __future__ import unicode_literals

from django.db import models

class Edit(models.Model):
    text = models.TextField()
