from django.db import models

# Create your models here.

class Item(models.Model):
    condition_choices = [
        ("Brand New", "Brand New"),
        ("Open Box", "Open Box"),
        ("Used", "Used"),
        ("Not Working", "Not Working"),
        ]

    poster = models.CharField(max_length=265, null=False, blank=False)
    # status: true means available, false means not available
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=265, null=False, blank=False)
    condition = models.CharField(max_length=128, choices=condition_choices)
    location = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=2048, null=False, blank=False)

