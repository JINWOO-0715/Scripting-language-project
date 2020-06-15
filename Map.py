import folium
from ReadFile import *
import webbrowser


def Pressed(s,index):
    # 위도 경도 지정
    map_osm = folium.Map(location=[s[index]['XCODE'],s[index]['YCODE']])
    # 마커 지정
    folium.Marker([s[index]['XCODE'],s[index]['YCODE']], popup='찾는위치').add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')
