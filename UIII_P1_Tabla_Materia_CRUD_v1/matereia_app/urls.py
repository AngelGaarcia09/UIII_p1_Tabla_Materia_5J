from django.urls import path
from matereia_app import views

urlpatterns = [
    path("",views.inicio_vista, name="Incio_vista")
]