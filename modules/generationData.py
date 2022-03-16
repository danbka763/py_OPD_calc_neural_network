import numpy as np


class CharacterTable:
    """Задан набор символов:
     + Закодировать их в однозначное целочисленное представление
     + Декодировать однозначное или целочисленное представление в их символьный вывод
     + Декодировать вектор вероятностей в их символьный вывод
    """

    def __init__(self, chars):
        """Инициализация таблицу символов.
            # Аргументы
            символы: Символы, которые могут отображаться во входных данных.
        """
        self.chars = sorted(set(chars))
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))

    def encode(self, C, num_rows):
        """Однократное горячее кодирование заданной строки C.
        # Аргументы
            C: строка, подлежащая кодированию.
            num_rows: Количество строк в возвращаемой однократной кодировке. Это
                      используется для того, чтобы количество строк для всех данных оставалось одинаковым.
        """
        x = np.zeros((num_rows, len(self.chars)))
        for i, c in enumerate(C):
            x[i, self.char_indices[c]] = 1
        return x

    def decode(self, x, calc_argmax=True):
        """Декодирование заданный вектор или 2D-массив в их символьный вывод.
        # Аргументы
            x: вектор или двумерный массив вероятностей или одномерных представлений;
                или вектор символьных индексов (используется с `calc_argmax=False`).
            calc_argmax: Следует ли находить символьный индекс с максимальным
                вероятность, значение по умолчанию равно "True`.
        """
        if calc_argmax:
            x = x.argmax(axis=-1)
        return "".join(self.indices_char[x] for x in x)


def gen(np, chars, TRAINING_SIZE, DIGITS, REVERSE, MAXLEN):
    ctable = CharacterTable(chars)

    questions = []
    expected = []
    seen = set()
    print("Получение данных...")
    while len(questions) < TRAINING_SIZE:
        f = lambda: int(
            "".join(
                np.random.choice(list("0123456789"))
                for i in range(np.random.randint(1, DIGITS + 1))
            )
        )
        a, b = f(), f()
        # Пропустить любые дополнительные вопросы, которые мы уже видели
        # Также пропустить любое рекурсивное, как x + Y == Y + x.
        key = tuple(sorted((a, b)))
        if key in seen:
            continue
        seen.add(key)
        # Заполнитб данные пробелами таким образом, чтобы они всегда были MAXLEN.
        q = "{}+{}".format(a, b)
        query = q + " " * (MAXLEN - len(q))
        ans = str(a + b)
        # Ответы могут иметь максимальный размер DIGITS + 1.
        ans += " " * (DIGITS + 1 - len(ans))
        if REVERSE:
            # Изменить запрос в обратном направлении, например, '12+345 ' станет '543+21'. (Обратить
            # внимание на пробел, используемый для заполнения)
            query = query[::-1]
        questions.append(query)
        expected.append(ans)

    print("Всего вариаций примеров:", len(questions))
    # print("Примеры:", questions)

    return questions, expected, ctable