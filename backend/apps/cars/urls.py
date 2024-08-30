from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDeleteView

# from apps.cars.views import CarAddPhotoView

urlpatterns = [
    path('', CarListView.as_view(), name='cars_list_create'),
    # path('/test', TestEmailView.as_view()),
    path('/<slug:pk>', CarRetrieveUpdateDeleteView.as_view()),
    # path('/<slug:pk>/photo', CarAddPhotoView.as_view()),
]
