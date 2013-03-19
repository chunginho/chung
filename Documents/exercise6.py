def reverse_Check(strn):
	l = len(strn)
	index = 0
	str1 = strn[::-1]


	if str1 == strn:
		return 1
	else:
		return 0


strn = raw_input('input string : ')
check = reverse_Check(strn)

if check :
	print 'same'
else:
	print 'different'