from django.urls import path
from .views import DadosListView

urlpatterns = [
    path('dados/', DadosListView.as_view(), name='dados-list'),
]
