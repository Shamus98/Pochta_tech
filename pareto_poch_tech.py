#1) получить парето-распределение для SKU  pareto-SKU.eps (некоторые встречаются часто - некоторые редко)  
#2) нарисовать распределение паллет по количеству коробок  qty-boxes.eps 
#3) нарисовать распределение количества коробок по параметру Width width-boxes.eps
# listic_SKU1.append(col.strip('"'))
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from scipy.ndimage.filters import gaussian_filter1d
from functools import cmp_to_key
import numpy as np

SKU_Quantity = dict()

df = pd.read_csv(f'/Users/z/Desktop/Логистика датасет склад Хельвас/PochtaTech/cnt_bar_code_by_index_border_oper.csv',sep='[\s,\t]+', engine='python')
print(df['"num_cnt"'])
df = df.reset_index()


values = list(df['"num_cnt"'])
total_sum = sum(values)
cumulative_percentages = [100 * (value / total_sum) for value in values]
cumulative_sums = [sum(cumulative_percentages[:i+1]) for i in range(len(cumulative_percentages))]

color = 'blue'
line_size = 1

fig, ax = plt.subplots()
plt.rc("axes", axisbelow=True)
plt.grid()
ax.plot(list(df['index']), list(cumulative_sums), color=color, linewidth=line_size)
ax.plot(45000, 0)
ax.set_xlim(xmin=0, xmax=max(list(df['index']))+1000)
ax.set_ylim([0, 105])
ax.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis='y')
plt.title("Pareto", size=14, pad=20)
plt.xlabel("N", loc="right", size=12)

plt.savefig('/Users/z/Desktop/Логистика датасет склад Хельвас/pareto_cnt_bar_code_by_index_border_oper.eps', format='eps')
plt.savefig('/Users/z/Desktop/Логистика датасет склад Хельвас/pareto_cnt_bar_code_by_index_border_oper.png', format='png')

plt.show()

