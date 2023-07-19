# Palidrome words checker from a list of words

fl_lst = ['radar', 'civic', 'tool', 'madam', 'rocket', 'spice', 'essence',
             'cycle', 'peep', 'thesis', 'scientific', 'tennis', 'noon', 'waves',
             'cosmos', 'philosophy', 'fitness', 'technology', 'topography',
             'level', 'quantum', 'racecar', 'photon', 'deified', 'photon',
             'scooter', 'bikes', 'royal', 'train', 'eye', 'light',
             'did', 'cats', 'piano', 'guitar', 'deed', 'eve',
             'music', 'frequency', 'wavelength', 'biology', 'microscope',
             'telescope', 'electron', 'rope', 'tea', 'coco', 'a']

palin_lst = []
non_palin_lst = []

# print('number of elements in list: ', len(fl_lst))
# print('number of elements in palin list: ', len(non_palin_lst))
# print(type(non_palin_lst))

# Function to check the palindrome words
def check_palin():
    i, palin_nos, non_palin = 0, 0, 0
    # Loop trhough the list to check the number of words of palidrom form
    while i < len(fl_lst):
     
        cur_str = fl_lst[i]
        # print('current string is : ', cur_str)
        rev_str = cur_str[::-1]
        # print('Reverse of current string is : ', rev_str)
        if cur_str == rev_str and len(cur_str) > 1:
            palin_nos += 1
            palin_lst.append(fl_lst[i])                   
        else:
            non_palin += 1
            non_palin_lst.append(fl_lst[i])
        i += 1
    # Return the number of palindrome and non palidrome words from the function
    return palin_nos, non_palin

# Calling the function to check the plaidrome and non palidrome words in the phrase
pln, non_pln = check_palin()
# Display the number of occurences og palindrome and non palindrome words
print ('The number of palindrome words in the list is : ', pln)
print ('The number of non palindrome words in the list is : ', non_pln)

# Display the list of plaidrome and non palidrome words 
print('palin list : ', palin_lst) 
print('Non palin list : ', non_palin_lst) 