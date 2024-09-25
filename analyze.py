# 라이브러리 불러오기
import folium
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/content/drive/어린이보호구역_사고다발_찐.csv')
df.head(5)

df=df[df["소재지도로명주소"].notnull() & df["소재지도로명주소"].str.contains("대구광역시")]

# Map 함수를 이용해 지도를 focusing 합니다.
map=folium.Map(location=[35.869, 128.606], zoom_start=14)
map

# 반복문으로 마킹하기
for i in df.index:
    name = df.loc[i, '대상시설명']
    lat = df.loc[i, '위도']
    lon = df.loc[i, '경도']
    marker = folium.Marker([lat, lon], tooltip=name)
    marker.add_to(map)
map

#반복문으로 시설유형명, 위도, 경도 추출하기
#조건문(if)으로 시설크기 class별로 색깔을 지정하여 marker에 표시
for i in df.index:
  name = df.loc[i, '대상시설명']
  lat = df.loc[i, '위도']
  lon = df.loc[i, '경도']
  if df['시설종류'][i] == '어린이집':
        code_color = 'orange'
  elif df['시설종류'][i] == '초등학교':
        code_color = 'pink'
  elif df['시설종류'][i] == '유치원':
        code_color = 'green'
  else:
    code_color = 'blue'
  marker = folium.Marker([lat,lon], icon=folium.Icon(color=code_color), tooltip = name).add_to(map)
map

# 원 형태 마커(CircleMarker) 표시
for i in df.index:
    name = df.loc[i, '대상시설명']
    lat = df.loc[i, '위도']
    lon = df.loc[i, '경도']
    marker = folium.CircleMarker([lat, lon], radius = 20, color = 'skyblue',
                                 fill_color = 'skyblue',
                                 popup = name, #팝업창을 크게(popup = folium.Popup(name, max_width=300))
                                 icon = folium.Icon(color='skyblue')).add_to(map)

map

df=pd.read_csv('/content/drive/어린이 사고다발 구역.csv', encoding='cp949')
df.head(5)

# 원 형태 마커(CircleMarker) 표시
for i in df.index:
    name = df.loc[i, '지점명']
    lat = df.loc[i, '위도']
    lon = df.loc[i, '경도']
    marker = folium.CircleMarker([lat, lon], radius = 30, color = 'red',
                                 fill_color = 'red',
                                 popup = name, #팝업창을 크게(popup = folium.Popup(name, max_width=300))
                                 icon = folium.Icon(color='red')).add_to(map)

map