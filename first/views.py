from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from first.models import CarModel


# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs): #Користувач отримує дані з апки
#         print(self.request.query_params.dict())
#         return Response("hello from get all")
#
#     def post(self, *args, **kwargs): #Користувач записує дані на апку
#         print(self.request.data)
#         return Response("hello from post")
#
#
# class CarRetrieveUpdateDeleteView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response("hello from get single")
#
#     def put(self, *args, **kwargs):  # Користувач ПОВНІСТЮ оновлює дані про якийсь елемент
#         return Response("hello from put")
#
#     def patch(self, *args, **kwargs):  # Користувач ЧАСТКОВО оновлює дані про якийсь елемент
#         return Response("hello from patch")
#
#     def delete(self, *args, **kwargs):  # Видаляємо якісь дані
#         return Response("hello from delete")


#Create
#Read/ Retrieve
#Update
#Delete

class CarListCreateView(APIView):
    def get(self, *args, **kwargs): #Користувач отримує дані з апки
        cars = CarModel.objects.all()
        res = [model_to_dict(car) for car in cars]
        return Response(res, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs): #Користувач записує дані на апку
        data = self.request.data
        car = CarModel.objects.create(**data)
        car_dict = model_to_dict(car)
        return Response(car_dict, status=status.HTTP_201_CREATED)


class CarRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(car), status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):  # Користувач ПОВНІСТЮ оновлює дані про якийсь елемент
        pk = kwargs.get('pk')
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found")
        car.brand = data["brand"]
        car.price = data["price"]
        car.year = data["year"]
        car.save()
        return Response(model_to_dict(car), status=status.HTTP_200_OK)

    # def patch(self, *args, **kwargs):  # Користувач ЧАСТКОВО оновлює дані про якийсь елемент
    #     return Response("hello from patch")

    def delete(self, *args, **kwargs):  # Видаляємо якісь дані
        pk = kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            return Response("not found")
        return Response(status=status.HTTP_204_NO_CONTENT)


