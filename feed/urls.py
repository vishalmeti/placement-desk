from django.urls import path

from . import views

app_name = "feed"

urlpatterns = [


    path("", views.HomePage.as_view(), name="index"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("myall/", views.AllMyPost.as_view(), name="myall"),
    path("edit/<int:pk>/", views.EditPost.as_view(), name="edit"),
    path("new/", views.CreateNewPost.as_view(),name="new_post"),



]
