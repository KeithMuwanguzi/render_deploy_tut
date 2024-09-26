from django.urls import path
from . import views

urlpatterns = [
    path('',views.testEnd, name='test'),
    path('students/', views.get_students, name='get_students'),       
    path('students/<int:student_id>/', views.get_student, name='get_student'), 
    path('students/add/', views.add_student, name='add_student'), 
    path('students/update/<int:student_id>/', views.update_student, name='update_student'),
]