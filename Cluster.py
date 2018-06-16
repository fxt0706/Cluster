import matplotlib.pyplot as plt
import numpy as np

num_point = 200
distance_array = [[0] * num_point] * num_point

np.random.seed(20180001)
data = np.random.rand(2, num_point)
data[0] = data[0] * 10
data[1] = data[1] * 10
for i in range(0,2):
    for j in range(0, num_point):
        data[i][j] = round(data[i][j],1)

fig, axs = plt.subplots(1, 1, figsize=(10, 10))
axs.scatter(data[0], data[1])



def cal_distance(self_x, self_y, to_x, to_y):
    distance = (to_x - self_x) ** 2 + (to_y - self_y) ** 2
    return  distance

def move():
    for i in range(0, num_point):
        for j in range(0, num_point):
            distance_array[i][j] = cal_distance(data[0][i], data[1][i], data[0][j], data[1][j])
        distance_array[i][i] = 10000

        closest = distance_array[i].index(min(distance_array[i]))
        print('closest: ' + str(closest))

        if data[0][closest] > data[0][i] and data[0][i] < 10:
            data[0][i] = data[0][i] + 0.1
        elif data[0][closest] < data[0][i] and data[0][i] > 0:
            data[0][i] = data[0][i] - 0.1

        if data[1][closest] > data[1][i] and data[1][i] < 10:
            data[1][i] = data[1][i] + 0.1
        elif data[1][closest] < data[1][i] and data[1][i] > 0:
            data[1][i] = data[1][i] - 0.1

for i in range(0,5000):
    plt.cla()
    move()
    axs.scatter(data[0], data[1])
    plt.pause(0.0001)
