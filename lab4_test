import unittest
import re
from lab4 import Text, Sentence, Word, Punctuation, Letter, Furniture, FurnitureManager

class TestTextClasses(unittest.TestCase):
    def test_letter_creation(self):
        l = Letter('Ф')
        self.assertEqual(l.char, 'Ф')
        self.assertEqual(str(l), 'Ф')

    def test_punctuation_creation(self):
        p = Punctuation('!')
        self.assertEqual(p.symbol, '!')
        self.assertEqual(str(p), '!')

    def test_word_creation(self):
        w = Word("Стіл")
        self.assertEqual(len(w.letters), 4)
        self.assertTrue(all(isinstance(letter, Letter) for letter in w.letters))
        self.assertEqual(str(w), "Стіл")

    def test_sentence_creation(self):
        s = Sentence("Привіт, світ!")
        self.assertEqual(len(s.components), 4)
        self.assertIsInstance(s.components[0], Word)
        self.assertIsInstance(s.components[1], Punctuation)
        self.assertEqual(str(s), "Привіт, світ!")

    def test_text_cleaning_and_structure(self):
        t = Text("Це   перше речення.   А це \t друге!  ")
        self.assertEqual(len(t.sentences), 2)
        self.assertEqual(str(t), "Це перше речення. А це друге!")

    def test_text_comparison(self):
        t1 = Text("Скло")
        t2 = Text("Скло")
        t3 = Text("Дерево")

        self.assertTrue(t1 == t2)
        self.assertFalse(t1 == t3)
        self.assertTrue(t3 < t1)


class TestFurnitureLogic(unittest.TestCase):
    def setUp(self):
        self.manager = FurnitureManager()
        self.manager.fill_inventory()

    def test_furniture_equality(self):
        f1 = Furniture("Стіл", "Скло", 150.0, 20.0, False)
        f2 = Furniture("Стіл", "Скло", 150.0, 20.0, False)
        f3 = Furniture("Стіл", "Дерево", 150.0, 20.0, False)

        self.assertEqual(f1, f2)
        self.assertNotEqual(f1, f3)

    def test_sorting_logic(self):
        self.manager.inventory.sort(key=lambda x: (x.price, -x.weight))
        inv = self.manager.inventory

        self.assertEqual(inv[0].price, 25.0)

        self.assertEqual(inv[1].price, 45.0)
        self.assertEqual(inv[1].weight, 6.2)
        self.assertEqual(inv[2].price, 45.0)
        self.assertEqual(inv[2].weight, 5.5)

        self.assertEqual(inv[-1].price, 500.0)

    def test_search_logic(self):
        target = Furniture("Стіл", "Скло", 150.0, 20.0, False)
        self.assertIn(target, self.manager.inventory)

        missing_target = Furniture("Шафа", "ДСП", 300.0, 50.0, False)
        self.assertNotIn(missing_target, self.manager.inventory)


if __name__ == "__main__":
    unittest.main()
