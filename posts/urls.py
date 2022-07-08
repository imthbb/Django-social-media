from django.urls import path
from . import views
from .views import ListPost, DetailPost, CreatePost, UpdatePost, DeletePost

urlpatterns = [
	path('', ListPost.as_view(), name='home_page'),
    path('post/<int:pk>/', DetailPost.as_view(), name='post_page'),
    path('post/new/', CreatePost.as_view(), name='create_post_page'),
	path('post/<int:pk>/update/', UpdatePost.as_view(), name='update_post_page'),
	path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete_post_page'),
]
