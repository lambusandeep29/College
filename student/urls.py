from django.urls import path
from student import views

urlpatterns = [

    path('registration/', views.RegistrationList.as_view()),
    path('registration/<int:pk>', views.Registrationdetail.as_view())
]