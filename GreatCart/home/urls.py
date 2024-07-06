from django.urls import path
from home.views import homes
urlpatterns = [
    path('', homes, name='home'),
]