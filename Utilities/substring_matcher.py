
seed = "https://en.wikipedia.org/wiki/Tropical_cyclone" 
url = "https://en.wikipedia.org/wiki/Tropical_cyclone#MaximumIntensity"

seed = seed + '#'
length  = len(seed)
print(url[:length])
if(seed == url[:length]):
	print("duplicate")
else:
	print("exclusive")