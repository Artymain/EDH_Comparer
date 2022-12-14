from requests_html import HTMLSession
import csv

session = HTMLSession()
r = session.get('https://edhrec.com/commanders/koma-cosmos-serpent')
r.html.render(sleep=3, keep_page=True, scrolldown=1)

sections = [('#newcards', []), ('#highsynergycards', []), ('#topcards', []),
            ('#creatures', []), ('#instants', []), ('#sorceries', []),
            ('#utilityartifacts', []), ('#enchantments', []),
            ('#planeswalkers', []), ('#utilitylands', []),
            ('#manaartifacts', []), ('#lands', [])]
all_cards = []
found_cards = []

for section in sections:
    sel = section[0] + ' .Card_name__vWL80'
    cards = r.html.find(sel)
    for name in cards:
        section[1].append(name.text)
        all_cards.append(name.text)
    #print(section[1])

with open('all-folders.csv', 'r') as file:
    reader = csv.reader(file)
    for each_row in reader:
        if len(each_row) > 1:
            card_name = each_row[3]
            if card_name in all_cards and card_name not in found_cards:
                print('You have: ' + card_name)
                found_cards.append(card_name)
