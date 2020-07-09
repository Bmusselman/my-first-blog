from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='postlist'),

    # post/ = means url should begin with post followed by /
    # <int:pk> an int value and transfers it to view variable called pk
    # / = finishes url
    # so /post/num is translated to post number
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # url for postform
    path('post/new/', views.post_new, name='post_new'),

    # url for edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]