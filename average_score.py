def run():
    print("=== 평균 점수 계산기 ===")
    
    scores = []
    n = int(input("몇 개의 점수를 입력할까요? : "))

    for i in range(n):
        score = float(input(f"{i+1}번째 점수: "))
        scores.append(score)

    avg = sum(scores) / n
    print(f"\n평균 점수는 {avg:.2f}점 입니다!")
