def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    else:
        return ''.join([word if i > 0 else '#'+word for i,
                        word in enumerate(s.title().split(' '))])
    # your code here


generate_hashtag('')
generate_hashtag('Do We have A Hashtag')[0]
generate_hashtag('Codewars')
generate_hashtag('Codewars      ')
generate_hashtag('Codewars Is Nice')
generate_hashtag('codewars is nice')
generate_hashtag('CodeWars is nice')
generate_hashtag('c i n')
generate_hashtag('codewars  is  nice')
generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')
