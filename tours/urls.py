from django.urls import path

from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.TourListView.as_view(), name='index'),

]
