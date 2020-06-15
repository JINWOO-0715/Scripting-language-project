import folium
from ReadFile import *

s =Seoul().crawl_movie()

print(s[0]['XCODE'],s[0]['YCODE'])

map_som = folium.Map(location=[s[0]['XCODE'],s[0]['YCODE']])

