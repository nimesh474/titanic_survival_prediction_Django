from django.urls import path
from titanicmodel import views

urlpatterns = [
    path('', views.survival_prediction, name='survival_prediction')
]