from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('employes', views.EmployeViewset, basename = 'employes')

urlpatterns = [
    path('students/', views.studentsViews),
    path('students/<str:pk>/', views.studentsDetail),

    # path('employes/', views.Employes.as_view()),  # Use the class-based view for employes
    # path('employes/<str:pk>/', views.EmployesDetails.as_view()),  # This can be used for detail view if needed
    
    path('', include(router.urls)),  # Include the router URLs for employes

    path('blogs/', views.BlogViewset.as_view()),
    path('comments/', views.CommentViewset.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailViewset.as_view()),
    path('comments/<int:pk>/', views.CommentDetailViewset.as_view()),
]