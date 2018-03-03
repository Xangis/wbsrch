from django import template
from django.utils import translation

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)

@register.filter()
def language_name_safe(value):
    try:
        val = translation.get_language_info(value)['name']
    except KeyError:
        return value
