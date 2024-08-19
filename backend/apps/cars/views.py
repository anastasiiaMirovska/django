from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.paginations import PagePagination
from core.permissions.is_super_user_permission import IsSuperUser
from core.services.email_service import EmailService

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)
    # permission_classes = (IsSuperUser,)# Оскільки ми поставили дефолтний permission у rest_conf, то нам вже не потрібно нічого тут прописувати

    def get_queryset(self):
        return super().get_queryset()


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,) # Ми хочемо тільки для видалення зробити щоб був аутентифікований, тому перевизначаємо метод

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)



class CarAddPhotoView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)# Дозволяємо виконувати тільки метод put

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)


# class TestEmailView(GenericAPIView):
#     permission_classes = (AllowAny,)
#
#     def get(self,*args,**kwargs):
#         EmailService.send_test()
#         return Response(status=status.HTTP_204_NO_CONTENT)
