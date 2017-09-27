
seed = "https://en.wikipedia.org/wiki/Tropical_cyclone" 
url = "https://en.wikipedia.org/wiki/Tropical_cyclone#MaximumIntensity"

url_array = url.split("/")
for component in url_array:
	print(component)