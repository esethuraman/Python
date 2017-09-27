import re


seed = "https://en.wikipedia.org/wiki/Tropical_cyclone" 
url = "https://en.wikipedia.org/wiki/Tropical_cyclonea#MaximumIntensity"
seed = seed + '#'
print(seed)
pattern = re.compile(seed+"*")
is_matched = pattern.match(url)

def fun():
	flag = True
	if(is_matched == None):
		print("not a duplicate return false")
		flag = False
	return flag


print("FUNCTION CALL" ,fun())

#print("IS DUPLICATE :", flag)
print(is_matched)