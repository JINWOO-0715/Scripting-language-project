%matplotlib inline
import pandas as pd  # 데이터를 저장하고 처리하는 패키지
import matplotlib as mpl  # 그래프를 그리는 패키지
import matplotlib.pyplot as plt  # 그래프를 그리는 패키지


df = pd.read_csv('weather.csv', index_col='point')

df  # df 표시
