import textwrap
output=''

def switch(case):
	if case.lower()=='vc' or case.lower()=='cv' or case.lower()=='21' or case.lower()=='12':
		return 'a'
	elif case.lower()=='vd' or case.lower()=='dv' or case.lower()=='24' or case.lower()=='42':
		return 'b'
	elif case.lower()=='ve' or case.lower()=='ev' or case.lower()=='27' or case.lower()=='72': 
		return 'c'
	elif case.lower()=='vr' or case.lower()=='rv' or case.lower()=='28' or case.lower()=='82':
		return 'd'
	elif case.lower()=='vt' or case.lower()=='tv' or case.lower()=='29' or case.lower()=='92':
		return 'e'
	elif case.lower()=='vg' or case.lower()=='gv' or case.lower()=='26' or case.lower()=='62':
		return 'f'
	elif case.lower()=='vb' or case.lower()=='bv' or case.lower()=='23' or case.lower()=='32':
		return 'g'
	elif case.lower()=='cd' or case.lower()=='dc' or case.lower()=='14' or case.lower()=='41':
		return 'h'
	elif case.lower()=='ce' or case.lower()=='ec' or case.lower()=='17' or case.lower()=='71':
		return 'i'
	elif case.lower()=='rg' or case.lower()=='gr' or case.lower()=='86' or case.lower()=='68':
		return 'j'
	elif case.lower()=='cr' or case.lower()=='rc' or case.lower()=='18' or case.lower()=='81':
		return 'k'
	elif case.lower()=='ct' or case.lower()=='tc' or case.lower()=='19' or case.lower()=='91':
		return 'l'
	elif case.lower()=='cg' or case.lower()=='gc' or case.lower()=='16' or case.lower()=='61':
		return 'm'
	elif case.lower()=='cb' or case.lower()=='bc' or case.lower()=='13' or case.lower()=='31':
		return 'n'
	elif case.lower()=='de' or case.lower()=='ed' or case.lower()=='47' or case.lower()=='74':
		return 'o'
	elif case.lower()=='dr' or case.lower()=='rd' or case.lower()=='48' or case.lower()=='84':
		return 'p'
	elif case.lower()=='dt' or case.lower()=='td' or case.lower()=='49' or case.lower()=='94':
		return 'q'
	elif case.lower()=='dg' or case.lower()=='gd' or case.lower()=='46' or case.lower()=='64':
		return 'r'
	elif case.lower()=='db' or case.lower()=='bd' or case.lower()=='43' or case.lower()=='34':
		return 's'
	elif case.lower()=='er' or case.lower()=='re' or case.lower()=='78' or case.lower()=='87':
		return 't'
	elif case.lower()=='et' or case.lower()=='te' or case.lower()=='79' or case.lower()=='97':
		return 'u'
	elif case.lower()=='rb' or case.lower()=='br' or case.lower()=='83' or case.lower()=='38':
		return 'v'
	elif case.lower()=='tg' or case.lower()=='gt' or case.lower()=='96' or case.lower()=='69':
		return 'w'
	elif case.lower()=='tb' or case.lower()=='bt' or case.lower()=='93' or case.lower()=='39':
		return 'x'
	elif case.lower()=='eg' or case.lower()=='ge' or case.lower()=='76' or case.lower()=='67':
		return 'y'
	elif case.lower()=='gb' or case.lower()=='bg' or case.lower()=='63' or case.lower()=='36':
		return 'z'
	

code=input("Nhập mã vào: ")
group=textwrap.wrap(code, 2)
for i in range(len(group)):
	output=output+(switch(group[i]))
print(output)