#행렬의 성질을 익히면서 직접 해보기


#행렬의 놈 계산해보기
import numpy as np

A = (np.arange(9) - 4).reshape(3,3)
A

np.linalg.norm(A) #numpy의 linalg.norm()함수 이용

#trace 명령으로 대각합 구해보기
np.trace(np.eye(3))

#det 명령으로 행렬식 구하기
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.linalg.det(A)



#선형 연립방정식과 역행렬

#역행렬 사용해보기

import numpy as np

A = np.array([[1,1,0], [0,1,1], [1,1,1]])
A

Ainv = np.linalg.inv(A)
Ainv


#역행렬과 선형 연립방정식의 해

x = Ainv@b
x

A@x-b

#위 식의 결과가 0이 됨을 알 수 있다. Ax = b 이니까.

#lstsq()명령으로도 답 x를 구할 수 있다. 원래는 최소자승문제를 구하는 명령이지만 선형 연립방정식 해를 구할 때에도 사용 가능.
x, resid, rank, s = np.linalg.lstsq(A, b)
x
#결과가 이전에 역행렬 Ainv를 이용해 구한 것과 같음을 알 수 있다.


#보스턴 집값 문제. 
#범죄율, 공기 오염도, 방의 개수, 오래된 정도 4가지의 특징데이터 4개를 갖는 행렬 A
#우리가 구하려는 건 가중치 벡터 x (스몰 엑스)
#y가 집값.

from sklearn.datasets import load_boston
boston = load_boston()
X = boston.data
y = boston.target
A = X[:4, [0, 4, 5, 6]] #Crim(범죄율), Nox(공기 오염도), RM(방 개수), AGE(오래된 정도)
b = y[:4]

Ainv = np.linalg.inv(A)
x = np.dot(Ainv, b)
print(x)





#최소 자승 문제 실전.
#일단은 그냥 한 번 풀어보고 이후이 lstsq 함수 사용해서 풀어서 비교해보기

A = np.array([[1,1,0], [0,1,1], [1,1,1], [1,1,2]])
A

b = np.array([[2], [2], [3], [4.1]])
b

Apinv = np.linalg.inv(A.T@A)@A.T
Apinv

x = Apinv@b
x # [1, 1, 1]T가 나옴. 예제에서도 그랬음. x1, x2, x3가 1일 때 네개의 방정식으 비슷하게 만족시킴.

A@x #결과 : b와 굉장히 비슷함.



#이번에는 lstsq()함수를 이용해서 풀어보기.
#x는 계산결과벡터, resid는 잔차벡터의 놈값, rank는 rank, s는 고윳값. singular value의 's'.

x, resid, rank, s = np.linalg.lstsq(A, b)
x
#결과를 보면 linalg.inv함수 이용해서 직접 구할때랑 값 똑같이 나옴.




#보스턴 집값 문제를 최소 자승 문제로, lstsq 함수로 풀기

from sklearn.datasets import load_boston
boston = load_boston()
X = boston.data
y = boston.target

x, resid, rank, s = np.linalg.lstsq(X, y) #<-이렇게 한줄이면 된다는 게 포인트..
print(x)


