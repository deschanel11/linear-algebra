# 벡터의 평행이동 그려보기

import numpy as np
import matplotlib.pylab as plt

plt.rc("font", size = 18) #그림의 폰트 크기를 18로 고정
gray = {"facecolor" : "gray"}
black = {"facecolor" : "black"}
red = {"facecolor" : "red"}
green = {"facecolor" : "green"}
blue = {"facecolor" : "blue"}

a = np.array([1, 2])
plt.plot(0,0,'kP', ms=20)
plt.plot(a[0], a[1], 'ro', ms = 20)
plt.annotate('', xy=[-0.6, 1.6], xytext=(0.2, 0.7), arrowprops=gray)
plt.annotate('', xy=a, xytext = (0,0), arrowprops = black)
plt.annotate('', xy=a + [-1, 1], xytext=(-1, 1), arrowprops = black)
plt.text(0.35, 1.15, "$a$")
plt.text(1.15, 2.25, "$(1,2)$")
plt.text(-0.7, 2.1, "$s$")
plt.text(-0.9, 0.6, "평행이동")
plt.xticks(np.arange(-2, 4))
plt.yticks(np.arange(-1, 4))
plt.xlim(-2.4, 3.4)
plt.ylim(-0.8, 3.4)
plt.show()



#스칼라와 벡터의 곱

'''벡터에 양의 실수를 곱하면 방향은 변하지 않고 실수의 크기만큼 벡터의 길이가 커지고,
음의 실수를 곱하면 벡터의 방향이 반대가 된다.'''

a = np.array([1, 2])
b = 2*a
c=-a
plt.annotate('', xy=b, xytext = (0,0), arrowprops = red)
plt.text(0.8, 3.1, "$2a$")
plt.text(2.2, 3.8, "$(2,4)$")
plt.annotate('', xy=a, xytext=(0,0), arrowprops = gray)
plt.text(0.1, 1.3, "$a$")
plt.text(1.1, 1.4, "$(1, 2)$")
plt.plot(c[0], c[1], 'ro', ms=10)
plt.annotate('', xy=c, xytext = (0,0), arrowprops = blue)
plt.text(-1.3, -0.8, "$-a$")
plt.text(-3, -2.5, "#(-1, -2)$")
plt.plot(0,0,'kP', ms=20)
plt.xticks(np.arange(-5, 6))
plt.yticks(np.arange(-5, 6))
plt.xlim(-4.4, 5.4)
plt.ylim(-3.2, 5.2)
plt.show()


#단위벡터 : 길이가 1인 벡터.

a = np.array([1, 0])
b = np.array([0, 1])
c = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
np.linalg.norm(a), np.linalg.norm(b), np.linalg.norm(c)




#벡터의 합
#방법 1 : 평행사변형

a = np.array([1, 2])
b = np.array([2, 1])
c = a + b

plt.annotate('', xy=a, xytext = (0,0), arrowprops = gray)
plt.annotate('', xy=b, xytext = (0,0), arrowprops = gray)
plt.annotate('', xy=c, xytext = (0,0), arrowprops = black)

plt.plot(0,0,'kP', ms=10)
plt.plot(a[0], a[1], 'ro', ms=10)
plt.plot(b[0], b[1], 'ro', ms = 10)
plt.plot(c[0], c[1], 'ro', ms = 10)

plt.plot([a[0], c[0]], [a[1], c[1]], 'k--')
plt.plot([b[0], c[0]], [b[1], c[1]], 'k--')

plt.text(0.35, 1.15, "$a$")
plt.text(1.15, 0.25, "$b$")
plt.text(1.25, 1.45, "$c$")
plt.xticks(np.arange(-2,5))
plt.yticks(np.arange(-1, 4))
plt.xlim(-1.4, 4.4)
plt.ylim(-0.6, 3.8)
plt.show()



#방법 2 : 삼각형

a = np.array([1, 2])
b = np.array([2,1])
c = a + b

plt.annotate('', xy=a, xytext = (0,0), arrowprops = gray)
plt.annotate('', xy=c, xytext = a, arrowprops = gray)
plt.annotate('', xy=c, xytext = (0,0), arrowprops = gray)

plt.plot(0,0, 'kP', ms = 10)
plt.plot(a[0], a[1], 'ro', ms=10)
plt.plot(c[0], c[1], 'ro', ms=10)

plt.text(0.35, 1.15, "$a$")
plt.text(1.45, 2.45, "$b$")
plt.text(1.25, 1.45, "$c$")

plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1, 4))
plt.xlim(-1.4, 4.4)
plt.ylim(-0.6, 3.8)
plt.show()

#둘 중 하나를 평행이동해도 벡터의 합의 결과는 마찬가지.
#벡터의 합은 교환법칙이 성립한다.

a = np.array([1, 2])
b = np.array([2, 1])
c = a + b
c
c = b + a
c


