from django.urls import path
from .views import WorkoutPlanListCreateView, WorkoutPlanRetrieveUpdateDestroyView, \
    WorkoutSessionListCreateView, WorkoutSessionRetrieveUpdateDestroyView

urlpatterns = [
    path('plans/', WorkoutPlanListCreateView.as_view(), name='workout-plan-list-create'),
    path('plans/<int:pk>/', WorkoutPlanRetrieveUpdateDestroyView.as_view(), name='workout-plan-detail'),
    path('sessions/', WorkoutSessionListCreateView.as_view(), name='workout-session-list-create'),
    path('sessions/<int:pk>/', WorkoutSessionRetrieveUpdateDestroyView.as_view(), name='workout-session-detail'),
]
