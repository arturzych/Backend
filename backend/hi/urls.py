from django.urls import path
from hi import views
# form <nazwa_aplikacji>


urlpatterns = [
    path('', views.backend),

]