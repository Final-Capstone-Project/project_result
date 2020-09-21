import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

file_path = '서울시 주택종류별 화재발생현황 통계.csv'

df = pd.read_csv(file_path)

df['사망'] = pd.to_numeric(df['사망'], errors='coerce')
df['부상'] = pd.to_numeric(df['부상'], errors='coerce')
df['재산피해'] = pd.to_numeric(df['재산피해'], errors='coerce')

df = df.set_index(['구분'])

#df = df['화재건수']
#df = df['사망']
df = df['부상']

df = df.groupby('구분').sum()
print(df)

plt.style.use('ggplot')
df.plot(kind="bar")
plt.xticks(rotation = 45)
plt.ylabel('부상 건수')
plt.title('서울시 주택종류별 화재발생현황 (2017 ~ 2019)')
plt.show()

# 서울시 화재 오인 출동 현황
"""
file_path = '서울시 화재 오인출동현황 통계.csv'
df = pd.read_csv(file_path)
df = df.set_index(['소방서'])

df['연막소득'] = pd.to_numeric(df['연막소득'], errors='coerce')
df['방화기도'] = pd.to_numeric(df['방화기도'], errors='coerce')
df['경보오동작'] = pd.to_numeric(df['경보오동작'], errors='coerce')

print(df.info())

df_miss = df.sum()
print(df_miss)
df_miss.drop(['기간'], inplace = True)

#df_miss = df_miss.sort_index(ascending= True)

plt.style.use('ggplot')
df_miss.plot(kind='pie', figsize=(15,8), autopct='%1.1f%%')
plt.title('서울시 화재 오인출동현황 (2017~2019)', size = 10)
plt.axis('equal')
plt.legend(labels=df_miss.index, loc = 'upper right')
plt.show()
"""