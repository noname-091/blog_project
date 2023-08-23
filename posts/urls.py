from unicodedata import name
from django.urls import path
from .views import (
    BlockListView, 
    PostDetailView,
    PostCreateView,
    PostEditView,
    PostDeleteView,
) 

urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/new/', PostCreateView.as_view(), name = 'post_new'),
    path('', BlockListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('signup/', SignUpView.as_view(), name='signup')
]
