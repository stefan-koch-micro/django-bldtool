from django.urls import path
from . import views

urlpatterns = [
    path('api/demo/', views.DataListCreate.as_view() ),
]
