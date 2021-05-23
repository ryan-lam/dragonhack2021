from django.db import models


# Item listing database
class Item(models.Model):
    condition_choices = [
        ("Brand New", "Brand New"),
        ("Open Box", "Open Box"),
        ("Used", "Used"),
        ("Not Working", "Not Working"),
        ]

    poster = models.CharField(max_length=265, null=False, blank=False)
    code = models.CharField(max_length=12, null=False, blank=False)
    # status: true means available, false means not available
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=265, null=False, blank=False)
    condition = models.CharField(max_length=128, choices=condition_choices)
    location = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=2048, null=False, blank=False)

    def __str__(self):
        return f"{self.poster} : {self.status} : {self.title}"


# User profiles
class User(models.Model):
    username = CharField(max_length=32, null=False, blank=False)
    password = CharField(max_length=32, null=False, blank=False)
    name = CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f"{self.name} : {self.username}"


class Image(models.Model):
    code = models.CharField(max_length=12, null=False, blank=False)
    image = models.FileField(upload_to="images/")
    # <input type="file" name="images" multiple>

    def __str__(self):
        return f"{self.code}"

