# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:43:08 2024

@author: ASUS
"""
import numpy as np

def create_array(array_lenght):
    rand_array = np.random.randint(0, 21, array_lenght)
    return rand_array

def append_array(array1, array2):
    array3 = np.append(array2, array1)
    return array3

def sort_array(array):
    array_asc = np.sort(array)
    array_desc = array_asc[::-1]
    array_sym = array_asc + array_desc
    return array_sym

def scale(array_in):
    array_scaled = np.round((array_in * 20 / np.max(array_in)), 2)
    return array_scaled

def matrix_sum(matrix):
    sum_all = np.sum(matrix)
    sum_row = np.sum(matrix, axis=1)
    sum_column = np.sum(matrix, axis=0)
    return sum_all, sum_row, sum_column
