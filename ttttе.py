def load_text(filepath):
    """Загружает текст из файла.

    Args:
        filepath: Путь к текстовому файлу.

    Returns:
        Строка с текстом из файла, или None, если файл не найден.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # 'r' означает "читать", encoding='utf-8' поддерживает русский язык
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None

#  Правильный путь к файлу
filepath = r"C:\Users\Дарья\Desktop\14 лабораторная\text.txt"  # Укажите имя вашего текстового файла

text = load_text(filepath)

if text: #проверка, что текст загружен
    print("Текст успешно загружен!")
else:
    print("Загрузка текста не удалась.")
    exit()  # Останавливаем программу, если текст не загружен
tokens_split = text.split()  # Разбиваем текст по пробелам
print(f"Токенизация .split(): {tokens_split[:]}")
import re  # Импортируем модуль 're' для работы с регулярными выражениями

tokens_regex = re.findall(r'\w+', text.lower())  # Находим все слова (последовательности букв, цифр и символа подчеркивания)
print(f"Токенизация regex: {tokens_regex[:]}")


import nltk
import os
from nltk.tokenize import word_tokenize

# 1. Загрузка текста (предполагается, что у вас уже есть функция load_text)
def load_text(filepath):
    """Загружает текст из файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None

# Получаем текущую рабочую директорию
current_directory = os.getcwd()
print(f"Текущая рабочая директория: {current_directory}")

# Укажите имя файла (относительно текущей директории или абсолютный путь)
filepath = 'text.txt'  # Попробуйте сначала относительный путь

# Проверяем, существует ли файл по указанному пути
if not os.path.exists(filepath):
    print(f"Файл '{filepath}' не найден в текущей рабочей директории.")
    # Если не найден, предлагаем указать абсолютный путь
    filepath = input("Пожалуйста, введите полный (абсолютный) путь к файлу text.txt: ")
    # Проверяем, существует ли файл по введенному пользователем пути
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл '{filepath}' не найден. Проверьте правильность пути.")
        exit()

text = load_text(filepath)

if not text:
    exit()  # Завершаем, если текст не загружен

# 2. Загрузка ресурсов NLTK (если еще не загружены)
try:
    nltk.download('punkt')
    nltk.download('punkt_tab')  # Добавляем загрузку punkt_tab
except LookupError:
    print("Ошибка при загрузке ресурсов NLTK. Проверьте подключение к интернету и попробуйте еще раз.")
    exit()

# 3. Токенизация текста
tokens_nltk = word_tokenize(text)

# 4. Вывод токенов
print(f"Токенизация NLTK: {tokens_nltk[:]}")


count_len = len(tokens_nltk)  # Подсчитываем количество токенов в списке tokens_nltk
print(f"Количество слов (len): {count_len}")

from collections import Counter  # Импортируем класс Counter

count_counter = Counter(tokens_nltk)  # Создаем объект Counter из списка токенов
print(f"Самые частые слова (Counter): {count_counter.most_common(355)}")


tokens_no_punct = [token for token in tokens_nltk if token.isalpha()]  # Оставляем только токены, состоящие из букв
print(f"Токены без пунктуации: {tokens_no_punct[:]}")


from nltk.corpus import stopwords  # Импортируем модуль stopwords

nltk.download('stopwords')  # Загружаем список стоп-слов (если еще не загружен)

stop_words = set(stopwords.words("russian"))  # Получаем список стоп-слов для русского языка
tokens_no_stopwords = [token for token in tokens_no_punct if token not in stop_words]  # Удаляем стоп-слова из списка токенов
print(f"Токены без стоп-слов: {tokens_no_stopwords[:]}")


from nltk.stem import PorterStemmer  # Стеммер Портера (подходит для английского)
from nltk.stem.snowball import SnowballStemmer # Подходит для русского

stemmer = SnowballStemmer("russian") #Создаем стеммер для русского языка
stemmed_tokens = [stemmer.stem(token) for token in tokens_no_stopwords]  # Применяем стемминг к каждому токену
print(f"Стемминг (для русского): {stemmed_tokens[:]}")





import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import inspect

# Патч для inspect.getargspec (если требуется для вашей версии Python)
if not hasattr(inspect, 'getargspec'):
    def getargspec(func):
        sig = inspect.signature(func)
        args = [
            param.name for param in sig.parameters.values()
            if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        ]
        varargs = next((p.name for p in sig.parameters.values() if p.kind == inspect.Parameter.VAR_POSITIONAL), None)
        varkw = next((p.name for p in sig.parameters.values() if p.kind == inspect.Parameter.VAR_KEYWORD), None)
        defaults = tuple(param.default for param in sig.parameters.values()
                           if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD and param.default is not inspect.Parameter.empty)
        return inspect.FullArgSpec(
            args=args,
            varargs=varargs,
            varkw=varkw,
            defaults=defaults,
            kwonlyargs=[],
            kwonlydefaults=None,
            annotations={}
        )
    inspect.getargspec = getargspec

import pymorphy2

# 1. Загрузка текста
def load_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None

