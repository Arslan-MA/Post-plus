"""
URL configuration for django_block project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from block_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('password-change/', PasswordChangePage.as_view(), name='edit_password'),
    path('password-reset/', PasswordChangePage.as_view(), name='reset_password'),
    path('logout/', logout_page, name='logout'),
    path('create_post/', add_post, name='create'),
    path('edit/<int:pk>/', EditPostPage.as_view(), name='edit'),
    path('delete/<int:pk>/', delete_post, name='delete')
]
