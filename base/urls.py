from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('register/', views.registerPage, name="register"),
    path('update_user', views.update_user, name='update_user'),
    path('group_user/', views.creatgroup, name='group_user'),
    path('update_user_status/', views.updateUserStatus, name='update_user_status'),


    path('profile/<str:pk>/', views.userProfile, name='user-profile'),


    path('topics',views.topicspage, name='topics'),
    path('create-topic',views.createTopic, name='create-topics'),
    path('activity',views.activitypage, name='activities'),
    

    path('report/<str:pk>/',views.report, name='report'),
    path('create-report/', views.createReport, name = "create-report"),
    path('delete-report/<str:pk>/', views.deleteReport, name='delete-report'),
    path('update_report/', views.update_report_status, name='update_report'),


] 
