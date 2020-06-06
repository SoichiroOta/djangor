from django.urls import path

from djangor.entries import views

app_name = "entries"
urlpatterns = [
    path('', views.entry_list_view, name='list'),
    path('create/', views.entry_create_view, name='create'),
]
