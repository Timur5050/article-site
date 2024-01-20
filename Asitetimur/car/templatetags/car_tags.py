from django import template
import car.views as views
from car.models import Category

register = template.Library()


@register.inclusion_tag('car/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}