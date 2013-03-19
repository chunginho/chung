def num_char(strn):
	num = 0
	for index in strn:
		if index == 'e':
			num += 1

	return num


num = num_char("next people")
print 'e is',num