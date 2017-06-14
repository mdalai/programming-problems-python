def anagram(str1,str2):
	all_ch1 = [0]*26
	all_ch2 = [0]*26

	for p in str1:
		pos = ord(p) - ord('a')
		all_ch1[pos] = all_ch1[pos] + 1

	for p in str2:
		pos = ord(p) - ord('a')
		all_ch2[pos] = all_ch2[pos] + 1

	for i in range(len(all_ch1)):
		if all_ch1[i] != all_ch2[i]:
			return False
	return True


	#print [item for item in all_ch1 if item in all_ch2]
	#print [item for item in all_ch2 if item not in all_ch1]
	#any(map(lambda v: v in list2, list1))

print anagram('apple','pleap')
print anagram('apple','pleapf')
print anagram('abcdefghijkkkkabbbbbccccccccc','aaacccdddaaaffffccccdd')