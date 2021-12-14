from django.urls import path
from monday import views


app_name = 'monday'
urlpatterns = [
    path('isitmonday/', views.isitmonday, name='isitmonday')
]
