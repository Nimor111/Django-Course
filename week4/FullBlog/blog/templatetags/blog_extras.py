from django import template

register = template.Library()


@register.filter(name='truncate')
def truncate(string):
    return string[:20] + "..."
