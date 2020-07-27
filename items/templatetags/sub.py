from django.template.defaultfilters import register

@register.filter(name='sub')
def sub(a, b):
    return a-b