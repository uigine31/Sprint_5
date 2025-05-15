import unittest
import re

from online_sales_register import OnlineSalesRegisterCollector


class OSRTest(unittest.TestCase):

    def setUp(self):
        self.osr = OnlineSalesRegisterCollector()

    def tearDown(self):
        del self.osr

    def add_item(self, name, count=1):
        for _ in range(count):
            self.osr.add_item_to_cheque(name)

    def test_name_items_getter(self):
        "Тест геттера"

        self.assertEqual(self.osr.name_items, [])

    def test_nuber_items_getter(self):
        "Тест геттера"

        self.assertEqual(self.osr.nuber_items, 0)

    def test_add_item_to_cheque(self):
        "Тест добавление товара"

        self.osr.add_item_to_cheque('кола')
        self.osr.add_item_to_cheque('молоко')
        self.assertEqual(self.osr.name_items, ['кола', 'молоко'])
        self.assertEqual(self.osr.nuber_items, 2)

    def test_delete_item_from_check(self):
        "Тест удаление товара"

        self.osr.add_item_to_cheque('кола')
        self.osr.add_item_to_cheque('молоко')
        self.assertEqual(self.osr.name_items, ['кола', 'молоко'])
        self.assertEqual(self.osr.nuber_items, 2)
        self.osr.delete_item_from_check('молоко')
        self.assertEqual(self.osr.name_items, ['кола',])
        self.assertEqual(self.osr.nuber_items, 1)

    def test_check_amount_2_item(self):
        "Тест стоимости товаров 2 шт"

        self.add_item('кола', 2)
        self.assertEqual(self.osr.check_amount(), 200)

    def test_check_amount_10_item(self):
        "Тест стоимости товаров 10 шт"

        self.add_item('кола', 10)
        self.assertEqual(self.osr.check_amount(), 1000)

    def test_check_amount_11_item(self):
        "Тест стоимости товаров 11 шт"

        self.add_item('кола', 11)
        self.assertEqual(self.osr.check_amount(), 990)

    def test_check_amount_0_item(self):
        "Тест стоимости товаров 0 шт"

        self.assertEqual(self.osr.check_amount(), 0)

    def test_get_date_and_time(self):
        'Тест получение даты и времени'

        hour, minute, day, month, year = OnlineSalesRegisterCollector.get_date_and_time()
        self.assertTrue(re.match(r'^часы: \d+$', hour), 'Неправильный формат')
        self.assertTrue(re.match(r'^минуты: \d+$', minute), 'Неправильный формат')
        self.assertTrue(re.match(r'^день: \d+$', day), 'Неправильный формат')
        self.assertTrue(re.match(r'^месяц: \d+$', month), 'Неправильный формат')
        self.assertTrue(re.match(r'^год: \d+$', year), 'Неправильный формат')

    def test_get_telephone_number(self):
        "Тест получения корректного номера телефона"

        self.assertEqual(OnlineSalesRegisterCollector.get_telephone_number(1234567890), '+71234567890')

    def test_exception_add_item_to_cheque(self):
        "Тест проверки исключений и их текста при добавление товара"

        text = 'Нельзя добавить товар, если в его названии нет символов или их больше 40'
        text_2 = 'Позиция отсутствует в товарном справочнике'
        symbol_40 = 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdf'
        symbol_41 = 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfq'

        with self.assertRaises(ValueError) as context:
            self.osr.add_item_to_cheque('')
        self.assertEqual(str(context.exception), text)

        with self.assertRaises(ValueError) as context_41:
            self.osr.add_item_to_cheque(symbol_41)
        self.assertEqual(str(context_41.exception), text)

        with self.assertRaises(NameError) as context_40:
            self.osr.add_item_to_cheque(symbol_40)
        self.assertEqual(str(context_40.exception), text_2)

    def test_exception_delete_item_from_check(self):
        "Тест проверки исключений и их текста при удалении товара"

        text = 'Позиция отсутствует в чеке'
        with self.assertRaises(NameError)as context:
            self.osr.delete_item_from_check('test_name')
        self.assertEqual(str(context.exception), text)

    def test_exception_get_telephone_number(self):
        'Тест проверки ошибка номера телефона'
        with self.assertRaises(ValueError) as context:
            OnlineSalesRegisterCollector.get_telephone_number('stroka')
        self.assertEqual(str(context.exception), 'Необходимо ввести цифры')

        with self.assertRaises(ValueError) as context:
            OnlineSalesRegisterCollector.get_telephone_number(12345678901)
        self.assertEqual(str(context.exception), 'Необходимо ввести 10 цифр после "+7"')
