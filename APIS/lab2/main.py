KEYWORDS = {'record', 'integer', 'real', 'byte', 'word', 'char', 'string'}
OPERATORS = {';', '=', '[', ']', '(', ')', ':', ',', '.'}
WHITESPACE = {' ', '\t', '\n', '\r'}
COMMENT_START = '{'
COMMENT_END = '}'
MAX_ID_LENGTH = 32  # Максимальная длина идентификатора и строковых констант

TOKEN_TYPES = {
    'KEYWORD': 'Ключевое слово',
    'IDENTIFIER': 'Идентификатор',
    'OPERATOR': 'Оператор',
    'NUMBER': 'Число',
    'STRING': 'Строковая константа',
    'COMMENT': 'Комментарий',
    'ERROR': 'Ошибка'
}


class Token:
    def __init__(self, type_, value, position):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"{TOKEN_TYPES[self.type]}, '{self.value}', at position {self.position}"


class Lexer:
    def __init__(self, input_text):
        self.text = input_text
        self.position = 0
        self.tokens = []

    def get_char(self):
        """Возвращает текущий символ и переходит к следующему."""
        if self.position >= len(self.text):
            return None
        char = self.text[self.position]
        self.position += 1
        return char

    def peek_char(self):
        """Просматривает текущий символ, но не изменяет позицию."""
        if self.position >= len(self.text):
            return None
        return self.text[self.position]

    def tokenize(self):
        """Основной метод, который разбивает текст на токены."""
        while self.position < len(self.text):
            char = self.get_char()

            if char in WHITESPACE:
                continue

            if char == COMMENT_START:
                self.handle_comment()
                continue

            if char.isalpha() or char == '_':
                self.handle_identifier_or_keyword(char)
                continue

            if char.isdigit():
                self.handle_number(char)
                continue

            if char == '"':
                self.handle_string()
                continue

            if char in OPERATORS:
                self.tokens.append(Token('OPERATOR', char, self.position))
                continue

            self.tokens.append(Token('ERROR', char, self.position))

        return self.tokens

    def handle_comment(self):
        """Обрабатывает комментарии, пропуская текст до закрывающей скобки."""
        comment_content = ''
        while (char := self.get_char()) != COMMENT_END:
            if char is None:  # Ошибка: незакрытый комментарий
                self.tokens.append(
                    Token('ERROR', 'Unclosed comment', self.position))
                return
            comment_content += char
        self.tokens.append(Token('COMMENT', comment_content, self.position))

    def handle_identifier_or_keyword(self, char):
        """Обрабатывает идентификаторы или ключевые слова."""
        identifier = char
        while (char := self.peek_char()) and (char.isalnum() or char == '_'):
            identifier += self.get_char()
        if len(identifier) > MAX_ID_LENGTH:
            self.tokens.append(
                Token('ERROR', 'Identifier too long', self.position))
        elif identifier in KEYWORDS:
            self.tokens.append(Token('KEYWORD', identifier, self.position))
        else:
            self.tokens.append(Token('IDENTIFIER', identifier, self.position))

    def handle_number(self, char):
        """Обрабатывает числовые литералы."""
        number = char
        while (char := self.peek_char()) and char.isdigit():
            number += self.get_char()
        if char == '.':  # Это вещественное число
            number += self.get_char()
            while (char := self.peek_char()) and char.isdigit():
                number += self.get_char()
        self.tokens.append(Token('NUMBER', number, self.position))

    def handle_string(self):
        """Обрабатывает строковые константы."""
        string_literal = ''
        while (char := self.get_char()) != '"':
            if char is None:  # Ошибка: незакрытая строка
                self.tokens.append(
                    Token('ERROR', 'Unclosed string literal', self.position))
                return
            string_literal += char
        if len(string_literal) > MAX_ID_LENGTH:
            self.tokens.append(
                Token('ERROR', 'String too long', self.position))
        else:
            self.tokens.append(Token('STRING', string_literal, self.position))


if __name__ == "__main__":
    input_text = """
    record MyRecord;
    integer a;
    real b;
    string[30] str;
    { This is a comment }
    """

    lexer = Lexer(input_text)
    tokens = lexer.tokenize()

    print(*tokens, sep="\n")
