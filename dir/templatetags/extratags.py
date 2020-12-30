from django import template
from django.utils import translation
import idna

register = template.Library()


@register.filter()
def to_int(value):
    return int(value)


@register.filter()
def language_name_safe(value):
    try:
        val = translation.get_language_info(value)['name']
        return val
    except KeyError:
        return value


@register.filter()
def punycode(value):
    """
    Converts the value into a parenthetical expression if it's valid
    punycode, otherwise returns an empty string.
    """
    if not value:
        return ''
    if value.startswith('.'):
        value = value[1:]
    if not value or not value.startswith('xn--'):
        return ''
    return ' ({0})'.format(idna.decode(value))
