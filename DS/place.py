import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 적용
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

file_path = '서울시 장소별 화재발생 (구별) 통계.csv'

df = pd.read_csv(file_path)
df = df.set_index(['자치구'])

print(df)

df['기타주택'] = pd.to_numeric(df['기타주택'], errors='coerce')
df['학교'] = pd.to_numeric(df['학교'], errors='coerce')
df['판매시설'] = pd.to_numeric(df['판매시설'], errors='coerce')
df['숙박시설'] = pd.to_numeric(df['숙박시설'], errors='coerce')
df['종교시설'] = pd.to_numeric(df['종교시설'], errors='coerce')
df['의료시설'] = pd.to_numeric(df['의료시설'], errors='coerce')
df['공장 및 창고'] = pd.to_numeric(df['공장 및 창고'], errors='coerce')
df['작업장'] = pd.to_numeric(df['작업장'], errors='coerce')
df['위락오락시설'] = pd.to_numeric(df['위락오락시설'], errors='coerce')
df['위험물(가스 제조소 등)'] = pd.to_numeric(df['위험물(가스 제조소 등)'], errors='coerce')
df['임야'] = pd.to_numeric(df['임야'], errors='coerce')

df_year = df.groupby('기간').sum()
df_year = df_year.sum()

df_year['기타'] = df_year['학교'] + df_year['숙박시설'] + df_year['종교시설'] + df_year['의료시설'] + df_year['위험물(가스 제조소 등)'] + \
                df_year['임야'] + df_year['작업장'] + df_year['위락오락시설']

df_year.drop(['학교', '숙박시설', '종교시설', '의료시설', '위험물(가스 제조소 등)', '임야', '작업장', '위락오락시설'], inplace=True)

print(df_year)

plt.style.use('ggplot')
df_year.plot(kind='pie', figsize=(7, 5), autopct='%1.1f%%')
plt.title('서울시 장소별 화재발생 유형 (2017 ~ 2019)', size=20)
plt.axis('equal')
plt.legend(labels=df_year.index, loc='upper right')
plt.show()
