from django.urls import path
from .views import AdsListView
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', AdsListView.as_view(), name='all'),
]
