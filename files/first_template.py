'''ПЕРВЫЙ ШАБЛОН
Рядом с программой находится файл template.txt, в котором хранится шаблон текста. В шаблоне есть текст вида {{ name }}, который нужно заменить на реальное имя пользователя.

Напишите программу, которая принимает из первого аргумента командной строки имя пользователя, а затем подставляет его в шаблон и выводит результат.'''


from sys import argv
with open("template.txt") as f:
    t = f.read().replace("{{ name }}", argv[1])
    print(t)
