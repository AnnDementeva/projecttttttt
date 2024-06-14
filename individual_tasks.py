__all__= ['find_contours', 'calculate_average_area', 'find_coordinates']
import cv2 as cv
import cv2 as cv2
import numpy as np
import pandas as pd

def find_contours(sort_df_type):
    """Функция, которая находит контуры областей кальциевых активностей
      в отсортированном массиве, содержащем картинки из конктретной папки 
      (принимает на вход определенный отсортированный массив)"""
    contourss = []
    list = sort_df_type['file_path'].tolist()
    for i in range(len(sort_df_type)):
        im = cv2.imread(str(list[i]))
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY) 
        ret, thresh = cv.threshold(imgray, 127, 255, 0) 
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contourss.append(contours)
    return contourss

def calculate_average_area(found_contours):
    """Функция, которая принимает на вход найденные контуры областей кальциевых активностей 
    с картинок определенной папки. Рассчитывает (6.3) среднюю площадь области в зависимости от времени."""
    list_average_area = []
    total_area = 0
    for i in range(len(found_contours)):
        for j in range(len(found_contours[i])):
            area = cv2.contourArea(found_contours[i][j])
            total_area += area
        average_area = total_area/(len(found_contours[i]))
        total_area = 0
        list_average_area.append(average_area)
    return list_average_area

def find_coordinates(found_contours):
    """Функция, которая принимает на вход найденные контуры областей кальциевых активностей 
    с картинок определенной папки. Рассчитывает (6.10) координаты центра самой большой 
    области в зависимости от номера кадра."""
    coordinates = []
    for i in range(len(found_contours)):
        largest_contour = max(found_contours[i], key=cv2.contourArea)

        # момент наибольшего контура
        M = cv2.moments(largest_contour)

        # координаты центра
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        coordinates.append((x, y))
    
    return coordinates