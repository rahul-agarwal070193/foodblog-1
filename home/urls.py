from django.urls import path
from . import views
from .views import all_post, blog_detail, add_post, update_post, delete_post, LikeView, user_view, recipes_view

urlpatterns = [
    path('', views.base, name="base"),
    path('about', views.about, name="about"),
    path('error', views.error, name="error"),
    path('title', views.title, name="title"),
    path('coursel', views.coursel, name="coursel"),
    path('all_post', all_post.as_view(), name="all_post"),
    path('home', views.home, name="home"),
    path('blog/<int:pk>', blog_detail.as_view(), name="blog_detail"),
    path('add_post', add_post.as_view(), name="add_post"),
    path('blog/edit/<int:pk>', update_post.as_view(), name="update_post"),
    path('blog/delete/<int:pk>', delete_post.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('user/<str:name>/<int:id>', user_view.as_view(), name='user_profile'),
    path('recipes/<str:name>', recipes_view.as_view(), name='recipes'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
]
