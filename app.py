import matplotlib.pyplot as plt


x1 = [2, 4, 5, 3, 4]
y1 = [2, 3, 6, 5, 3]


plt.plot(x1, y1, label='Line 1')


x2 = [1,3,5,7]
y2 = [2,4,6,8]

plt.plot(x2, y2, label='Line 2')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph- Two lines')
plt.legend()
plt.show()