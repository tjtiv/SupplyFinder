from django.template.defaultfilters import register

@register.filter(name='price')
def price(n):
    if n < 0:
        n *= -1
    
    nSplit = str(n).split('.')

    if len(nSplit) == 1:
        priceStr = '$ '+nSplit[0]+'.00'
    else:
        dollar = '$ '+nSplit[0]
        cent = nSplit[1]
        if len(cent) > 2:
            cent = cent[0:2]
        elif len(cent) < 2:
            cent = cent+'0'
        priceStr = dollar+'.'+cent

    return priceStr 