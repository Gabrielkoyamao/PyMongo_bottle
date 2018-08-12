fruta = ["apple", "orange", "banana", "kiwi", "morango"]

def analyze_list(l):
	cont = {}

	for item in l:
		if (item in cont):
			cont[item] = cont[item] + 1
		
		else:
			cont[item] = 1
		

	return cont



conts = analyze_list(fruta)

print(conts)
