import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

file_path = '서울시 원인별 화재발생 (구별) 통계.csv'
df = pd.read_csv(file_path)
df = df.set_index(['자치구'])

df['화학적 요인'] = pd.to_numeric(df['화학적 요인'], errors='coerce')
df['가스누출(폭발)'] = pd.to_numeric(df['가스누출(폭발)'], errors='coerce')
df['교통사고'] = pd.to_numeric(df['교통사고'], errors='coerce')
df['자연적인 요인'] = pd.to_numeric(df['자연적인 요인'], errors='coerce')
df['기타'] = pd.to_numeric(df['기타'], errors='coerce')
df['방화명확'] = pd.to_numeric(df['방화명확'], errors='coerce')
df['방화의심'] = pd.to_numeric(df['방화의심'], errors='coerce')


print(df.info())


df_why = df.sum()
df_why['기타'] = df_why['기타'] + df_why['화학적 요인'] + df_why['가스누출(폭발)'] + df_why['교통사고'] + df_why['자연적인 요인'] + df_why['방화의심']
df_why.drop(['기간','화학적 요인', '가스누출(폭발)', '교통사고', '자연적인 요인', '방화의심'], inplace = True)

print(df_why)

plt.style.use('ggplot')
df_why.plot(kind='pie', figsize=(10,5), autopct='%1.1f%%')
plt.title('서울시 원인별 화재발생 (2019)', size = 15)
plt.axis('equal')
plt.legend(labels=df_why.index, loc = 'upper right')
plt.show()
