from copy import deepcopy

from django import template
from django.utils import simplejson
from django.db.models import Count, F
from django.template import resolve_variable

register = template.Library()

def to_dictionary(param_string):
    "Split an http param string into a dictionary"
    params = {}
    kv_strings = param_string.split('&')
    for kv_string in kv_strings:
        key, value = kv_string.split('=')
        params[key] = value
    return params

def to_string(param_dict):
    "Take a dictionary and convert it to a parameter string"
    params = "?"
    for k, v in param_dict.iteritems():
        params += "%(key)s=%(value)s&" % {'key': k, 'value': v}
    return params[:-1]
    
@register.simple_tag()
def param_link(request, title, param_string):
    "Build a parameter string based on an existing request and new param values"
    
    default_dict = {
        'page': 1, 'per_page': 10,
        'type': 'list'
    }
    old_dict = deepcopy(default_dict)
    new_dict = deepcopy(default_dict)

    for k, v in request.GET.iteritems():
        old_dict[k] = v
    new_dict.update(to_dictionary(param_string))
    
    for k in old_dict.keys():
        if k not in new_dict or str(old_dict[k]) != str(new_dict[k]):
            return "<a href='%(url)s' title='%(title)s'>%(title)s</a>" % {'url': to_string(new_dict), 'title': title}
    return title

@register.simple_tag()
def page_link(request, page_number):
    return param_link(request, str(page_number), 'page=' + str(page_number))