def sqaures(n=10): # 10까지 자승하는 놈을 리턴
    for i in range(n+1): #매개변수 10을 받아서 1부터 10까지 범위 설정
        yield i**2 # i값을 제곱함


for x in sqaures(10): #함수를 매개변수로 받아서 for문을 돌림
    print(x)