from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from core.paginations import PagePagination

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.less_than_year(2000).only_audi()
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)# Тепер на машинки можуть дивитись тільки залогінені юзери

    def get_queryset(self):
        print(self.request.user.profile.name, "!!!!!!!")
        return super().get_queryset()


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    # permission_classes = (IsAuthenticated,) # Ми хочемо тільки для видалення зробити щоб був аутентифікований, тому перевизначаємо метод

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)
