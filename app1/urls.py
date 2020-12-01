from django.urls import path
from app1 import views
app_name = 'app1'

urlpatterns = [
    path ('f1/',views.f1,name='f1'),
]