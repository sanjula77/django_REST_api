from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.studentsViews),
    path('students/<str:pk>/', views.studentsDetail),
    path('employes/', views.Employes.as_view()),  # Use the class-based view for employes
    path('employes/<str:pk>/', views.EmployesDetails.as_view()),  # This can be used for detail view if needed
]