from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.exceptions.body_type_choice_exception import BodyTypeChoiceException
from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)


class AutoParkAddCarView(GenericAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data

        # valid_choices = [choice[1] for choice in BodyTypeChoices]
        # car_body_type = data['body_type']
        # if car_body_type not in valid_choices:
        #     raise BodyTypeChoiceException

        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validate_body_type(serializer.validated_data.get('body_type'))
        serializer.save(auto_park=auto_park)
        ap_serializer = self.get_serializer(auto_park)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)


