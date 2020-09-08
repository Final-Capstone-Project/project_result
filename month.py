import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

file_path = '서울시 화재발생 현황 (월별) 통계.csv'
df = pd.read_csv(file_path)

df['발생합계'] = pd.to_numeric(df['발생합계'], errors='coerce')

print(df.info())
df = df.set_index(['월별'])
df = df['발생합계']
df = df.groupby('월별').sum()
df = df.drop('계')

df = df.sort_index(ascending= True)

print(df)



plt.style.use('ggplot')
df.plot(kind="bar")
plt.xticks(rotation = 45)
plt.ylabel('발생 건수')
plt.title('서울시 월별 화재발생 현황 (2017 ~ 2019)')
plt.show()

