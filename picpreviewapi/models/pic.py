"""
    Pic Model Module
"""
from django.db import models


class Pic(models.Model):
    """Pic Model"""
    image_url = models.ImageField(upload_to="pics",
                                  height_field=None,
                                  width_field=None,
                                  max_length=None,
                                  null=True)
