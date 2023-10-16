"""
Файл для тренировки и учёбы
"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int



def get_anot(word: str, num: int) -> str:
    """
    Получить анотацию для слова
    :param word: слово
    :param num: число
    :return: анотация
    """
    return f"{word} {num}"


def main():
    print("Hello from GitHub")
    print("new commit")

    person1 = Person("Peter", 20)
    print(person1)


if __name__ == "__main__":
    main()
