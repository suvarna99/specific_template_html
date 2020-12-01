from django.urls import path
from app2 import views
app_name = 'app2'

urlpatterns = [
    path ('f2/',views.f2,name='f2'),
]