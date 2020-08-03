import re
f=open("file_path")
r=f.read()
r.replace("\n", "")
q=open("file_path")
p=q.read()
p=list(p.replace("\n",""))
b_float = list(map(float,p))
print(b_float)
s=(re.findall(r"compound:(.+?),",r))
str1 = ','.join(s)
print(str1)
a_float = []
for num1 in s:
    a_float.append(float(num1))
len(a_float)
def mean(x):
  return sum(x) / len(x)
mean_a = mean(a_float)
mean_b = mean(b_float)
print('a组数据期望： ', mean_a)
print('b组数据期望： ', mean_b)
# 计算每一项数据与均值的差
def de_mean(x):
  x_bar = mean(x)
  return [x_i - x_bar for x_i in x]
# 辅助计算函数 dot product 、sum_of_squares
def dot(v, w):
  return sum(v_i * w_i for v_i, w_i in zip(v, w))
def sum_of_squares(v):
  return dot(v, v)
# 方差
def variance(x):
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)
# 标准差
import math
def standard_deviation(x):
  return math.sqrt(variance(x))

var_a = variance(a_float)
var_b = variance(b_float)
print('a组数据的方差： ', var_a)
print('b组数据的方差： ', var_b)
std_a = standard_deviation(a_float)
std_b = standard_deviation(b_float)
print('a组数据的标准差： ', std_a)
print('b组数据的标准差： ', std_b)
# 协方差
def covariance(x, y):
  n = len(x)
  return dot(de_mean(x), de_mean(y)) / (n -1)
# 相关系数
def correlation(x, y):
  stdev_x = standard_deviation(x)
  stdev_y = standard_deviation(y)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(x, y) / stdev_x / stdev_y
  else:
    return 0

cov_a_b = covariance(a_float, b_float)
corr_a_b = correlation(a_float, b_float)
print('ab的协方差： ', cov_a_b)
print('ab的相关系数： ', corr_a_b)
