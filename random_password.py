import random

def make_random_password(length):
    password = " "

    for _ in range(length):
        password += str(random.randint( 0, 9))
        
    return password

print("= 랜덤 비밀번호 생성기 =")
length = int(input("비밀번호 길이를 입력하세요: "))

result = make_random_password(length)
print("생성된 비밀번호:", result)
