from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'photo', 'created_at', 'updated_at')

    def validate_body_type(self, value):
        choices = dict(BodyTypeChoices.choices)
        if value not in choices:
            raise serializers.ValidationError(
                f"Invalid status '{value}'. Valid choices are: {', '.join(choices.keys())}"
            )
        return value


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}
