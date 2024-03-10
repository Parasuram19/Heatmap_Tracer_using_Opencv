import folium
import pandas as pd 
import random 
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
from geopy.distance import geodesic 
from folium.plugins import HeatMap
mapobj = folium.Map(location=[12.960135498820074, 80.05737150584049],zoom_start=10)
 
data=[
    [12.960135498820075, 80.0573715058405],
    [13.876544567890345, 81.9876543234567],
    [13.876234567893456, 82.7654321987654],
    [14.876234567896543, 82.7654321234565],
    [15.960135498820075, 83.0573715058405],
    [16.960135498820075, 84.0573715058405],
    [17.960135498820075, 85.0573715058405],
    [18.960135498820075, 86.0573715058405],
    [19.960135498820075, 87.0573715058405],
    [20.960135498820075, 88.0573715058405],
    [21.960135498820075, 89.0573715058405],
] 
# l=[]
# for i in range(0,10):
#     l.append(list(random.uniform(12.960135498820074, 20)))
#     data.append(l) 
print(data)

HeatMap(data).add_to(mapobj) 

mapobj.save("output.html")