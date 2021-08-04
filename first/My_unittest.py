import unittest     # Импортируем модуль unittest


class TestAbs(unittest.TestCase):       # Создаём класс, который наследуется от класса TestCase
    def test_abs1(self):        # Превращаем тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")      # Изменяем assert на self.assertEqual()

    def test_abs2(self):
        self.assertEqual(abs(-42), 44, "Should be absolute value of a number")

    def test_abs3(self):
        self.assertEqual(abs(-10), 10, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()     # Заменяем строку запуска программы на unittest.main()


'''
Исходный текст тестов, до переделки на unittest:
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == 42, "Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
'''
