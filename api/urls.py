from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.studentsViews),
    path('students/<str:pk>/', views.studentsDetail),
]