from itertools import groupby


d1 = {'swiped_on':'2015-04-29 15:21:50', 'member_id': 712461, 'card_number': 422951, 'granted': False , 'club_id ': 8}
d2 = {'swiped_on':'2015-04-29 15:42:52', 'member_id': 712461, 'card_number': 424911, 'granted': True , 'club_id ': 10}
d3 = {'swiped_on':'2015-04-29 17:36:25', 'member_id': 821665, 'card_number': 425905, 'granted': False , 'club_id ': 9}
d4 = {'swiped_on':'2015-04-29 17:36:28', 'member_id': 821665, 'card_number': 425905, 'granted': False , 'club_id ': 9}
d5 = {'swiped_on':'2015-04-29 17:36:31', 'member_id': 821665, 'card_number': 425905, 'granted': True , 'club_id ': 9}
d6 = {'swiped_on':'2015-04-29 18:07:21', 'member_id': 515466, 'card_number': 425180, 'granted': True , 'club_id ': 12}
d7 = {'swiped_on':'2015-04-29 18:17:16', 'member_id': 515466, 'card_number': 420357, 'granted': True , 'club_id ': 6}
d8 = {'swiped_on':'2015-04-29 18:27:49', 'member_id': 988462, 'card_number': 422951, 'granted': False , 'club_id ': 9}
d9 = {'swiped_on':'2015-04-29 18:27:52', 'member_id': 988462, 'card_number': 427695, 'granted': True , 'club_id ': 9}
d10 = {'swiped_on':'2015-04-29 18:28:02', 'member_id': 515466, 'card_number': 423751, 'granted': True , 'club_id ': 12}

swipe = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

def filter_duplicate_swipes(swipes):
    l2=sorted(swipes, key=lambda d: (d['member_id'], -sum(1 for v in d.values() if v))) 
    n = [next(d) for _,d in groupby(l2, key=lambda _d: _d['member_id'])]

    for swipe in n: 
        filtered_swipes = swipe['swiped_on'], swipe['member_id'], swipe['granted']
        print(filtered_swipes)

filter_duplicate_swipes(swipe)