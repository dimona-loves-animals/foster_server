from django.urls import path

from . import views

urlpatterns = [
    path('angels/', views.angels_add),
]