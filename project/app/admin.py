from django.contrib import admin
# from .models import Item, User
from .models import Item, User, Image

# Register your models here.
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Image)