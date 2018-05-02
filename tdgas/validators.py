import re

from django.core.exceptions import ValidationError

# Only allow letters, numbers, dots(.), underscores(_) and hyphens(-) in the name.
def name_validator(name):
    if not re.match(r'^[\w._-]+$', name):
        raise ValidationError('Names can only contain letters, numbers, dots(.), underscores(_) and hyphens(-).')

def phone_number_validator(phone_number):
    if not re.match("[0-9]", phone_number):
        raise ValidationError('Phone numbers can only contain numbers.')