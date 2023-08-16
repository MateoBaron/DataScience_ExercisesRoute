'''
These exercises are the page w3resource and can find in the next link:
https://www.w3resource.com/python-exercises/sets/
'''
def exercises_1():
    # 1. Write a Python program to create a set. 
       
    print("\033[1m"+"A. Create a set of countries"+ "\033[0m")
    set_countries = {'CO','AE','IT','PE','UK','US'} #Set about countries 
    print ("Type of set_countries: "+ str(type(set_countries)))
    print (set_countries)
    
    print ("\033[1m"+"\nB.Another forms to create a set"+"\033[0m")
    print ("Empty set:")
    emp_set = set()
    print ("Type of emp_set: "+ str(type(emp_set)))
    print (emp_set)

    print ("\nCreate a non empty set:")
    non_empSet = set([2,4,6,8])
    print ("Type of non_empSet: "+ str(type(non_empSet)))
    print (non_empSet)



  
def exercises_2():
    # 2. Write a search Python program to iterate over sets.
    
    #Create three sets: Odd numbers, soccer teams and string. 
    num_set = set ([1,3,5,7,9,11,13]) 
    soccTeam_set = {"ath", "fcb", "bay", "bam", "psg", "liv"} 
    char_set = set("TheOffice")

    # For loops to iterate
    print("Elements of the set of odd numbers")
    for num in num_set:
        print(num, end=' ')
    
    print("\n\nElements of the set of soccer teams")
    for team in soccTeam_set:
        print(team, end=' ')

    print("\n\nElements of the set of string")
    for char_elmt in char_set:
        print(char_elmt, end=' ')



def exercises_3():
    # 3. Write a Python program to add member(s) to a set.

    #  We created a empty set
    empty_set = set()
    print ("Initial set\n", empty_set)
    print ('\n')
    # Prompt the user how many terms he wants to add to he set
    amount_set = int(input("Enter the set size: "))
    

    #For loop to add the terms to the set
    for term in range (amount_set) :
        element_set= input("Enter a element for the set: ")
        empty_set.add(element_set)

    print("\nFinally set\n", empty_set)

    



def exercises_4():
    #4. Write a Python program to remove item(s) from a given set.

    #Create a set
    animals_set = set(["lion","dog", "cat", "mouse", "bird", "fish" ])
    print ("Initial set:\n", animals_set)
    print ("Initial Size set: " + str(len(animals_set)))

    #We ask the user to choose the term to delete
    delete_terms = int(input("Enter the numbers of items to remove: "))
    for term in range (delete_terms):        
        animals_set.pop()
    
    print("The final set is: \n", animals_set)
    print ("Final size of the set: " + str(len(animals_set)))
    




def exercises_5():
    #5. Write a Python program to remove an item from a set if it is present in the set.

    '''Note:The discard() method removes 
    the specified item from the set. 
    This method is different from the 
    remove() method, because the remove() 
    method will raise an error if 
    the specified item does not exist, 
    and the discard() method will not.'''

    #Create a set
    Set_primeNumbers = set([2,3,5,7,11,13,17,19,23])
    print("\033[1m"+"Initial Set Prime Numbers"+ "\033[0m")
    print(Set_primeNumbers)

    # We ask the user to choose the term to delete
    term2Remove = int(input("Enter a prime number to remove form the Set PrimeNumbers: "))
    Set_primeNumbers.discard(term2Remove)
    
    print("\033[1m"+"Final Set Prime Numbers"+ "\033[0m")
    print(Set_primeNumbers)



def exercises_6():
    #6. Write a Python program to create an intersection of sets.

    #Created two sets
    set1 = {1,2,3,4,5,6,7,8,9}
    set2 = {0,2,4,6,8}

    print ("Set1:\n",set1)
    print ("Set2:\n",set2)

    #Intersection
    set3=set1.intersection(set2)
    print("\nIntersection Between Set1 and Set2")
    print(set3)
    print(set1 & set2)


def exercises_7():
    #7. Write a Python program to create a union of sets.
    
    #Created two sets
    set1 = {1,2,3,4,5,6,7,8,9}
    set2 = {11,31,51}
    print ("Set1:\n",set1)
    print ("Set2:\n",set2)

    #Union
    set3 = set1.union(set2)
    print("\nIntersection Between Set1 and Set2")
    print(set3)
    print(set1 | set2)



def exercises_8():
    #8. Write a Python program to create set difference.
    
    #Created two sets
    set1 = {1,2,3,4,5,6,7}
    set2 = {11,31,51,4,7}
    print ("Set1:\n",set1)
    print ("Set2:\n",set2)

    #Difference
    set3 = set1.difference(set2)
    print("\nDifference Between Set1 and Set2")
    print(set3)
    print(set1-set2)



def exercises_9():
    #9. Write a Python program to create a symmetric difference.

    #Created two sets
    set1 = {1,2,3,4,5,6,7}
    set2 = {11,31,51,4,7}
    print ("Set1:\n",set1)
    print ("Set2:\n",set2)

    #Symmetric Difference   
    set3 = set1.symmetric_difference(set2)
    print("\nDifference Between Set1 and Set2")
    print(set3)
    print(set1^ set2)




