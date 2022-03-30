import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import load_model
from tkinter import messagebox


def generate_neural_network():
    # Модель Sequential представляет собой линейный стек слоев.
    # В качестве входных данных можно использовать массив narray.
    # Что бы создать нейронную сеть. Надо объявить модель Sequential добавить на неё слои:
    model = Sequential()
    model.add(Dense(3, input_shape=(2,), activation='sigmoid'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='sigmoid'))
    model.add(Dense(1, activation='relu'))
    # где 3/6/3/1 – количество нейронов, input_shape – размерность входных данных, activation – функция активации
    model.compile(loss='mse', optimizer='adam')  # ошибка - среднеквадратичная
    return model


def learning_model(self):
    # Формирование numpy-массива для обучения
    '''x = np.random.randint(1000, size=(10000, 2))
    y = np.transpose(np.subtract(np.transpose(x)))  # ответы для массива обучения (на сложение)'''
    '''x = np.random.randint(1000, size=(10000, 2))
    y = np.empty(len(x), dtype=int)
    for i in range(0, len(x)):
        y[i] = np.array(abs(np.transpose(x[i][0]) - np.transpose(x[i][1])))  # вопросы и ответы для вычитания
    self.fit(x, y, epochs=1000)  # обучение
    return self'''


if __name__ == '__main__':
    '''model = generate_neural_network()
    model = learning_model(model)
    model.save('multiplication.h5')  # эти строки создавали и обучали модель'''

model_for_additional = load_model('additional.h5')
model_for_subtraction = load_model('subtraction.h5')


def addition(input_data):  # функция сложения, входные данные в формате 'x+y'
    question_row = np.array(input_data.split('+'), dtype='float32')
    question = np.reshape(question_row, [1, 2])
    answ = model_for_additional.predict(question)
    return round(answ[0][0])


def subtraction(input_data):  # функция вычитания, входные данные в формате 'x-y'
    first_negative = False
    if input_data[0] == '-':
        question_row = np.array(input_data[1:].split('-'), dtype='float32')
        first_negative = True
    else:
        question_row = np.array(input_data.split('-'), dtype='float32')
    try:
        question = np.reshape(question_row, [1, 2])
    except ValueError:
        messagebox.showinfo('Ошибка', 'Обнулите калькулятор и вводите снова\nНе стоит первому числу быть отрицательным')
    if first_negative:
        question[0][0] = 0 - question[0][0]
    answ = model_for_subtraction.predict(question)
    if question[0][0] >= question[0][1]:
        return round(answ[0][0])
    else:
        return 0 - round(answ[0][0])


def multiplication(input_data):  # функция умножения, входные данные в формате 'x*y'
    question_row = np.array(input_data.split('*'), dtype='float32')
    question = np.reshape(question_row, [1, 2])
    if (question[0][0] < 0 and question[0][1] < 0) or (question[0][0] > 0 and question[0][1] > 0):
        negative = False
    else:
        negative = True
    for i in range(0, len(question)):
        answ = 0
        n = 0
        if abs(question[i][0]) >= abs(question[i][1]):
            while n < abs(question[i][1]):
                answ = addition(str(answ) + '+' + str(abs(question[i][0])))
                n += 1
        else:
            while n < abs(question[i][0]):
                answ = addition(str(answ) + '+' + str(abs(question[i][1])))
                n += 1
    if negative:
        return 0-round(answ)
    else:
        return round(answ)


def division(input_data):
    question_row = np.array(input_data.split('/'), dtype='float32')
    question = np.reshape(question_row, [1, 2])
    if question[0][1] == 0:
        messagebox.showinfo('Ошибка', 'Не стоит делить на ноль')
        return 0
    if question[0][0] == 0:
        return 0
    last = question[0][0]
    n = 0

    while True:
        last -= question[0][1]
        n += 1
        if last < question[0][1]:
            break
    if last>0:
        answ = str(n) + '.' + str(last/question[0][1])[2:]
    else:
        answ = str(n)
    return answ

