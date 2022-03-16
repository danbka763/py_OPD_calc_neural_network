def build(keras, layers, DIGITS, MAXLEN, chars):
    print("Build model...")
    num_layers = 1

    model = keras.Sequential()
    # "Кодировать" входную последовательность с помощью LSTM, создавая выходные данные размером 128.
    model.add(layers.LSTM(128, input_shape=(MAXLEN, len(chars))))
    # По мере того как декодер выполняет ввод, повторно предоставлять последний вывод
    model.add(layers.RepeatVector(DIGITS + 1))

    for _ in range(num_layers):
        model.add(layers.LSTM(128, return_sequences=True))

    model.add(layers.Dense(len(chars), activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.summary()

    return model