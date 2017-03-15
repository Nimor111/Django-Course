from django import template
import markdown

register = template.Library()


@register.filter(name='markdown')
def convert_from_markdown(text):
    md = markdown.Markdown()
    return md.convert(text)
