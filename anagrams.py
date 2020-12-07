def anagrams(word, words):

    lista = []
    word = [each for each in word]
    word.sort()

    for each in words:
        each2 = [letter for letter in each]
        each2.sort()
        if each2 == word:
            lista.append(each)

    return lista


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams(
    'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
