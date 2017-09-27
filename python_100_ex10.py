def remove_same():
	word = input("Enter the word: ").split()
	word_remove = []
	for i in word :
		if i not in word_remove:
			word_remove.append(i)

	print (" ".join(list_sort(word_remove)))

def list_sort(words):
	word_sort = sorted(words)
	return word_sort
remove_same()