import Unit_conversion
import average_score
import feature_average_score
import change
import random_password

def main():
    while True:
        print("\n==== Main Menu ====")
        print("1. Unit Conversion")
        print("2. Average Score")
        print("3. Feature Average Score")
        print("4. Change Calculation")
        print("5. Random Password Generator")
        print("0. Exit")

        choice = input("메뉴 입력: ")

        if choice == "1":
            unit_conversion()
        elif choice == "2":
            average_score.calculate_average()
        elif choice == "3":
            feature_average()
        elif choice == "4":
            change.change()
        elif choice == "5":
            make_random_password()
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("다시 입력하세요.")

if __name__ == "__main__":
    main()
