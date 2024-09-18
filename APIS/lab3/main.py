import re

# Регулярные выражения для токенов
TOKEN_SPECIFICATION = [
    ('COMMENT',      r'{[^}]*}'),
    ('STRING',       r'"[^"]{0,32}"'),
    ('NUMBER',       r'\d+(\.\d+)?'),
    ('KEYWORD',      r'\b(record|integer|real|byte|word|char|string)\b'),
    ('IDENTIFIER',   r'[A-Za-z_][A-Za-z0-9_]{0,31}'),
    ('OPERATOR',     r'[=;:,.\[\]]'),
    ('WHITESPACE',   r'\s+'),
    ('MISMATCH',     r'.'),
]

TOKENS_REGEX = '|'.join(
    f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)

TOKEN_TYPES = {
    'KEYWORD': 'Ключевое слово',
    'IDENTIFIER': 'Идентификатор',
    'NUMBER': 'Число',
    'STRING': 'Строка',
    'OPERATOR': 'Оператор',
    'COMMENT': 'Комментарий',
    'MISMATCH': 'Ошибка'
}


class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text

    def tokenize(self):
        tokens = []
        for match in re.finditer(TOKENS_REGEX, self.input_text):
            token_type = match.lastgroup
            token_value = match.group(str(token_type))

            if token_type == 'WHITESPACE':
                continue
            elif token_type == 'MISMATCH':
                tokens.append((token_type, token_value, "Некорректный символ"))
            else:
                tokens.append((token_type, token_value))
        return tokens


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

    for token_type, token_value, *error in tokens:
        if error:
            print(f"{TOKEN_TYPES[token_type]}: '{token_value}' -> {error[0]}")
        else:
            print(f"{TOKEN_TYPES[token_type]}: '{token_value}'")
