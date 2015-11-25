import pymorphy2
# import json
morph = pymorphy2.MorphAnalyzer()

items = ['сон']  #, 'окно', 'крокозяблик','синица','бегемот','зебра','рыба']
colors = ['быстрый', 'желтоватый', 'синий', 'белый', 'полосатая', 'прозрачный']
for item in items:
    for color in colors:
        for i in range(1, 12):
            w = morph.parse(item)[0].normalized
            #print(w.tag.gender)
            c = morph.parse(color)[0].normalized

            rest = ""
            if i == 1:
                rest = "{} всего {} {} {}".format(
                    morph.parse('Осталось')[0].inflect({w.tag.gender}).word.capitalize(),
                    i,
                    c.inflect({'nomn', 'ADJF', w.tag.gender}).word,
                    w.inflect({'nomn'}).word
                )
            else:
                rest = "{} всего {} {} {}".format(
                    'Осталось',
                    i,
                    c.make_agree_with_number(i).inflect({'accs', 'plur', 'ADJF'}).word,
                    w.make_agree_with_number(i).inflect({'gent', 'plur'}).word
                )

            adv = "Распродажа {}. {}".format(
                w.inflect({'gent', 'plur'}).word, # родительный падеж множественное число
                rest)
            print(adv)


