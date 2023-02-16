from django.urls import path
from .views import FeedBackView
from . import views


urlpatterns = [
    path('feedback/', FeedBackView.as_view(), name='feedback_view'),
    path("", views.index, name="index"),


     ]