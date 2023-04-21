# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()


@register.filter
def format_number(value):
    if value >= 1000000000:
        return "{:.2f} bil ".format(value / 1000000000)
    elif value >= 1000000:
        return "{:.2f} mil ".format(value / 1000000)
    else:
        temp = str(value)
        mid = len(temp)//2
        return temp[:mid]+","+temp[mid:]


@register.filter
def format_name(value):
    print("-".join(list(value.split(' '))))
    return "-".join(list(value.split(' ')))