# 2. Загрузка ресурсов NLTK
def download_nltk_resources():
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
    except LookupError:
        print("Ошибка при загрузке ресурсов NLTK. Проверьте подключение к интернету и попробуйте еще раз.")
        return False
    return True

# 3. Токенизация текста
def tokenize_text(text):
    return word_tokenize(text)

# 4. Очистка текста
def clean_text(tokens, remove_punct=True, remove_stopwords=True):
    stop_words = set(stopwords.words('russian'))
    cleaned_tokens = tokens.copy()
    if remove_punct:
        cleaned_tokens = [token for token in cleaned_tokens if token.isalpha()]
    if remove_stopwords:
        cleaned_tokens = [token for token in cleaned_tokens if token not in stop_words]
    return cleaned_tokens

# 5. Лемматизация
def lemmatize_text(tokens):
    try:
        morph = pymorphy2.MorphAnalyzer()
        lemmatized_tokens = [morph.parse(token)[0].normal_form for token in tokens]
        print("Выполнена лемматизация")
        return lemmatized_tokens
    except Exception as e:
        print(f"Ошибка при лемматизации: {e}")
        print("Попробуйте установить более старую версию pymorphy2: pip install pymorphy2==0.8")
        print("Или обновите Python до версии 3.8 или выше.")
        return []

# 6. Стемминг
def stem_text(tokens):
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("russian")
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    print("Выполнен стемминг")
    return stemmed_tokens

# 7. Функция для построения графика частотности слов
def plot_top_words(tokens, n=20):
    counts = Counter(tokens)
    top_words = counts.most_common(n)
    words, counts = zip(*top_words)

    plt.figure(figsize=(12, 6))
    plt.bar(words, counts)
    plt.xticks(rotation=90)
    plt.xlabel("Слова")
    plt.ylabel("Частота")
    plt.title("Наиболее частотные слова")
    plt.tight_layout()
    plt.show()
# 8. Функция для получения грамматических характеристик
def get_grammemes(token):
    """Определяет грамматические характеристики слова.

    Args:
        token: Слово для анализа.

    Returns:
        Объект GramInfo с грамматическими характеристиками слова, или None, если анализ не удался.
    """
    try:
      morph = pymorphy2.MorphAnalyzer()
      parse = morph.parse(token)[0]  # Получаем первый вариант разбора
      return parse.tag #Возвращаем только Grammeme
    except Exception as e:
        print(f"Ошибка при определении грамматических характеристик: {e}")
        return None

# --- Основной код ---

# Получаем текущую рабочую директорию
current_directory = os.getcwd()
print(f"Текущая рабочая директория: {current_directory}")

# Укажите имя файла
filepath = 'text.txt'

# Проверяем, существует ли файл
if not os.path.exists(filepath):
    print(f"Файл '{filepath}' не найден в текущей рабочей директории.")
    filepath = input("Пожалуйста, введите полный (абсолютный) путь к файлу text.txt: ")
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл '{filepath}' не найден. Проверьте правильность пути.")
        exit()

# Загружаем текст
text = load_text(filepath)
if not text:
    exit()

# Загружаем ресурсы NLTK
if not download_nltk_resources():
    exit()

# Токенизируем текст
tokens_nltk = tokenize_text(text)

# Очищаем текст
cleaned_tokens = clean_text(tokens_nltk)

# Выбираем, что делать: лемматизировать или использовать стемминг
do_lemmatization = True
do_stemming = False

if do_lemmatization:
    lemmatized_tokens = lemmatize_text(cleaned_tokens)
elif do_stemming:
    lemmatized_tokens = stem_text(cleaned_tokens)
else:
    lemmatized_tokens = cleaned_tokens

# Получаем грамматические характеристики для примера
if lemmatized_tokens:
    sample_word = lemmatized_tokens[0]  # Берем первое слово из списка лемматизированных слов для примера
    grammemes = get_grammemes(sample_word)  # Получаем грамматические характеристики слова
    print(f"Грамматические характеристики слова '{sample_word}': {grammemes}")

    # Строим график, если есть слова
    plot_top_words(lemmatized_tokens)
else:
    print("Лемматизированный список токенов пуст. Невозможно получить грамматические характеристики и построить график.")






from nltk.text import Text

nltk_text = Text(tokens_nltk) #Используем исходные токены NLTK, чтобы было больше контекста

# similar
try:
    nltk_text.similar("информация") #Пример слова
except LookupError:
    print("Ошибка: Нужны дополнительные данные для NLTK.  Загрузите их, выполнив nltk.download('wordnet')")
else:
    print("Слова, похожие на 'информация':", nltk_text.similar("информация"))

# common_contexts
try:
    nltk_text.common_contexts(["информация", "безопасность"]) #Пример пары слов
except LookupError:
    print("Ошибка: Нужны дополнительные данные для NLTK.  Загрузите их, выполнив nltk.download('averaged_perceptron_tagger') и nltk.download('punkt')")
else:
    print("Общие контексты для 'информация' и 'безопасность':", nltk_text.common_contexts(["информация", "безопасность"]))

# collocations
print("Коллокации:", nltk_text.collocations())
