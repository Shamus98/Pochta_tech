import matplotlib.pyplot as plt
import numpy as np
import statistics
data = [[0.004,0.04735958493795467,529.5],[0.04735958493795467,0.10552489594273934,281.875],[0.10552489594273934,0.17641574960127587,202.5],
        [0.17641574960127587,0.24522598039215687,124.625],[0.24522598039215687,0.3011911764705883,70.25],[0.3011911764705883,0.35326638655462195,38.375],
        [0.35326638655462195,0.40772857142857144,36.625],[0.40772857142857144,0.46690389610389604,48],[0.46690389610389604,0.5329610389610389,51.75],
        [0.5329610389610389,0.6017064935064935,37.25],[0.6017064935064935,0.6692886363636363,34.125],[0.6692886363636363,0.7417416666666666,37.875],
        [0.7417416666666666,0.824698245614035,32.25],[0.824698245614035,0.8985428692699491,36.125],[0.8985428692699491,0.9622474972191324,31.625],
        [0.9622474972191324,1.0228905547226388,28.5],[1.0228905547226388,1.0858876811594205,23.875],[1.0858876811594205,1.1487500000000002,22.375],
        [1.1487500000000002,1.2158229166666665,16],[1.2158229166666665,1.2983229166666665,29.25],[1.2983229166666665,1.3915530303030303,29.25],
        [1.3915530303030303,1.4815530303030302,21.75],[1.4815530303030302,1.561,13.25],[1.561,1.6254487179487178,12.125],[1.6254487179487178,1.6859278846153845,12.25],
        [1.6859278846153845,1.7458958333333334,9.125],[1.7458958333333334,1.7984166666666668,10.375],[1.7984166666666668,1.8593333333333333,4.125],
        [1.8593333333333333,1.9195000000000002,3.375],[1.9195000000000002,1.9877142857142858,6.625],[1.9877142857142858,2.0930267857142857,12.25],
        [2.0930267857142857,2.1917291666666667,9.25],[2.1917291666666667,2.263916666666667,10.625],[2.263916666666667,2.3801666666666668,5.625],
        [2.3801666666666668,2.493,3.25],[2.493,2.5646666666666667,3],[2.5646666666666667,2.6395476190476193,3.5],[2.6395476190476193,2.7037142857142857,5.75],
        [2.7037142857142857,2.75875,1.875],[2.75875,2.818178571428571,2.5],[2.818178571428571,2.8785535714285713,6],[2.8785535714285713,2.936125,4],
        [2.936125,3.007375,1.75],[3.007375,3.094125,3.375],[3.094125,3.1695,2.25],[3.1695,3.284416666666667,2.125],[3.284416666666667,3.4024666666666668,3.125],
        [3.4024666666666668,3.4721333333333337,4.5],[3.4721333333333337,3.5708333333333333,3.125],[3.5708333333333333,3.666,2],
        [3.666,3.7413333333333334,1.375],[3.7413333333333334,3.8128333333333333,2.5],[3.8128333333333333,3.879,1.625],[3.879,3.959,3.25],[3.959,4.0335,1.5],[4.0335,4.1055,1.875],
        [4.1055,4.1945,1.875],[4.1945,4.2844999999999995,1.125],[4.2844999999999995,4.432,1.25],[4.432,4.574333333333334,2.75],[4.574333333333334,4.636833333333334,2.75],[4.636833333333334,4.6905,1.25],
        [4.6905,4.78975,1.375],[4.78975,4.984500000000001,3.375],[4.984500000000001,5.14325,2.25],[5.14325,5.3155,2],[5.3155,5.525,1.875],[5.525,5.662,1.25],[5.662,5.7795000000000005,1.75],[5.7795000000000005,5.865,1.25],
        [5.865,5.964,1.75],[5.964,6.1115,1.125],[6.1115,6.27,1],[6.27,6.555,1],[6.555,6.859999999999999,1],[6.859999999999999,7.047499999999999,1],[7.047499999999999,7.195,1],[7.195,7.3175,1],[7.3175,7.46,1],[7.46,7.67,1],
        [7.67,7.858750000000001,1.125],[7.858750000000001,7.9675,1.875],[7.9675,8.065000000000001,2],[8.065000000000001,8.25375,1.875],[8.25375,8.434000000000001,1.125],[8.434000000000001,8.5365,1],[8.5365,8.66875,1.125],
        [8.66875,9.283750000000001,1.75],[9.283750000000001,9.870000000000001,1.125],[9.870000000000001,10.0225,1],[10.0225,10.29,1],[10.29,10.685,1],[10.685,11.037500000000001,1],[11.037500000000001,11.545,1],[11.545,12.719999999999999,1],
        [12.719999999999999,13.54875,1.125],[13.54875,14.15225,1.75],[14.15225,17.3385,1.125],[17.3385,21.485,1],[21.485,23,1]]

x = [item[0] for item in data]
y = [item[2] for item in data]
width = [item[1] - item[0] for item in data]
turbo_cm = plt.cm.get_cmap('turbo')
colors = [turbo_cm(v) for v in np.linspace(0,1,len(x))]
# Создание фигуры и осей
fig, ax = plt.subplots(figsize=(12, 6))

# Построение гистограммы с переменной шириной столбцов
ax.bar(x, y, width=width, edgecolor=colors)

# Форматирование осей
ax.set_xlabel('Диапазон значений, кг')
ax.set_ylabel('Величина')
ax.set_title('Гистограмма с переменной шириной столбцов')
plt.savefig('/Users/z/Desktop/Логистика датасет склад Хельвас/hist_width.eps', format='eps')
plt.savefig('/Users/z/Desktop/Логистика датасет склад Хельвас/hist_width.png', format='png')
# Отображение графика
plt.show()
