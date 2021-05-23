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
    path("add_item_submit", views.add_item_submit, name="add_item_submit"),
    path("add_item", views.add_item, name="add_item"),


    # TESTING ONLY
    path("test", views.test, name="test"),

]
if settings.DEBUG:
    urlpatterns += static("/media/images/", document_root=settings.MEDIA_ROOT)