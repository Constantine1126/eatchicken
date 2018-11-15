def every_other_new (list1):
    '''
    Return a new list consisting of every other element of the list starting from the first

    >>> every_other_new (['potatoe',10,9,'cat'])
    ['potatoe',9]
    '''
    return list [::2]



def every_other_modify (list1):
    '''
    Modify the list so that every other element starting with the first, is removed

    >>>list1 [1,2,3,4,5]
    >>>every_other_modify (list1)
    [2,4]
    '''
    # we want the items in list1 to be removed
    for item in list1[::2]:
        list1.remove (item)


def sum_of_even (list1):
    '''
    Return the sum of all the even numbers in list_of_numbers

    >>>sum_of_even([1,2,3,4])
    6
    '''
    r=0 # we want to sum into a number, not a string
    for i in list1:
        if i%2==0:
            r=r+i
    return r


def collect_strings (list1):
    '''
    Return a new list consisting of all the strings in the list

    >>>list1['1','2','3','4']['5','6']
    >>>collect_strings(list1)
    ['1','2','3','4','5','6']
    '''
    r=""
    for item in list1:
        r=r+str(item) # convert item into a string
    return r


def count_int (list1):
    '''
    Return the total number of integers in the list

    >>>count_int(['skrrr',1,4,'skrrrrrrrr'])
    5
    '''
    ## check your example for correctness
    num=0
    for i in list1:
        if type(i)==int:
            num=num+1
    return num


def remove_strings_modify (list1):
    '''
    Modify the list so that it does not contain any strings

    >>>list1['skrrr',7]
    >>>remove_strings_modify(list1)
    [7]
    '''
    #i="" we don't need a new string
    for i in list1 [:]:
        if type(i)==str:
            list1.remove(i) # good!


def mystery_10(list_of_number)->list:
    '''
    Return the number is greater than limit and add to list

    >>>limit[5]
    >>>mystery_10([1,2,6,7])
    >>>[1,2,6,7,6,7]
    '''
    L=[] # we can't have a number as a variable
    for e in list_of_number:
        if e>limit:
            L.append(e)
    return L
#good!
        
