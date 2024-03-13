# workouts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutPlanViewSet

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'workout-plans', WorkoutPlanViewSet)

# The router automatically generates URL patterns for CRUD operations
urlpatterns = [
    path('', include(router.urls)),
]
