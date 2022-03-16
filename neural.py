from tensorflow import keras
from keras import layers
import numpy as np

from modules import generationData, vectorizationData, buildModel, educateNeural


chars = "0123456789+ "

# Параметры для модели и набора данных.
TRAINING_SIZE = 50000
DIGITS = 3
REVERSE = True

# Максимальная длина ввода равна 'int + int' (например, '345+678'). Максимальная его длина - ЦИФРЫ.
MAXLEN = DIGITS + 1 + DIGITS


questions, expected, ctable = generationData.gen(np, chars, TRAINING_SIZE, DIGITS, REVERSE, MAXLEN)

print(questions)

x_train, y_train, x_val, y_val = vectorizationData.vect(np, questions, expected, ctable, chars, DIGITS, MAXLEN)

print()

model = buildModel.build(keras, layers, DIGITS, MAXLEN, chars)

print()

model = educateNeural.educate(np, x_train, y_train, x_val, y_val, model, REVERSE, ctable)


# Погружаем данные в виде '312+214', ' 12+214', '  12+21', ...
def calc(str):
    pass