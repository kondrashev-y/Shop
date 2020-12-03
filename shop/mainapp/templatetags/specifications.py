from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone, Notebook

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """


TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>

                """


# PRODUCT_SPEC = {
#     'notebook': {
#         'Диагональ': 'diagonal',
#         'Тип дисплея': 'display_type',
#         'Частота процессора': 'processor_freq',
#         'Оперативная память': 'ram',
#         'Видеокарта': 'video',
#         'Время работы аккамулятора': 'time_without_charge'
#     },
#     'smartphone': {
#         'Диагональ': 'diagonal',
#         'Тип дисплея': 'display_type',
#         'Разрешение экрана': 'resolution',
#         'Оперативная память': 'ram',
#         'Емкость батареи': 'accum_value',
#         'Наличие слота для SD карты': 'sd',
#         'Максимальный объем SD карты': 'sd_volume_max',
#         'Обьем встроенной памяти': 'store_max',
#         'Главная камера': 'main_cam_mp',
#         'Фронтальная камера': 'frontal_cam_mp'
#     }
# }


def get_product_spec(product, model_name):
    table_content = ''
    spec_dict = {}
    print(get_dict(product, model_name))
    for name, value in get_dict(product, model_name)[model_name].items():
        if name == 'Наличие sd карты':
            if getattr(product, value):
                spec_dict[name] = 'Да'
            else:
                spec_dict[name] = 'Нет'
        elif name == 'Максимальный объем SD карты' and not getattr(product, 'sd'):
            pass
        else:
            spec_dict[name] = getattr(product, value)
        # table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    for name, value in spec_dict.items():
        table_content += TABLE_CONTENT.format(name=name, value=value)
    return table_content

def get_dict(model, model_name):
    dict_spec = {}
    del_list = ('ID', 'Категория', 'Наименование', 'slug', 'Изображение', 'Описание', 'Цена')
    dict_spec[model_name] = {}
    for i in model._meta.fields:
        if i.verbose_name not in del_list:
            dict_spec[model_name][i.verbose_name] = i.name
    return dict_spec



@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    # if isinstance(product, Smartphone):
    #     if not product.sd:
    #         PRODUCT_SPEC['smartphone'].pop('Максимальный объем SD карты', False)
    #     else:
    #         PRODUCT_SPEC['smartphone']['Максимальный объем SD карты'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)