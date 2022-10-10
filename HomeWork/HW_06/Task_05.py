"""Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
in
10 True
out

['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый',
'город позавчера утопичный']
in
10 False
out

['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый',
'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый',
'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']"""

from random import randrange


def main(num, unique=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if unique:
        num = min(num, len(nouns), len(adverbs), len(adjectives))

    res = []
    for i in range(num):
        noun = nouns[randrange(0, len(nouns))]
        adverb = adverbs[randrange(0, len(adverbs))]
        adjective = adjectives[randrange(0, len(adjectives))]

        if unique:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)

        res.append(" ".join([noun, adverb, adjective]))

    return res


n = int(input())
print(main(n))
