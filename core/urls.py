"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('accounts/signup/', signup, name="signup"),
    path('contact/', contact_us, name="contact_us"),
    path('upload_script/', upload_script, name="upload_script"),
    path('upload_model/', set_trained_model, name="upload_model"),
    path('generate_script/<int:pk>/', generate_script, name="generate_script"),
    path('view_details_script/<int:pk>/', view_all_scripts, name="view_all_script"),
    path('who_are_you/<int:pk>/', who_are_you, name="who_are_you"),
    path('start_script/<int:pk>/<str:ch>/', start_script, name="start_script"),
    path('send_script_data/<int:pk>/<str:ch>/', send_script_data, name="send_script_data"),
    path('about_us/', about_us, name="about_us"),
    path('set_audio/<int:pk>/', set_audio, name="set_audio"),
    path('send_audio/<int:pk>/', return_audio_view, name="return_audio_view"),
]
