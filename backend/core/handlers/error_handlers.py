from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.cars.choices.body_type_choices import BodyTypeChoices


def error_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validation_error_handler,
        'BodyTypeChoiceException': _body_type_choice_error_handler
    }

    response = exception_handler(exc, context)
    exc_class = exc.__class__.__name__
    if exc_class in handlers:
        return handlers[exc_class](exc, context)
    return response


def _jwt_validation_error_handler(exc: Exception, context: dict) -> Response:
    return Response({'detail': 'Token is invalid or expired'}, status=status.HTTP_403_FORBIDDEN)


def _body_type_choice_error_handler(exc: Exception, context: dict) -> Response:
    valid_choices = [choice[1] for choice in BodyTypeChoices.choices]
    return Response({'detail': f'Invalid body type. It must be one of these variants: {" | ".join(valid_choices)}'}, status=status.HTTP_400_BAD_REQUEST)

