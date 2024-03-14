from django.urls import path
from .views import ExerciseListCreateView, ExerciseRetrieveUpdateDestroyView

urlpatterns = [
    path('', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('<int:pk>/', ExerciseRetrieveUpdateDestroyView.as_view(), name='exercise-detail'),
]
