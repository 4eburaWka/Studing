# Имена файлов
LEXER=lexer.l
PARSER=parser.y
EXECUTABLE=parser.out

# Сгенерированные файлы
BISON_SRC=y.tab.c
BISON_HEADER=y.tab.h
LEX_SRC=lex.yy.c

# Компилятор
CC=gcc
CFLAGS=-lfl

# Правило по умолчанию
all: $(EXECUTABLE)

# Генерация файлов Yacc
$(BISON_SRC) $(BISON_HEADER): $(PARSER)
	yacc -d $(PARSER)

# Генерация файлов Lex
$(LEX_SRC): $(LEXER)
	lex $(LEXER)

# Правило для сборки исполняемого файла
$(EXECUTABLE): $(BISON_SRC) $(LEX_SRC)
	$(CC) -o $(EXECUTABLE) $^ $(CFLAGS)

# Очистка сгенерированных файлов
clean:
	rm -f $(EXECUTABLE) $(BISON_SRC) $(BISON_HEADER) $(LEX_SRC)

.PHONY: all clean
