__all__ = ['conclusion'] #название главных вызываемсых функций через запитую

import glob
import cv2 as cv
import cv2 as cv2
import pandas as pd
from glob import glob
from pathlib2 import Path
import matplotlib.pyplot as plt
import numpy as np

from .data_frames import create_data_frame, sorted_df_type
from .individual_tasks import find_contours, calculate_average_area, find_coordinates
from .graphics import find_dependence_square, find_dependence_coordinates, save_graphic
from .tables import create_dict, save_excel

def conclusion(dir):
    """Функция, которая содержит в себе все необходимые функции,
    на вход принимает dir - название директории, в которой находятся папки с наблюдениями, 
    выводит графики всех папок и таблицу со значениями средних площадей областей 
    кальциевых активностей всех картинок,
    а также сохраняет графики в двух форматах (png и svg) 
    и таблицы со средними значениями площадей областей кальциевых активностей и 
    координатами центров самых больших областей в зависимости от номера кадра"""
    current_dir = Path.cwd()
    dirs_path_mask = current_dir / dir / '**'
    dirs_names = glob (str(dirs_path_mask))
    observations =[]
    for dir_name in dirs_names:
        observations.append(dir_name.split('\\')[-1])

    df_image = create_data_frame('image', dir)
    df_event = create_data_frame('event', dir)

    for i in range(len(observations)):
        sort_df_type = sorted_df_type(df_event, observations[i])
        found_contours = find_contours(sort_df_type)

        area = calculate_average_area(found_contours)
        sort_df_type = sort_df_type.assign(average_area = area)

        coordinates = find_coordinates(found_contours)
        sort_df_type = sort_df_type.assign(coordinates = coordinates)

        fig_square = find_dependence_square(observations[i], sort_df_type)
        fig_coordinates = find_dependence_coordinates(observations[i], sort_df_type)

        save_graphic(fig_square, observations[i])
        save_graphic(fig_coordinates, observations[i])

    Average_Area = pd.DataFrame(create_dict('average_area', df_event))
    Coordinates = pd.DataFrame(create_dict('coordinat', df_event))
    save_excel(Average_Area, 'average_area')
    save_excel(Coordinates, 'coordinates')
    return Average_Area


    

