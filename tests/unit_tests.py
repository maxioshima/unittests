from anagrams.anagrams import remove_word
import unittest


class WordRemoveTest(unittest.TestCase):

    def test_of_expected_remove(self):  # тест при условии ожидаемых значений
        self.assertEqual(remove_word(''), '')
        self.assertEqual(remove_word('ab1'), 'ba1')
        self.assertEqual(remove_word('av12bd34'), 'db12va34')
        self.assertEqual(remove_word('cl1!bd?4 abc12'), 'db1!lc?4 cba12')

    def test_types(self):  # тест при условии нетипичных параметров
        self.assertRaises(TypeError, remove_word, 1)
        self.assertRaises(TypeError, remove_word, True)
        self.assertRaises(TypeError, remove_word, print())


if __name__ == '__main__':
    unittest.main()
