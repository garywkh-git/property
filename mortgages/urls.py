from django.urls import path
from . import views
from .views import mortgage_calculator

app_name='mortgages'
urlpatterns = [
    path('', mortgage_calculator, name='calculator'),
]


