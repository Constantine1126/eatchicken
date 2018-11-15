def largest(list_of_numbers):
    '''
    Return the largest number in list_of_numbers

    >>>largest([1,2,3,4])
    4
    '''
    ## we want i to be a number
    i = a[0]  # the first number in the list could be the largest
    #i=""
    ## we already have a variable called i, so lets use a new one, also the length of the list
    for ind in range(0, len(list_of_numbers)):
    #for i in range (0,list_of_numbers):
        ##  i is a number, so we can't compare it to a list
        if list_of_numbers[ind] > i:  # if the next number is larger than the largest number so far
            i = list_of_numbers[ind]  # remember the larger number
        #if i > list_of_numbers and i==i
    return i


def remove_duplicates(list1): # we should use the same variable names as in the description (old_list)
    '''
    Return a copy of old_list which has no dulicate element

    >>>remove_duplicates([1,2,2,3])
    [1,2,3]
    '''
    ## we want a new list
    new = []
    #i=""
    for item in list1:
        ## if we don't already have a copy of item in our new list
        ## add it to the new list
        if item not in new:
            new.append(item)
        #if i==item:
            #item.remove(list1)
    return new


def common_elemnt (list1,list2):
    '''
    return true if and only if list1 and list2 have at least one element in common

    >>>common_element([1,2,3],[1,4,5])
    True
    '''
    ## we can't do a for loop over two lists!
    for i in list1:
        if i in list2:
            return True
    #for i in list1 and list2:
       #if list1[i]==list2[i]
    #return True
    return False


def list_to_string(list_of_numbers):
    '''
    Return a string consisting of each element of list_of_number

    >>>list_to_string([1,2,3,4])
    ['1','2','3','4']
    '''
    ## want a new string
    s = ""
    for item in list_of_numbers:
        ## convert the item to a string, and add it to our previous string
        s = s + str(item)
        #type(item)==str(item)
    return s


def extend_a_list(list1,list2):
    '''
    Add all of the element of list2 to the end of list1

    >>>extend_a_list([1,2,3],[4,5,6])
    [1,2,3,4,5,6]
    '''
    #new_list[] we don't need a new list
    for i in list2:# and list1:
        # add the items to list1
        list1.append(i)
        #new_list.append[i]


def all_squares(max_number):
    '''
    Return a list of all the squares of numbers from 0 to max_number

    >>>all_squares(26)
    [0,1,2,3,4,5]
    '''
    new_list=[]
    for j in range(0,max_number):
        if j**2<=max_number:
            new_list.append(j**2)
    # good, just return the list
    return new_list


def items_in_common(list1,list2):
    '''
    Return a list consisting of all the element that list1 and list2 have in common

    >>>items_in_common([1,2,3],[1,4,5])
    [1]
    '''
    ## give new list a value
    new_list = []
    #new_list[]
    for i in list1:# and list2:
        if i in list2:
            new_list.append(i)
    return new_list


def mystery_12(list_of_numbers,upper_limit):
    '''
    Return True if and only if the numbers in the list is lesser than the limit

    >>>mystery_12([1,2,3],5)
    True
    '''
    b=True
    for e in list_of_numbers:
        if e > upper_limit:
            b=False
    return b
## Good work!
        
    
