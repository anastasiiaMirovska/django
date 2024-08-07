# from django.forms import model_to_dict
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from first.models import CarModel
# from first.serializers import CarSerializer
#
# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs): #Користувач отримує дані з апки
#         cars = CarModel.objects.all()
#         serializer = CarSerializer(instance=cars, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs): #Користувач записує дані на апку
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDeleteView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response("not found", status=status.HTTP_404_NOT_FOUND)
#         serializer = CarSerializer(instance=car)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):  # Користувач ПОВНІСТЮ оновлює дані про якийсь елемент
#         pk = kwargs.get('pk')
#         data = self.request.data
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response("not found")
#         serializer = CarSerializer(instance=car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response("not found")
#         serializer = CarSerializer(instance=car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):  # Видаляємо якісь дані
#         pk = kwargs.get('pk')
#         try:
#             car = CarModel.objects.get(pk=pk)
#             car.delete()
#         except CarModel.DoesNotExist:
#             return Response("not found")
#         return Response(status=status.HTTP_204_NO_CONTENT)







# from django.db.models import Q
# from rest_framework.response import Response
# from rest_framework import status
# from first.models import CarModel
# from first.serializers import CarSerializer
# from rest_framework.generics import GenericAPIView
#
#
# class CarListCreateView(GenericAPIView):
#     def get(self, *args, **kwargs):  # Користувач отримує дані з апки
#         # qs = CarModel.objects.all()
#         # qs = qs.filter(brand__in=["Renault", "audi"], year=2014)
#
#         # qs = CarModel.objects.filter(brand__in=["Renault", "audi"], year=2014)
#
#         # qs = CarModel.objects.filter(Q(brand__in=["Renault", "BMW"]) & Q(price__gt=2000) | Q(year__lt=2020)).exclude(
#         #     brand="BMW").order_by('price',
#         #                           '-brand')  # можна ще додавати .count() і воно рахує кількість таких знайдених елементів; щоб сортувати в протилежному порядку, потрібно перед назвою поля поставити мінус; .reverse() робить усе навпаки
#         qs = CarModel.objects.filter(Q(brand='Renault')).values('id','brand')
#
#         print(qs.query)
#         serializer = CarSerializer(instance=qs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):  # Користувач записує дані на апку
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDeleteView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs.get('pk')
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status=status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(instance=car)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):  # Користувач ПОВНІСТЮ оновлює дані про якийсь елемент
#         # pk = kwargs.get('pk')
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found")
#         car = self.get_object()
#         serializer = CarSerializer(instance=car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs.get('pk')
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found")
#         car = self.get_object()
#         serializer = CarSerializer(instance=car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):  # Видаляємо якісь дані
#         # pk = kwargs.get('pk')
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         #     car.delete()
#         # except CarModel.DoesNotExist:
#         #     return Response("not found")
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






# from rest_framework.response import Response
# from rest_framework import status
#
# from first.filter import car_filter
# from first.models import CarModel
# from first.serializers import CarSerializer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get_queryset(self):
#         return car_filter(self.request.query_params)
#
#     # def get_serializer(self, *args, **kwargs):
#     #     return super().get_serializer(*args, **kwargs)
#
#     # def get_object(self):
#     #     return super().get_object()
#
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)







from rest_framework.response import Response
from rest_framework import status

from first.filter import car_filter
from first.models import CarModel
from first.serializers import CarSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)

class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
