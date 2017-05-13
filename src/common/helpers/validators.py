from django.core import exceptions
from src.common.libraries.constants import *
from rest_framework.status import HTTP_400_BAD_REQUEST

import re

def validate_user_name(name):
    if len(name) <= MAX_NAME_LENGTH and len(name) >= MIN_NAME_LENGTH and (re.match('^[\w ]+$', name) is not None):
        return True
    raise exceptions.ValidationError('Enter a valid username within length', code=HTTP_400_BAD_REQUEST)

def validate_user_hash(hash):
    condition = (len(hash) >= MIN_PASSWORD_LENGTH) and len(hash) <= MAX_PASSWORD_LENGTH

    if condition:
        return True
    raise exceptions.ValidationError('Password hash invalid', code=HTTP_400_BAD_REQUEST)

def validate_user_details(user_details):
    if not user_details:
        raise exceptions.ValidationError('Empty signup request', code=HTTP_400_BAD_REQUEST)
    if len(user_details) > len(SIGNUP_FIELDS) and not all( field in SIGNUP_FIELDS for field in user_details ):
        raise exceptions.ValidationError('Extra data supplied')

    return \
        validate_user_hash(user_details[KEY_PASSWORD_HASH]) and \
        validate_user_name(user_details[KEY_USER_NAME])

def validate_signin_details(signin_details):
    if not signin_details:
        raise exceptions.ValidationError('Empty signin request', code=HTTP_400_BAD_REQUEST)
    if len(signin_details) > len(SIGNIN_FIELDS) and not all( field in SIGNIN_FIELDS for field in signin_details ):
        raise exceptions.ValidationError('Extra data supplied')
    return validate_user_hash(signin_details[KEY_PASSWORD_HASH])

def validatejounerydetail(journey_detail):
    if not journey_detail:
        raise exceptions.ValidationError('Empty Booking request', code=HTTP_400_BAD_REQUEST)
    if not all( field in BOOKING_DETAILS for field in journey_detail ):
        raise exceptions.ValidationError('Extra payload passed')
    if journey_detail[KEY_SOURCE] == journey_detail[KEY_DESTINATION]:
        raise exceptions.ValidationError('Same source and destination')
    return True

def validatebooking(booking_detail):
    if not booking_detail:
        raise exceptions.ValidationError('Empty Booking request', code=HTTP_400_BAD_REQUEST)
    if not all( field in CONFIRM_DETAILS for field in booking_detail):
        raise exceptions.ValidationError('Extra payload passed')
    return True



