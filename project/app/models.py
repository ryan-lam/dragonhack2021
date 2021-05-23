from django.db import models


# Item listing database
class Item(models.Model):
    condition_choices = [
        ("Brand New", "Brand New"),
        ("Open Box", "Open Box"),
        ("Used", "Used"),
        ("Not Working", "Not Working"),
        ]

    poster = models.CharField(max_length=265,)
    code = models.CharField(max_length=12)
    # status: true means available, false means not available
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=265)
    condition = models.CharField(max_length=128, choices=condition_choices)
    location = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.poster} : {self.status} : {self.title}"


# User profile database
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f"{self.name} : {self.username}"


# Image database
class Image(models.Model):
    code = models.CharField(max_length=12)
    image = models.FileField(upload_to="images/")
    # <input type="file" name="images" multiple>

    def __str__(self):
        return f"{self.code}"