def exercises_10():    
    #10. Write a search Python program to check if a set is a subset of another set.
    set1={0,1,2,3,4,5,6,7,8,9,10,11,12}
    set2={0,2,4,6,8,10}
    set3={20,30,40,50,60}

    print ("Set1: ",set1)
    print ("Set2: ",set2)
    print ("Set3: ",set3)


    # First form
    counter_set1 =0
    counter_set3 =0
    for term in set2:
        if term in set1:
            counter_set1 +=1
        
        if term in set3:
            counter_set3 +=1
        

    if counter_set1 == len(set2):
        print("\033[1m"+"First Form"+ "\033[0m")
        print("The set2 is a subset of the set1")    
    else:
        print("\033[1m"+"First Form"+ "\033[0m")
        print("The set2 is not a subset of the set1")

    if counter_set3 == len(set2):       
        print("The set2 is a subset of the set3")    
    else:        
        print("The set2 is not a subset of the set3")

    

    #Second form
    set4=set2.intersection(set1)
    set5=set2.intersection(set3)
    #print (set3)
    if set2 == set4:
        print("\033[1m"+"Second Form"+ "\033[0m")
        print("The set2 is a subset of the set1")    
    else:
        print("\033[1m"+"Second Form"+ "\033[0m")
        print("The set2 is not a subset of the set1")

    if set2 == set5:       
        print("The set2 is a subset of the set3")    
    else:        
        print("The set2 is not a subset of the set3")

    
    #Third form
    print("\033[1m"+"Third Form"+ "\033[0m")
    print("Is the set2 a subset of the set1?")    
    print(set2.issubset(set1))
    print("Is the set2 a subset of the set3?")   
    print(set2.issubset(set3))




def exercises_11():
    #11. Write a search Python program to create a shallow copy of sets.
    #Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
    animals_set = set(["lion","dog", "cat", "mouse", "bird", "fish" ])
    
    copy_set = animals_set.copy()

    print ("Original_set: ", animals_set)
    print ("Copy_set: ", animals_set)



def exercises_12():
    #12. Write a Python program to remove all elements from a given set.
    soccTeam_set = {"ath", "fcb", "bay", "bam", "psg", "liv"} 
    print ("Set of soccer teams, formerly: \n ", soccTeam_set)
    print ("Set of soccer teams, after removing the elements: \n ", soccTeam_set.clear())


def exercises_13():
    # 13. Write a Python program that uses frozensets.
    #Note: Frozensets behave just like sets except they are immutable.

    set1 = frozenset([1,2,3,4,5])
    
    print('The frozen set is:', set1)
    # random dictionary
    person = {"name": "John", "age": 23, "sex": "male"}

    fSet = frozenset(person)
    print('The frozen set is:', fSet)


def exercises_14():    
    #14. Write a Python program to find the maximum and minimum values in a set.
    set1 = set([4,8,2,7,58,41,14,80,90])

    print("The set is: ", set1)
    print("The maximum number from the set is: ", max(set1))
    print("The minimumnumber from the set is: ", min(set1))


def exercises_15():    
    #15. Write a search Python program to find the length of a set.
    soccTeam_set = {"ath", "fcb", "bay", "bam", "psg", "liv"} 
    
    print("The set is: ", soccTeam_set)
    print("The length from the set is: ", len(soccTeam_set))



def exercises_16():
    #16. Write a Python program to check if a given value is present in a set or not.
    Char_set=set("ONEPIECE")
    print("It's the set: ", Char_set)
    let2in = input("Enter a letter to find out if it's in the set: ")
    print ("Is the letter entered in the set? \n"+ let2in + ":", let2in in Char_set)
    

def exercises_17():
    #17. Write a search Python program to check if two given sets have no elements in common.
    
    
    animals_set = set(["lion","dog", "cat", "mouse", "bird", "fish" ])
    soccTeam_set = {"ath", "fcb", "bay", "bam", "psg", "liv"} 
    pets = {"fish", "dog", "bird",  }

    #The idea the code is comparing three sets
    print("\033[1m"+"Do these sets have elements in common? \n"+ "\033[0m")
    print("animals_set : ",animals_set)
    print("soccTeam_set : ",soccTeam_set)
    print("pets :",pets)
    print("\n")

    print ("animal_set VS soccTeam_set: ", animals_set.isdisjoint(soccTeam_set))
    print ("animal_set VS pets: ",animals_set.isdisjoint(pets))



def exercises_18(): 
    #18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
    set1={0,1,2,3,4,5,6,7,8,9,10,11,12}
    set2={0,2,4,6,8,10}

    print("Is set1 a super set of set2?: ", set1.issuperset(set2))


def exercises_19():    
    #19. Write a Python program to find elements in a given set that are not in another set.
    set1={0,1,2,3,4,5,6,7,8,9,10,11,12}
    set2={0,2,4,6,8,10}

    # The Difference can we helping to find elemnts that are not in another set. 
    print("Set1:\n", set1)
    print("Set2:\n", set2)

    print("\033[1m"+"These elements are not in another set"+ "\033[0m")
    print("Difference between set1-set2")
    print (set1-set2)
    print("Difference between set2-set1")
    print (set2-set1)

    

    

'''
def exercises_20():    
    #20. Write a Python program to remove the intersection of a second set with a first set.

def exercises_21():
    #21. Write a search Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

def exercises_22():
    #22. Write a search Python program that finds all pairs of elements in a list whose sum is equal to a given value.

def exercises_23():
    #23. Write a Python program to find the longest common prefix of all strings. Use the Python set.

def exercises_24():
    #24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

def exercises_25():
    #25. Given two sets of numbers, write a search Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

def exercises_26():
    #26. Write a Python program to find all the anagrams and group them together from a given list of strings. Use the search Python data type.

def exercises_27():
    #27. Write a Python program to find all the anagrams in a given list of strings and then group them together. Use the Python data type.

def exercises_28():
    #28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

def exercises_29():
    #29. Write a search Python program to find the third largest number from a given list of numbers.Use the Python set data type.


def exercises_30():
    #30. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the search Python set data type.

'''
exercises_19()
