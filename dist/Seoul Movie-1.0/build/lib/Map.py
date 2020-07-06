import folium
from ReadFile import *
import webbrowser


def Pressed(x,y):
    map_osm = folium.Map(location=[x,y] ,  zoom_start=40)
    # 마커 지정
    folium.Marker([x,y], popup='찾는위치').add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')
