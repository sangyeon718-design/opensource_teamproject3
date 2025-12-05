## 과제 소개(기능 설명, 팀 역할 분담)  
주제: 미니 도구 모음  
사용 언어: Python  

- 기능/역할분담  
main.py : 권나현, 김상연  
1. 단위 변환기(Unit_conversion): 김상연  
2. 간단 계산기(calculator.py): 정은담  
3. 점수 평균 계산(feature_average_score.py): 권나현  
4. 문자열 처리(change.py): 김민성  
5. 랜덤 비밀번호 생성기(random_password.py): 안찬모  


## 실행 방법  
main.py를 실행하면 메뉴 번호를 입력받아 각 기능에 해당하는 모듈(.py 파일)을 실행한다.  

## Git 협업 기록  
- Pull Request 수  
김상연:
정은담:
권나현:
김민성:
안찬모:
  
- 충돌 해결 경험  
main 브랜치와 correction/menu 브랜치에서 main.py 파일을 서로 다르게 수정하였다.  

main 브랜치의 main.py 내용: print("잘못된 입력하였습니다. 다시 입력하세요.")  
correction/menu 브랜치의 main.py 내용: print("잘못된 입력입니다. 다시 입력하세요.")  

두 브랜치를 병합하는 과정에서 main.py에 충돌이 발생하였고, GitHub 웹 에디터에서 correction/menu 브랜치의 수정사항을 선택하여 충돌을 해결하였다.  

충돌 해결 후에는 Pull Request 병합 옵션 중 Squash and Merge를 사용하여 여러 커밋을 하나의 커밋으로 정리하여 병합하였다.  
이 과정으로 main.py의 충돌이 깔끔하게 해결되었고, 최종 병합이 완료되었다.  
