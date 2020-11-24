def title_case(title, minor_words=''):
    final_list = []
    for i, each in enumerate(title.split(' ')):
        if each.lower() in minor_words.lower().split(' ') and i > 0:
            final_list.append(each.lower())
        else:
            final_list.append(each.title())
    print(' '.join(final_list))


title_case('')
title_case('a clash of KINGS', 'a an the of')
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')
