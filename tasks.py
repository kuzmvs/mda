# Задание 1
# Напишите функцию, возвращающую округленную взвешенную сумму оценок по данным оценкам и весам.
# Можете посчитать свою оценку за курс :)
#
# %%
import numpy as np


def result_mark(weights, marks):
    return sum(w * m for w, m in zip(weights, marks))


weights = np.array([0.35, 0.4, 0.15, 0.1])
marks = np.array([6, 9, 8, 7])
result_mark(weights, marks)

# Задание 2
# Напишите функцию, меняющую каждое третье (начиная с 0) значение массива целых чисел на заданное число.
# Например, если на вход поступает массив `array([3, 5, 1, 0, -3, 22, 213436])`
# и число `-111`, то на выходе должен получиться массив `array([-111, 5, 1, -111, -3, 22, -111])`.
#
# %%
import numpy as np


def change_array(array, number):
    # from start to end, exclusive, set every 3nd element to "number"
    array[::3] = number


array = np.array([3, 5, 1, 0, -3, 22, 213436])
number = -111
change_array(array, number)
print(array)
