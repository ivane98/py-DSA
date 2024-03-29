def test_location(cards, query, mid):
    mid_n = cards[mid]
    if mid_n == query:
        if mid -1 >= 0 and cards[mid -1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_n < query:
        return 'left'
    else:
        return 'right'

def locate_cards(cards, q):
    l, h = 0, len(cards) - 1

    while l <= h:
        mid = (l + h) // 2
        result = test_location(cards, q, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            h = mid - 1
        elif result =='right':
            l = mid + 1
    return -1

cards = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(locate_cards(cards, 8))