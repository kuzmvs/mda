# Задание 2
# Напишите функцию, меняющую каждое третье (начиная с 0) значение массива целых чисел на заданное число.
# Например, если на вход поступает массив `array([3, 5, 1, 0, -3, 22, 213436])`
# и число `-111`, то на выходе должен получиться массив `array([-111, 5, 1, -111, -3, 22, -111])`.
#
# %%
import numpy as np


def change_array(array, number):
    for i in range(0, array.size):
        if i == 0 or (i + 3) % 3 == 0:
            array[i] = number


array = np.array([3, 5, 1, 0, -3, 22, 213436])
number = -111
change_array(array, number)
print(array)
