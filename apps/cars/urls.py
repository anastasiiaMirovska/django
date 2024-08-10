from django.urls import path

from apps.cars.views import CarListCreateView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<slug:pk>', CarRetrieveUpdateDeleteView.as_view()),
]
