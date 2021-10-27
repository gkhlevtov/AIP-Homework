class Text:
    """Класс, описывающий константный многострочный текстовый блок"""

    def __init__(self, txt):
        self.__txt = txt.split('\n')
        self.txt_lines = len(txt.split('\n'))

    def get_line(self, line_number):
        if line_number - 1 >= self.txt_lines:
            print('Выход за пределы количества строк')
        else:
            return self.__txt[line_number - 1]

    def get_line_words(self, line_number):
        if line_number - 1 >= self.txt_lines:
            print('Выход за пределы количества строк')
        else:
            return len(self.__txt[line_number - 1].split())

    def get_word(self, line_number, word_number):
        if line_number - 1 >= self.txt_lines:
            print('Выход за пределы количества строк')
        else:
            if word_number - 1 >= len(self.get_line(line_number).split()):
                print('Выход за пределы количества слов')
            else:
                return self.get_line(line_number).split()[word_number - 1]

    def __str__(self):
        return '\n'.join(self.__txt)


class EditableText(Text):
    """Класс, описывающий изменяемый многострочный текстовый блок"""

    def __init__(self, txt):
        Text.__init__(self, txt)
        self.__txt = txt.split('\n')
        self.txt_lines = len(txt.split('\n'))

    def set_line(self, line_number, line_text):
        if line_number - 1 >= self.txt_lines:
            print('Выход за пределы количества строк')
        else:
            self.__txt[line_number - 1] = str(line_text)

    def set_word(self, line_number, word_number, word):
        if line_number - 1 >= self.txt_lines:
            print('Выход за пределы количества строк')
        else:
            if word_number - 1 >= len(self.get_line(line_number).split()):
                print('Выход за пределы количества слов')
            else:
                line_list = self.get_line(line_number).split()
                line_list[word_number - 1] = str(word)
                self.set_line(line_number, str(' '.join(line_list)))
                return f'Слово "{self.get_line(line_number).split()[word_number - 1]}" заменено на слово "{word}"'

    def word_position(self, word):
        onestr_text = self.onestring_text().replace('.', '').replace(',', '')
        if word in onestr_text:
            return onestr_text.split().index(str(word)) + 1
        else:
            print('Слово не найдено')

    def onestring_text(self):
        return str(' '.join(self.__txt))

    def __str__(self):
        return '\n'.join(self.__txt)


pizza = 'Это Антон.\nОн любит пиццу.\nПицца очень вкусная,\nно он ненавидит пиццу с ананасами.'
text = Text(pizza)
ed_text = EditableText(pizza)
print(text)
print('---------------')
print(text.get_line_words(1))
print('---------------')
print(ed_text.set_word(4, 6, 'брокколи.'))
print('---------------')
print(ed_text)
print('---------------')
print(ed_text.onestring_text())
print('---------------')
print(ed_text.word_position('очень'))
