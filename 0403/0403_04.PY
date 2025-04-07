import random

def generate_winning_numbers():
    # 랜덤으로 6개의 당첨 번호를 생성
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def get_user_numbers():
    # 사용자로부터 6개의 번호를 입력받아 반환
    user_numbers = []
    print("1부터 45 사이의 숫자 6개를 입력하세요.")
    while len(user_numbers) < 6:
        try:
            num = int(input(f"{len(user_numbers) + 1}번째 번호: "))
            if num < 1 or num > 45:
                print("1부터 45 사이의 숫자를 입력하세요.")
            elif num in user_numbers:
                print("이미 입력한 숫자입니다. 다른 숫자를 입력하세요.")
            else:
                user_numbers.append(num)
        except ValueError:
            print("숫자를 입력하세요.")
    user_numbers.sort()
    return user_numbers

def check_matching_numbers(winning_numbers, user_numbers):
    # 당첨 번호와 사용자 번호를 비교하여 맞춘 번호 반환
    matched_numbers = []
    for win_num in winning_numbers:
        for user_num in user_numbers:
            if win_num == user_num:
                matched_numbers.append(win_num)
    return matched_numbers


while True:
    print("[ 로또 프로그램 ]")
    print("-" * 60)
    input_ = int(input("시작 : 1번 \t 종료 : 2번 \n: "))
    if input_ == 1:
        winning_numbers = generate_winning_numbers()
        user_numbers = get_user_numbers()
        print(f"입력한 번호: {user_numbers}")
        matched_numbers = check_matching_numbers(winning_numbers, user_numbers)
        print(f"맞춘 번호: {sorted(matched_numbers)}")
        print(f"총 {len(matched_numbers)}개 맞췄습니다!")
        print(f"당첨 번호: {winning_numbers}")
        if {len(matched_numbers)} == 6:
            print("!!당첨!!")
    elif input_ == 2:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
