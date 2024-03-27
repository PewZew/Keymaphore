import textwrap
output=''

def switch(case):
	if case.lower() in ['vc', 'cv']:
		return 'a'
	elif case.lower() in ['vd', 'dv']:
		return 'b'
	elif case.lower() in ['ve', 'ev']: 
		return 'c'
	elif case.lower() in ['vr', 'rv']:
		return 'd'
	elif case.lower() in ['vt', 'tv']:
		return 'e'
	elif case.lower() in ['vg', 'gv']:
		return 'f'
	elif case.lower() in ['vb', 'bv']:
		return 'g'
	elif case.lower() in ['cd', 'dc']:
		return 'h'
	elif case.lower() in ['ce', 'ec']:
		return 'i'
	elif case.lower() in ['rg', 'gr']:
		return 'j'
	elif case.lower() in ['cr', 'rc']:
		return 'k'
	elif case.lower() in ['ct', 'tc']:
		return 'l'
	elif case.lower() in ['cg', 'gc']:
		return 'm'
	elif case.lower() in ['cb', 'bc']:
		return 'n'
	elif case.lower() in ['de', 'ed']:
		return 'o'
	elif case.lower() in ['dr', 'rd']:
		return 'p'
	elif case.lower() in ['dt', 'td']:
		return 'q'
	elif case.lower() in ['dg', 'gd']:
		return 'r'
	elif case.lower() in ['db', 'bd']:
		return 's'
	elif case.lower() in ['er', 're']:
		return 't'
	elif case.lower() in ['et', 'te']:
		return 'u'
	elif case.lower() in ['rb', 'br']:
		return 'v'
	elif case.lower() in ['tg', 'gt']:
		return 'w'
	elif case.lower() in ['tb', 'bt']:
		return 'x'
	elif case.lower() in ['eg', 'ge']:
		return 'y'
	elif case.lower() in ['gb', 'bg']:
		return 'z'
	else:
		return '#'

while True:
	output=''
	code=input("Nhập mã vào: ")
	group=textwrap.wrap(code, 2)

	for i in range(len(group)):
		output=output+(switch(group[i]))
	print(output)