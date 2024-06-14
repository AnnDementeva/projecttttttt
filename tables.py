__all__= ['create_dict', 'save_excel']

from .data_frames import sorted_df_type
from .individual_tasks import find_contours, calculate_average_area, find_coordinates

def create_dict(choise, df):
    """Функция на выбор (choise) создает списки, 
    в которых буду хранится значения средней площади и координаты для каждой картинки во всех папках,
    на вход принимает 
    choise - выбор списка,
    df - дата фрейм, по которому будем считать значения"""
    dict = {}
    unique = df.types.unique()
    for i in range(len(unique)):
        s = sorted_df_type(df, unique[i])
        found_contours = find_contours(s)
        if choise == 'average_area':
            values = calculate_average_area(found_contours)
        elif choise == 'coordinat':
            values = find_coordinates(found_contours)
        key = unique[i]
        value = values
        dict[key] = value
    return dict

def save_excel(df, name):
   """Функция save_excel сохраняет data frame в excel таблицу 
       параметр df - data frame,
       параметр name - имя файла"""
   df.to_excel(f'{name}.xlsx', index= False)