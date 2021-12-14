from django.urls import path
from draw import views

app_name = 'draw'
urlpatterns = [
    path('toto-lotek/', views.toto, name='toto-lotek'),
]