#coding=utf-8
'''
Created on 2015年10月8日

@author: 10256603
'''

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats':Category.objects.all(),'act_cat':cat}