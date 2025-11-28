def run():
    print("=== 사칙연산 계산기 ===")
    print("1. 덧셈 (+)")
    print("2. 뺄셈 (-)")
    print("3. 곱셈 (*)")
    print("4. 나눗셈 (/)")
    
    choice = input("연산 선택: ")

    num1 = float(input("첫 번째 숫자: "))
    num2 = float(input("두 번째 숫자: "))

    if choice == "1":
        print(f"결과: {num1 + num2}")
    elif choice == "2":
        print(f"결과: {num1 - num2}")
    elif choice == "3":
        print(f"결과: {num1 * num2}")
    elif choice == "4":
        if num2 == 0:
            print("0으로는 나눌 수 없습니다.")
        else:
            print(f"결과: {num1 / num2}")
    else:
        print("올바른 메뉴 번호를 입력하세요.")
