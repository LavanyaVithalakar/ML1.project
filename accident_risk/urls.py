from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_accident_risk, name='predict_accident_risk'),
]
