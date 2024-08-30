from django.urls import path

from apps.users.views import UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create')
]