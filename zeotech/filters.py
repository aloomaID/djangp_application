from django import template

register = template.Library()

@register.filter
def split1(value, delimiter_and_index):
    delimiter, index = delimiter_and_index.split(',')
    parts = value.split(delimiter)
    if len(parts) > int(index):
        return parts[int(index)]
    return ""


@register.filter
def split2(value, delimiter_and_index):
    delimiter, index, delimiter1, index1 = delimiter_and_index.split(',')
    parts = value.split(delimiter)
    if len(parts) > int(index):
        return parts[int(index)].split(delimiter1)[int(index1)]
    return ""

@register.filter
def replace_data(value, delimiter_and_index):
    delimiter, index = delimiter_and_index.split(',')
    return value.replace(delimiter, index)

@register.filter
def replace_data_split(value, delimiter_and_index):
    delimiter, index, delimiter1, index1 = delimiter_and_index.split(',')
    parts = value.split(delimiter)
    if len(parts) > int(index):
        return parts[int(index)].replace(delimiter1, index1)
    return ""