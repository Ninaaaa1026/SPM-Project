import re

from django.core.exceptions import ValidationError

# Only allow letters, numbers, dots(.), underscores(_) and hyphens(-) in the name.
def name_validator(name):
    if not re.match(r'^[\w._-]+$', name):
        raise ValidationError('Usernames can only contain letters, numbers, dots(.), underscores(_) and hyphens(-).')

def phoneNumber_validator(phoneNumber):
    if not re.match("[0-9]", phoneNumber):
        raise ValidationError('PhoneNumber can only contain numbers.')