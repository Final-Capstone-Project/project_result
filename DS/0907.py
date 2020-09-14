import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

file_path = './서울시 화재발생 현황 (구별) 통계.csv'
df = pd.read_csv(file_path)

df = df.set_index(['자치구'])

# object -> float 형변환
df['발생 방화'] = pd.to_numeric(df['발생 방화'], errors='coerce')
# 기간별 data frame

df_10 = df
df_10 = df_10[['기간', '부동산 피해액', '동산 피해액']]
df_10 = df_10.sort_values(by='동산 피해액', ascending=False)
df_10 = df_10.head(10)
print(df_10)

df_2017 = df[df['기간'].isin(['2017'])]
df_2018 = df[df['기간'].isin(['2018'])]
df_2019 = df[df['기간'].isin(['2019'])]

df_2019 = df_2019.head(5)
df_2019 = df_2019[['기간', '부동산 피해액', '동산 피해액']]
df_2019 = df_2019.sort_values(by='동산 피해액', ascending=False)

# 피애액 기준 요약

df_place = df.groupby('자치구').sum()
df_place = df_place[['기간', '부동산 피해액', '동산 피해액']]
df_place = df_place.sort_values(by='동산 피해액', ascending=False)
print(df_place)

plt.style.use('ggplot')
df_place.plot(kind="bar", stacked=True, color=['orange', 'red', 'skyblue'])
plt.xticks(rotation=45)
plt.ylabel('피해액')
plt.title('서울시 화재발생 피해액 현황 (2017 ~ 2019)')
plt.show()

# 기간별 기준 요약
"""
df_year = df.groupby('기간').sum()
df_year = df_year[['발생 실화','발생 방화', '발생 기타']]

plt.style.use('ggplot')
df_year.plot(kind="barh", figsize = (10, 5), width=0.5,stacked = True)
plt.xticks(rotation = 45)

plt.title('서울시 연도별 화재발생 현황')
plt.ylabel('연도')
plt.xlabel('발생 건수')
plt.show()
df_year['총 발생 화재'] = df_year['발생 실화'] + df_year['발생 방화'] + df_year['발생 기타']
print(df_year)
"""

# 자치구 기준 요약
"""
print(df.info())
df_place = df.groupby('자치구').sum()

df_place = df_place.sort_values(by = '발생합계', ascending= False)
df_place = df_place[['발생 실화', '발생 방화', '발생 기타']]

plt.style.use('ggplot')
df_place.plot(kind="bar",stacked = True, color = ['orange', 'red', 'skyblue'])
plt.xticks(rotation = 45)
plt.ylabel('발생 건수')
plt.title('서울시 화재발생 현황 (2017 ~ 2019)')
plt.show()
df_place['총 발생 화재'] = df_place['발생 실화'] + df_place['발생 방화'] + df_place['발생 기타']
"""
