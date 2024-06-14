__all__ = ['find_dependence_square', 'find_dependence_coordinates', 'save_graphic']

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def find_dependence_square(type, df):
    """Функция выводит график средней площади кальциевого события в зависимости от времени
    параметр df - data frame, из которого берут столбцы, которые буду использоваться 
    для построения графика, а именно 'time' и 'average_area',
    параметр type - название графика (график по конуертной папке),
    возвращаемое значение - фигура с графиком"""
    right_time = (df['time']/2)/60
    x = right_time.tolist()
    y = df['average_area'].tolist()
    graph_height = (8.3 - 1.8) #11.7 x 8.3 дюймов, поделила на 3 длину и вычла границы
    graph_width = ((8.3 - 1.58)/3)
    fig = plt.figure(figsize=(graph_height, graph_width), dpi = 300)
    plt.plot(x, y, color = '#F08080', linewidth = 2.5) 
    plt.title(f'Зависимость средней площади кальциевого события \n {type} от времени')
    plt.xlabel('Момент наблюдения, мин.')
    plt.ylabel('Средняя площадь, мкм^2')
    plt.xticks(np.arange(int(min(x)), int(max(x))+1, 1.0)) # Отображает только целые значения времени на графике
    plt.grid()
    plt.show
    return fig

def find_dependence_coordinates(type, df):
    """Функция выводит график найденных координат в зависимости от времени
    параметр df - data frame, из которого берут столбцы, которые буду использоваться 
    для построения графика, а именно 'time' и 'coordinates',
    параметр type - название графика (график по конуертной папке),
    возвращаемое значение - фигура с графиком"""  
    right_time = (df['time']/2)/60
    x = right_time.tolist()
    coordinat = df['coordinates'].tolist()
    x_coordinates, y_coordinates = zip(*coordinat)
    graph_height = (8.3 - 1.8) #11.7 x 8.3 дюймов, поделила на 3 длину и вычла границы
    graph_width = ((8.3 - 1.58)/3)
    fig = plt.figure(figsize=(graph_height, graph_width), dpi = 300)
    plt.plot(x, x_coordinates, label='координата x',  color = '#66CDAA', linewidth = 2) 
    plt.plot(x, y_coordinates, label='координата y', color = '#8A2BE2', linewidth = 2) 
    plt.title(f"Зависимость координат центра самой большой области \n {type} от времени")
    plt.xlabel('Момент наблюдения, мин.')
    plt.ylabel('Координаты, мкм^2')
    plt.legend(loc='upper left', fontsize=6)
    plt.xticks(np.arange(int(min(x)), int(max(x))+1, 1.0)) # Отображает только целые значения времени на графике
    plt.grid()
    plt.show
    return fig

def save_graphic(fig,observation):
    """Функция save_fig сохраняет графики в форматах .png и .svg
       парметр fig - фигура с графиком
       параметр observation - название директории с данными"""
    fig.savefig(f"{observation}.png", dpi=300)
    fig.savefig(f"{observation}.svg", dpi=300)