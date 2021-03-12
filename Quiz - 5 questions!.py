import requests
import json
import random
import html

url = 'https://opentdb.com/api.php?amount=1'
stat_game = True
score = [0,0]
print('5 questions game!')
for number_que in range(5):
    req = requests.get(url)
    data = json.loads(req.text)
    que = data['results'][0]['question']
    ans = data['results'][0]['incorrect_answers']
    c_ans = data['results'][0]['correct_answer']
    ans.append(c_ans)
    random.shuffle(ans)

    print('\n' + html.unescape(que) + '\n')
    l_pref = ['a', 'b', 'c', 'd']
    j = 0
    for i in ans:
        pref = l_pref[j]
        print(pref + ' - ' + html.unescape(i))
        j += 1

    if j == 2:
        user_ans = input('\n Type "a" or "b" : ')
        while user_ans not in l_pref[:2]:
            user_ans = input('\n Type "a" or "b" : ')
    if j == 4:
        user_ans = input('\n Type "a" or "b" or "c" or "d" : ')
        while user_ans not in l_pref:
            user_ans = input('\n Type "a" or "b" or "c" or "d" : ')
    index_user = l_pref.index(user_ans)

    if ans[index_user] == c_ans:
        print('Correct answer!')
        score[0] += 1
    else:
        print(f'Wrong, correct answer is "{l_pref[ans.index(c_ans)]}" : {c_ans}')
        score[1] += 1
    if number_que < 4:
        print(f'Your score is {score[0]} : {score[1]}')
    else:
        print(f'\n          Your final score is {score[0]} : {score[1]}')