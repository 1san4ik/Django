from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.templates, name='templates'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('registration/', views.register, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
