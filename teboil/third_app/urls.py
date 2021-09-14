from django.urls import path, include
from . import views
from . import models


urlpatterns = [
    path('', views.templates, name='templates'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('registration/', views.register, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.Search.get_context_data, name='search'),
    path('category/', views.categoryshow, name='category'),
    path('<product_id>/', views.productshow, name='product'),
]
