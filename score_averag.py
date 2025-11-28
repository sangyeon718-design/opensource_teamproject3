def feature_average():
    n = int(input("요소 개수 입력: "))
    scores = input("점수 입력: ").split()
    sum_s = 0
    for i in range(n):
        sum_s += int(scores[i])

    print(f"평균 점수: {sum_s / n}")

