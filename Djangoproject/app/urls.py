
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('logout/', logout),
    path('verification/', signup),
    path('otpsend/<str:email>/', otpsend),
    path('user/', userpage),
    path('profile/', userprofile),
    path('addpost/', addPost),
    path('deletepost/<int:id>/', deletePost),
    path('updatepost/<int:id>/', updatePost),
    path('updateprofile/<int:id>/', updateProfile),
    path('otpverify/<str:otp>/', otpvalidation)

]
