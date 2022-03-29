import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import load_model


def generate_neural_network():
    # Модель Sequential представляет собой линейный стек слоев.
    # В качестве входных данных можно использовать массив narray.
    # Что бы создать нейронную сеть. Надо объявить модель Sequential добавить на неё слои:
    model = Sequential()
    model.add(Dense(3, input_shape=(2,), activation='elu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='elu'))
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
        y[i] = np.array(abs(np.transpose(x[i][0]) - np.transpose(x[i][1])))  # вопросы и ответы для вычитания'''
    x = np.random.randint(1000, size=(10000, 2))
    y = np.empty(len(x), dtype=int)
    for i in range(0, len(x)):
        number = 0
        n = 0
        if x[i][0] >= x[i][1]:
            while n < x[i][1]:
                number += np.transpose(x[i][0])
                n += 1
        else:
            while n < x[i][0]:
                number += np.transpose(x[i][1])
                n += 1
        y[i] = np.array(number)
    self.fit(x, y, epochs=1000000)  # обучение
    return self


if __name__ == '__main__':
    '''model = generate_neural_network()
    model = learning_model(model)
    model.save('multiplication.h5')  # эти строки создавали и обучали модель'''

model_for_additional = load_model('additional.h5')
model_for_subtraction = load_model('subtraction.h5')
#model_for_multiplication = load_model('multiplication.h5')


def addition(input_data):  # функция сложения, входные данные в формате 'x+y'
    question_row = np.array(input_data.split('+'), dtype='float32')
    question = np.reshape(question_row, [1, 2])
    answ = model_for_additional.predict(question)
    return round(answ[0][0])


def subtraction(input_data):  # функция вычитания, входные данные в формате 'x-y'
    question_row = np.array(input_data.split('-'), dtype='float32')
    question = np.reshape(question_row, [1, 2])
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
