def locate_card(cards, query):
    pass

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

print(locate_card(**test['input']) == test['output'])


