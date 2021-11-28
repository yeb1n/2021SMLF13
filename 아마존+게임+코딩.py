import random

print('"AmaZon 게임"을 시작하겠습니다.')
print('A부터 Z까지의 알파벳을 번갈아 불러 Z를 부르는 사람이 지는 게임입니다.')

alphabet = 0

turn = 0

end = 0

atoz=[0,'A','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','Z']

while True:
    if end == 1:
        print('게임이 끝났습니다.')
        break
    
    if turn == 0:
        p1 = int(input('말할 알파벳의 개수를 입력하세요.(1 ~ 3): '))
        
        
        while p1 > 3 or p1 < 1:
            p1 = int(input('1, 2, 3 중에서 하나를 입력해 주세요:'))
            
        for i in range(p1):
            alphabet += 1
            if alphabet >= 26:
                print('나:',atoz[26])
                end=1
                break
            print('나:', atoz[alphabet])

        turn += 1
        turn %= 2



    else:   
        p2 = random.randint(1, 3)
        for i in range(p2):
            alphabet += 1
            if alphabet >= 26:
                print('컴퓨터:',atoz[26])
                end=1
                break
            print('컴퓨터:', atoz[alphabet])

        turn += 1
        turn %= 2
        
if turn == 0:
    print('당신의 승리!')
    print('컴퓨터 패배...')
else:
    print('컴퓨터 승리!')
    print('당신의 패배...')
