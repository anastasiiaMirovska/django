from datetime import datetime

from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from core.services.file_service import FileService

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=15, validators=(
        V.MinLengthValidator(3),
        V.RegexValidator(*RegexEnum.BRAND.value)
    ))
    price = models.IntegerField(validators=(V.MinValueValidator(1), V.MaxValueValidator(1_000_000)))
    year = models.IntegerField(validators=(V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)))
    body_type = models.CharField(max_length=9)
    # auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    # photo = models.ImageField(upload_to=FileService.upload_car_photo, blank=True, validators=(
    #     V.FileExtensionValidator(['jpg', 'jpeg']),
    # ))

    objects = CarManager()
