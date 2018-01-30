
speed_of_light= 299792458.0 # spped of light in meters/second 
billionth = 1.0/1000000000
nanostick= speed_of_light*billionth*100 # calculate how much light travles in nanosecond 
print nanostick
#python code that print out 
# the distance, in meters, that light travles in one processor cycle
cycles_per_second=2700000000.0 # 2.7 GHz 
distance=speed_of_light/cycles_per_second
print distance
