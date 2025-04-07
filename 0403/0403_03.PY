# 카드 모양 SPAED, HEART, DIAMONDM, CLOVER
# 번호 1-A,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K
import random

cList = []

cShape = ["SPADE", "DIAMONDM", "CLOVER", "HEART"]

no = ["", "A", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for i in range(52):
    cList.append({"Shape": cShape[i // 13], "no": i % 13 + 1})

random.shuffle(cList)


def prtcard():
    for my, your in zip(myCard, youCard):
        if my['no'] > your['no']:
            card_no = no[my['no']]
            print("승리 카드 : ", card_no, end = " ")


# 카드 분배

myCard = []
youCard = []

for i in range(5):
    myCard.append(cList[i])

for i in range(5, 10):
    youCard.append(cList[i])

# 내 카드 출력
print("My Cards:")
for i in myCard:
    print(f"[{i['Shape']}]", no[i['no']])

# 상대 카드 출력
print("Enemy's Cards:")
for i in youCard:
    print(f"[{i['Shape']}]", no[i['no']])

# 카드 대수 비교
myWins = 0  # 내가 이긴 횟수
yourWins = 0  # 상대가 이긴 횟수

for my, your in zip(myCard, youCard):
    # 카드 번호를 비교하여 승패 결정
    if my['no'] > your['no']:
        myWins += 1  # 내가 이긴 경우
    elif my['no'] < your['no']:
        yourWins += 1  # 상대가 이긴 경우

# 결과 출력
print("\nGame Result:")
if myWins > yourWins:
    print(f"승리! ({myWins} vs {yourWins})")
    prtcard()
elif myWins < yourWins:
    print(f"패배! ({yourWins} vs {myWins})")
    prtcard()
else:
    print(f"무승부 ({myWins} vs {yourWins})")
    prtcard()

