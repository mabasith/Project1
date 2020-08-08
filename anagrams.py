str1=raw_input('Enter the first string: ')
str2=raw_input('enter the second string: ')
if sorted(str1)==sorted(str2):
	print('These are anagrams')
else:
	print('These are not anagrams')