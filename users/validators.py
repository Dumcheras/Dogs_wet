import re
from django.core.exceptions import ValidationError


def validate_password(field):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    if not bool(re.match(pattern, field)):
        raise ValidationError('Пароль должен содержать символы латинского алфавита и цифры')
    if not 8 <= len(field) <= 16:
        raise ValidationError('Длина пароля от 8 до 16 символов')
