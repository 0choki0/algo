# 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 
# 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.

import sys
sys.stdin = open('input.txt', encoding='utf-8') 
#한글 파일을 인코딩하는 방법

man1 = input()
man2 = input()

rps = ['가위', '바위', '보']

man1_idx = rps.index(man1)
man2_idx = rps.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} win!')
else:
    if result == -1:
        print('Result : Man2 win!')
    else:
        print('Result : Man1 win!')


