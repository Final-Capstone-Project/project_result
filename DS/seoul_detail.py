import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

#한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

file_path = './서울시 화재발생 세부.csv'
df = pd.read_csv(file_path, encoding='euc-kr')
df.drop(['시도'], axis=1, inplace=True)

df['화재발생년월일'] = pd.to_datetime(df['화재발생년월일'])
df['발생시간대'] = df['화재발생년월일'].dt.hour
df['count'] = 1

#df.sort_values(by='인명피해(명)소계', ascending = False, inplace = True)
df.sort_values(by='재산피해소계', ascending = False, inplace = True)
df_damage_top5 = df.head(6)


#print(df_damage_top5)
df_damage_detail = pd.DataFrame()
df_damage_detail['화재발생시간'] = df_damage_top5['화재발생년월일']
df_damage_detail['발생지역'] = df_damage_top5['시·군·구'] + ' ' + df_damage_top5['읍면동'] + ' ' + df_damage_top5['장소소분류']
df_damage_detail['발화 열원'] = df_damage_top5['발화열원대분류']
df_damage_detail['발화요인'] = df_damage_top5['발화요인대분류']
df_damage_detail['인명피해'] = df_damage_top5['인명피해(명)소계']
df_damage_detail['재산피해'] = df_damage_top5['재산피해소계']


df_damage_detail.set_index("발생지역", inplace=True)
df_damage_detail.drop(['중구 신당동 전통시장'], inplace=True)
plt.style.use('ggplot')
df_damage_detail['재산피해'].plot(kind='bar', color = 'r', alpha=0.8, figsize=(7,5))
plt.title('서울시 재산피해 화재 Top 5 (2019, 제일평화시장 제외)\n', size = 20)
plt.xlabel('\n발생 지역')
plt.ylabel('재산 피해')
plt.xticks(rotation = 0)
plt.show()




"""
df_place = df
df_place['세부 지역명'] = df_place['시·군·구'] + ' ' + df_place['읍면동']
df_place = df_place.groupby('세부 지역명').sum()

del df_place['발생시간대']
df_place.loc['서울시 동별 평균'] = [df_place['인명피해(명)소계'].mean(), df_place['사망'].mean(), df_place['부상'].mean(),
                      df_place['재산피해소계'].mean(), df_place['count'].mean()]

df_place.sort_values(by='count', ascending = False, inplace = True)
#df_place.sort_values(by='인명피해(명)소계', ascending = False, inplace = True)

df_place_top10 = df_place.head(10)
df_place_top10.loc['서울시 동별 평균'] = df_place.loc['서울시 동별 평균']
"""

#서울시 동별 인명피해 Top 10
"""
df_place_top10.rename(index = {'영등포구 영등포동3가':'영등포구 영등포동'}, inplace=True)
plt.style.use('ggplot')
df_place_top10['인명피해(명)소계'].plot(kind='bar', color=['r','r','r','r','r','r','r','r','r','r','b'], alpha=0.8,figsize=(7,5))
plt.title('서울시 동별 인명피해 Top 10 \n', size = 20)
plt.xlabel('\n지역명')
plt.ylabel('인명 피해')
plt.xticks(rotation = 0)
plt.show()
"""

"""
#동별 화재 발생 건수 top 10
plt.style.use('ggplot')
df_place_top10['count'].plot(kind='bar', color=['r','r','r','r','r','r','r','r','r','r','b'], alpha=0.8,figsize=(7,5))
plt.title('서울시 동별 화재 발생 건수 Top 10 \n', size = 20)
plt.xlabel('\n지역명')
plt.ylabel('발생 건수')
plt.xticks(rotation = 0)
plt.show()
"""

"""
#발생 시간대 발생 건수
hour = df.groupby('발생시간대').sum()

plt.style.use('ggplot')
hour['count'].plot(kind='bar', figsize=(7,5))
plt.title('서울시 시간대별 화재건수 (2019)\n', size = 20)
plt.xlabel('발생 시간대')
plt.ylabel('발생 건수')
plt.xticks(rotation = 0)
plt.show()


#발생 시간대 인명피해
plt.style.use('ggplot')
hour['인명피해(명)소계'].plot(kind='bar', figsize=(7,5))
plt.title('서울시 시간대별 인명피해 (2019)\n', size = 20)
plt.xlabel('발생 시간대')
plt.ylabel('인명피해')
plt.xticks(rotation = 0)
plt.show()

#발생 시간대 사망자
plt.style.use('ggplot')
hour['사망'].plot(kind='bar', figsize=(7,5))
plt.title('서울시 시간대별 사망자 수 (2019)\n', size = 20)
plt.xlabel('발생 시간대')
plt.ylabel('사망자 수')
plt.xticks(rotation = 0)
plt.show()

#발생시간대 부상자
plt.style.use('ggplot')
hour['부상'].plot(kind='bar', figsize=(7,5))
plt.title('서울시 시간대별 부상자 수 (2019)\n', size = 20)
plt.xlabel('발생 시간대')
plt.ylabel('부상자 수')
plt.xticks(rotation = 0)
plt.show()
"""