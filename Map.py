import folium
from ReadFile import *
import webbrowser


def Pressed(x,y):
    # 위도 경도 지정
    x = float(s['좌표정보(X)'].iloc[index])
    y =float(s['좌표정보(Y)'].iloc[index])

    map_osm = folium.Map(location=[x,y])
    # 마커 지정
    folium.Marker([x,y], popup='찾는위치').add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')
