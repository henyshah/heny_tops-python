"""
URL configuration for DigitalSociety project.

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
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('change-password',views.change_password,name="change-password"),
    path('update-chairman-profile',views.update_chairman_profile,name="update-chairman-profile"),
    path('add-media',views.add_media,name="add-media"),
    path('view-image-gallery',views.view_image_gallery,name="view-image-gallery"),
    path('view-video-gallery',views.view_video_gallery,name="view-video-gallery"),
    path('delete-video/<int:pk>',views.delete_video,name="delete-video"),
    path('add-member',views.add_member,name="add-member"),
    path('all-member',views.all_member,name="all-member"),
    path('sall-member',views.sall_member,name="sall-member"),
    path('add-notice',views.add_notice,name="add-notice"),
    path('all-notice',views.all_notice,name="all-notice"),
    path('Society-Member-profile/',views.Society_Member_profile,name="Society-Member-profile"),
    path('Society-Member-change-password/',views.Society_Member_change_password,name="Society-Member-change-password"),
    path('Society-Member-update-chairman-profile/',views.Society_Member_update_chairman_profile,name="Society-Member-update-chairman-profile"),
    path('Society-Member-view-image-gallery/',views.Society_Member_view_image_gallery,name="Society-Member-view-image-gallery"),
    path('Society-Member-view-video-gallery/',views.Society_Member_view_video_gallery,name="Society-Member-view-video-gallery"),
    path('sall-notice/',views.sall_notice,name="sall-notice"),
]
