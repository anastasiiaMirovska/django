from django.urls import path

from apps.cars.views import CarAddPhotoView, CarListView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('', CarListView.as_view()),
    # path('/test', TestEmailView.as_view()),
    path('/<slug:pk>', CarRetrieveUpdateDeleteView.as_view()),
    path('/<slug:pk>/photo', CarAddPhotoView.as_view()),
]
