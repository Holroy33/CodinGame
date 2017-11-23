import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
v_lon = float(lon.replace(",","."))
v_lat = float(lat.replace(",","."))
v_lon_rad = ((v_lon * math.pi)/180)
v_lat_rad = ((v_lat * math.pi)/180)
defib_dict={}
prev_d=9999999999
last_id=0
for i in range(n):
    defib = input()
    id=defib.split(";")[0]
    defib_dict[id]=defib.split(";")[1]
    d_lon=float(defib.split(";")[4].replace(",","."))
    d_lon_rad=math.radians(d_lon)
    d_lat=float(defib.split(";")[5].replace(",","."))
    d_lat_rad=math.radians(d_lat)
    x = math.fabs(v_lon_rad - d_lon_rad) * math.cos((v_lat_rad + d_lat_rad) / 2)
    y = math.fabs(v_lat_rad - d_lat_rad)
    d = math.hypot(x, y) * 6371
    if d < prev_d :
        prev_d=d
        last_id=id
print(defib_dict[last_id])
