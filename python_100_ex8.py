
def sort_list(words):
    words = sorted(words)
    print (words)
    print (",".join(words))

def sort_dic(words):
    word_dic = {}
    for word in words:
        word_dic[word] = 0
    print(word_dic)
    
    word_sort = sorted(word_dic)
    
    print(word_sort)

    print (",".join(word_sort))

words = input("Enter your words").split(",")
print (words)
sort_list(words)
sort_dic(words)



