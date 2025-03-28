import random



while True:
    print("[ 프로그램 구현]")
    print("-"*20)
    print("1. 숫자 맞추기")
    print("2. 로또 맞추기")
    print("3. 학생 성적 프로그램")
    print("0. 종료")
    print("-"*20)

    choice = int(input("원하시는 숫자를 눌러주세요 : "))

    if choice > 3:
        print("항목 내 번호를 입력해주세요")
        
    if choice == 1:
        print("-" * 20)
        print("숫자 맞추기\n")

        q1_1 = []
        q1_2 = []
        match_count = 0

        while len(q1_1) < 3:
            ran_num_1 = random.randint(1, 11)
            if ran_num_1 not in q1_1:
                q1_1.append(ran_num_1)
                
        
        while len(q1_2) < 3:
            input_num = int(input(q1_2,"번째 숫자를 입력해주세요"))
            if input_num in q1_2:
                pass
            else:
                q1_2.append(input_num)

        for num in q1_1:
            if num in q1_2:
                match_count += 1
            
        if match_count == 2:
            print("정답입니다")

    








    if choice == 2:
        print("로또 맞추기")
        
    if choice == 3:
        print("학생 성적 프로그램")
        
    if choice == 0:
        pass


