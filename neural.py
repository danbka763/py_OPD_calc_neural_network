from tensorflow import keras
from keras import layers
import numpy as np
from keras.models import load_model
from modules import generationData, vectorizationData, buildModel, educateNeural


chars = "0123456789+ "

# Параметры для модели и набора данных.
TRAINING_SIZE = 50000
DIGITS = 3
REVERSE = True

# Максимальная длина ввода равна 'int + int' (например, '345+678'). Максимальная его длина - ЦИФРЫ.
MAXLEN = DIGITS + 1 + DIGITS


questions, expected, ctable = generationData.gen(np, chars, TRAINING_SIZE, DIGITS, REVERSE, MAXLEN)

#print(questions)

x_train, y_train, x_val, y_val = vectorizationData.vect(np, questions, expected, ctable, chars, DIGITS, MAXLEN)

print()

#model = buildModel.build(keras, layers, DIGITS, MAXLEN, chars)

print()

#model = educateNeural.educate(np, x_train, y_train, x_val, y_val, model, REVERSE, ctable)
model = load_model('my_model.h5')
#model.save('my_model.h5')


# Погружаем данные в виде '312+214', ' 12+214', '  12+21', ...
# Пока не понятен тип данных на вход
def calc(input_data):
    ind = np.random.randint(0, len(x_val))
    question = np.array(input_data.split('+'), dtype='int')
    rowx, rowy = x_val[np.array(question)], y_val[np.array([ind])]
    preds = np.argmax(model.predict(rowx), axis=-1)
    q = input_data
    correct = ctable.decode(rowy[0])
    guess = ctable.decode(preds[0], calc_argmax=False)
    print("Q", q[::-1] if REVERSE else q, end=" ")
    print("T", correct, end=" ")
    print("☑ " + guess)

    '''question = np.array(input_data.split('+'), dtype='float32')
    answ = model.predict(question)  # этот вызывает ошибку - неверный ввод
    return answ  # передать на выход'''


print(calc('3+2'))  #тестовый вызов функции
