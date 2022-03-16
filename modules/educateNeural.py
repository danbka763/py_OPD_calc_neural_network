epochs = 30
batch_size = 32


def educate(np, x_train, y_train, x_val, y_val, model, REVERSE, ctable):
    # Обучение модели каждого поколения и показ прогнозов в соответствии с набором данных проверки.
    for epoch in range(1, epochs):
        print()
        print("Итерация", epoch)
        model.fit(
            x_train,
            y_train,
            batch_size=batch_size,
            epochs=1,
            validation_data=(x_val, y_val),
        )
        # Выбор 10 выборок из набора проверки случайным образом, чтобы визуализировать ошибки.
        for i in range(10):
            ind = np.random.randint(0, len(x_val))
            rowx, rowy = x_val[np.array([ind])], y_val[np.array([ind])]
            preds = np.argmax(model.predict(rowx), axis=-1)
            q = ctable.decode(rowx[0])
            correct = ctable.decode(rowy[0])
            guess = ctable.decode(preds[0], calc_argmax=False)
            print("Q", q[::-1] if REVERSE else q, end=" ")
            print("T", correct, end=" ")
            if correct == guess:
                print("☑ " + guess)
            else:
                print("☒ " + guess)

    return  model