from django.contrib import admin
from django.urls import path,include
from app import views



urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login_view, name='login_view'),
   path('register/', views.register, name='register'),
   path('doctor/', views.doctor, name='doctor'),
   path('patient/', views.patient, name='patient'),



   # path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    #path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]