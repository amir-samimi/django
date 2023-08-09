from django.contrib import admin
from django.urls import path
from news.views import printhello
from register.views import regis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',printhello),
    path('register/',regis)
]
