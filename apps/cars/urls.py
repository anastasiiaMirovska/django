from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<slug:pk>', CarRetrieveUpdateDeleteView.as_view()),
]
