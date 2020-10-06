import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc
import pandas_profiling

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
hour = df.groupby('발생시간대').sum()
#hour = hour.sort_values(by='count', ascending=False)
print(hour)


#발생 시간대 발생 건수
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
