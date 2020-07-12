from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index , name='index'),
    path('delete/<int:pk>/',views.delete_note, name= 'delete'),
    path("edit/<int:pk>/", views.edit_note, name="edit"),
    path("register/",views.user_register,name='register'),
    path("login/",views.user_login,name='login'),
    path("logout/",views.user_logout,name='logout'),
]

