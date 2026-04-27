import re
# [Перша частина]

class Letter:
    def __init__(self, char: str):
        self.char = char

    def __repr__(self):
        return self.char


class Punctuation:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol


class Word:
    def __init__(self, word_str: str):
        self.letters = [Letter(c) for c in word_str]

    def __repr__(self):
        return "".join(str(letter) for letter in self.letters)


class Sentence:
    def __init__(self, sentence_str: str):
        self.components = []

        tokens = re.findall(r"[\w'-]+|[.,!?;:]", sentence_str)
        for token in tokens:
            if re.match(r"[\w'-]+", token):
                self.components.append(Word(token))
            else:
                self.components.append(Punctuation(token))

    def __repr__(self):
        result = ""
        for comp in self.components:
            if isinstance(comp, Punctuation):
                result += str(comp)
            else:
                if result and not result.endswith((" ", "\t", "\n")):
                    result += " "
                result += str(comp)
        return result.strip()


class Text:
    def __init__(self, text_str: str):
        cleaned_text = re.sub(r'[ \t]+', ' ', text_str).strip()

        self.sentences = []

        raw_sentences = re.split(r'(?<=[.!?]) +', cleaned_text)
        for rs in raw_sentences:
            if rs:
                self.sentences.append(Sentence(rs))

    def __eq__(self, other: object):
        if isinstance(other, Text):
            return str(self) == str(other)
        return False

    def __lt__(self, other: object):
        if isinstance(other, Text):
            return str(self) < str(other)
        return NotImplemented

    def __repr__(self):
        return " ".join(str(sentence) for sentence in self.sentences)


# [Друга частина]

class Furniture:
    def __init__(self, category: str, material: str, price: float, weight: float, is_assembled: bool):
        self.category = Text(category)
        self.material = Text(material)
        self.price = price
        self.weight = weight
        self.is_assembled = is_assembled

    def __eq__(self, other: object):
        if not isinstance(other, Furniture):
            return NotImplemented
        return (self.category == other.category and
                self.material == other.material and
                self.price == other.price and
                self.weight == other.weight and
                self.is_assembled == other.is_assembled)

    def __repr__(self):
        return (f"Furniture(категорія='{self.category}', матеріал='{self.material}', "
                f"ціна={self.price}, вага={self.weight}, зібрано={self.is_assembled})")


class FurnitureManager:
    def __init__(self):
        self.inventory = []

    def fill_inventory(self):
        self.inventory = [
            Furniture("Стілець", "Дерево", 45.0, 5.5, True),
            Furniture("Стіл", "Скло", 150.0, 20.0, False),
            Furniture("Стілець", "Пластик", 25.0, 2.0, True),
            Furniture("Диван", "Штучна    шкіра", 500.0, 45.0, True),
            Furniture("Стілець", "Дерево", 45.0, 6.2, True),
            Furniture("Робочий \t стіл", "Метал", 180.0, 18.0, False)
        ]

    def display_all(self, message: str):
        print(f"\n--- {message} ---")
        for item in self.inventory:
            print(item)

    def execute_lab_task(self):
        self.fill_inventory()
        self.display_all("Початковий стан масиву")

        self.inventory.sort(key=lambda x: (x.price, -x.weight))

        self.display_all("Масив після сортування (Ціна: зростання, Вага: спадання)")
        target = Furniture("Стіл", "Скло", 150.0, 20.0, False)
        print(f"\nШукаємо об'єкт: {target}")

        found = False
        for index, item in enumerate(self.inventory):
            if item == target:
                print(f"Успіх! Знайдено ідентичний об'єкт під індексом: {index}")
                print(item)
                found = True
                break

        if not found:
            print("Ідентичний об'єкт не знайдено.")


def main():
    app = FurnitureManager()
    app.execute_lab_task()


if __name__ == "__main__":
    main()
