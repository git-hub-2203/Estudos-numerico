import numpy as np
import matplotlib.pyplot as plt

'''
#array de valores 
x = np.arange(2, 11, 0.1)

#função
y = 2*x - 1

plt.plot(x, y) #Define o domínio e a lei da função

plt.show()


x = np.arange(-2, 3)
y = x**2 

plt.plot(x, y)

plt.show()


x = np.array([1, 2, 6, 10, 14])
y = np.array([1, 3, 8, 6, 12])

plt.plot(x, y, '*', color='red')


A = np.array([[1, -5, 2], [2, 2, 2], [2, -1, 1]])
print(*A)

#plt.show()


x = np.linspace(1, 4, 4) -> criação de array com 4 elementos igualmente espaçados
print(x)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = filter (lambda x : x % 2 == 0, a)

print(list(f))


x = list(map(int, input('Elementos de x: ').strip().split()))
y = list(map(int, input('Elementos de y: ').strip().split()))

plt.plot(x, y, '*')
plt.show()



x = list(map(int, input('Elementos de x: ').strip().split()))

print(x)


t = np.arange(0, 4.01, 0.01)
y = np.exp(-t) * (np.cos(10*t) + np.sin(10*t))

plt.plot(t, y, color='orange', linewidth=2.0)
plt.title('Gráfico de sistema massa-mola')
plt.xlabel('Tempo decorrido (t)')
plt.ylabel('Altura da Mola (y)')
plt.grid()
plt.show()
'''

#GRÁFICOS EM 3 DIMENSÕES
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

f = lambda x, y : np.sin(x) + np.cos(y)

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.plot_wireframe(X, Y, Z, color='orange')
ax.set_title('Gráfico de f(x, y)')

plt.show()