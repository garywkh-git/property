from django.urls import path
from . import views

app_name = 'careers'

urlpatterns = [
    path('', views.career_list, name='list'),
    path('<int:job_id>/', views.career_detail, name='detail'),
]