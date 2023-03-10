from sys import argv

digits = {
    1: {"ru": "один", "en": "one"},
    2: {"ru": "два", "en": "two"},
    3: {"ru": "три", "en": "three"},
    4: {"ru": "четыре", "en": "four"},
    5: {"ru": "пять", "en": "five"},
    6: {"ru": "шесть", "en": "six"},
    7: {"ru": "семь", "en": "seven"},
    8: {"ru": "восемь", "en": "eight"},
    9: {"ru": "девять", "en": "nine"},
    0: {"ru": "ноль", "en": "zero"}
}

key1 = int(argv[1])
key2 = argv[2]

print(digits[key1][key2])
