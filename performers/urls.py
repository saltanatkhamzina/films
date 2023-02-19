from django.urls import path
from .views import PerformersListView

urlpatterns = [
    path('', PerformersListView.as_view(), name='all')
]
