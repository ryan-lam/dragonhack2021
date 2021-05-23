from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("marketplace", views.marketplace, name="marketplace"),
    path("add_item", views.add_item, name="add_item"),
    path("add_item_submit", views.add_item_submit, name="add_item_submit"),
    path("logout", views.logout, name="logout"),

    # TESTING ONLY
    path("test", views.test, name="test"),
    path("add_image", views.add_image, name="add_image"),
]
