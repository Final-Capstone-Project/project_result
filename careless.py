import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

file_path = '서울시 부주의에 의한 화재발생(소방서별) 통계.csv'

df = pd.read_csv(file_path)
df = df.set_index(['소방서'])

print(df.info())

df['가연물 근접방치'] = pd.to_numeric(df['가연물 근접방치'], errors='coerce')
df['불장난'] = pd.to_numeric(df['불장난'], errors='coerce')
df['용접 절단 연마'] = pd.to_numeric(df['용접 절단 연마'], errors='coerce')

df_year = df.groupby('기간').sum()
df_year = df_year.sum()

print(df_year)

plt.style.use('ggplot')
df_year.plot(kind='pie', figsize=(7,5), autopct='%1.1f%%')
plt.title('서울시 부주의 화재발생 유형 (2017 ~ 2019)', size = 20)
plt.axis('equal')
plt.legend(labels=df_year.index, loc = 'upper right')
plt.show()

