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
    model.add(Dense(3, input_shape=(2,), activation='relu'))
    model.add(Dense(6, activation='relu'))
    model.add(Dense(3, activation='relu'))
    model.add(Dense(1, activation='elu'))
    # где 3/6/3/1 – количество нейронов, input_shape – размерность входных данных, activation – функция активации
    model.compile(loss='mse', optimizer='adam')  # ошибка - среднеквадратичная
    return model


def learning_model(self):
    # Формирование numpy-массива для обучения
    x = np.random.randint(1000, size=(10000, 2))
    y = np.transpose(sum(np.transpose(x)))  # ответы для массива обучения (на сложение)
    self.fit(x, y, epochs=100)  # обучение
    return model


if __name__ == '__main__':
    '''model = generate_neural_network()
    model = learning_model(model)
    model.save('additional.h5')''' # эти строки создавали и обучали модель для сложения чисел в диапазоне от 0 до 1000
    model = load_model('additional.h5')


def addition(input_data):  # функция сложения, входные данные в формате 'x+y'
    question_row = np.array(input_data.split('+'), dtype='float32')
    question = np.reshape(question_row, [1, 2])
    answ = model.predict(question)  # этот вызывает ошибку - неверный ввод
    return answ  # передать на выход


print(addition('1+2'))  # тестовый вызов функции
