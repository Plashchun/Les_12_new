#1
June_dab = {'Mark', 'Oleksandr', 'Viktor', 'Bob', 'Max'}
July_dab = {'Mark', 'Oleksandr', 'Viktor', 'Bob', 'Max', 'John', 'Stepan', 'Valerii'}

all_months = June_dab.intersection(July_dab)
diff_months = July_dab.difference(June_dab)
print('Повинні за червень та липень', all_months)
print('Повинні за липень', diff_months)


#2
words = ['FootBall', 'BasketBoll', 'PlayHockey']
new_words = []
for word in words:
    new_word = ''
    for i, letter in enumerate(word):
        if i != 0 and letter.isupper():
            new_word += '_'
        new_word += letter.lower()
    new_words.append(new_word)
print(new_words)