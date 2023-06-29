from . import views
from django.urls import path

urlpatterns = [
    path('', views.recipes, name='home-recipes'),
    path('delete-recipe/<id>/', views.delete_recipe, name="delete-recipe"),
    path('update-recipe/<id>/', views.update_recipe, name="update-recipe"),
    path('login/', views.login_page, name="login-page"),
    path('register/', views.register_page, name="register-page"),
]

