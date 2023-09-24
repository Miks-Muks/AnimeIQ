from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('poll', views.PollCreateView.as_view(), name='poll'),
    path('list', views.FollowersListView.as_view(), name='list'),
    path('detail/<int:pk>', views.FollowerTopDetailView.as_view(), name='detail'),
]
