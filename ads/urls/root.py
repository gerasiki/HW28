from django.urls import path

from ads.views import ads

urlpatterns = [path('', ads.index)]
