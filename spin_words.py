def spin_words(sentence):
    # lista = []
    # for each in sentence.split(' '):
    #   if len(each)>4:
    #     lista.append(each[::-1])
    #   else:
    #     lista.append(each)
    # return ' '.join(lista)

    print(' '.join([each[::-1] if len(each)>4 else each for each in sentence.split(' ')]))


spin_words("Welcome")
spin_words( "Hey fellow warriors" ) 
spin_words( "This is another test" )
spin_words( "This is a test")