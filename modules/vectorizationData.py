def vect(np, questions, expected, ctable, chars, DIGITS, MAXLEN):
    print("Векторизация данных...")
    x = np.zeros((len(questions), MAXLEN, len(chars)), dtype=np.bool)
    y = np.zeros((len(questions), DIGITS + 1, len(chars)), dtype=np.bool)
    for i, sentence in enumerate(questions):
        x[i] = ctable.encode(sentence, MAXLEN)
    for i, sentence in enumerate(expected):
        y[i] = ctable.encode(sentence, DIGITS + 1)

    # Перемешать (x, y), так как более поздние части x почти все будут больше.
    indices = np.arange(len(y))
    np.random.shuffle(indices)
    x = x[indices]
    y = y[indices]

    # Явно выделяем 10% для проверки данных, которые никогда не обрабатываем.
    split_at = len(x) - len(x) // 10
    (x_train, x_val) = x[:split_at], x[split_at:]
    (y_train, y_val) = y[:split_at], y[split_at:]

    print("Тренировочные данные:")
    print(x_train.shape)
    print(y_train.shape)

    print("Валидированные данные:")
    print(x_val.shape)
    print(y_val.shape)

    return x_train, y_train, x_val, y_val