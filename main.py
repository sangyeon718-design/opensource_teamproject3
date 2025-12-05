import Unit_conversion 
import feature_average_score
import calculator

def main():
    while True:
        print("\n==== Main Menu ====")
        print("1. Unit Conversion")
        print("2. Calculator")
        print("3. Feature Average Score")
        print("4. Change Calculation")
        print("5. Random Password Generator")
        print("0. Exit")

        choice = input("메뉴 입력: ").strip()

        if choice == "1":
            Unit_conversion.unit_conversion()
        elif choice == "2":
            calculator.run()
        elif choice == "3":
            feature_average_score.feature_average()
        elif choice == "4":
            import change
            change.change()
        elif choice == "5":
            import random_password
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")


if __name__ == "__main__":
    main()
