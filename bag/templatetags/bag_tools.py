from django import template

register = template.Library()


@register.filter(name='caluclate_sub_total')
def caluclate_sub_total(price, quantity):
    """ Template tag to calculate the  sub total """
    return price * quantity
