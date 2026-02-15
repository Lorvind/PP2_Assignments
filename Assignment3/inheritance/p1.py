class FlashCard:
    def __init__(self, front: str, back: str):
        self.front = front
        self.back = back

    def show_front(self):
        print(self.front)
    def show_back():
        print(self.front)

class JapaneseCard(FlashCard):
    def __init__(self, front: str, back: str, romaji: str):
        self.front = front
        self.back = back
        self.romaji = romaji
    def show_furigana(self):
        print(self.romaji)


fruit = JapaneseCard("果物", "Fruit", "kudamono")

fruit.show_front()
fruit.show_furigana()