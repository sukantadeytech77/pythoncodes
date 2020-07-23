from collections import Counter, OrderedDict
import collections

# Generate Prime Numbers
def fill_prime_number(num):
    primeNums = []

    for x in range(2,num):
        if  ( is_prime(x) == True ):    
            primeNums.append(x)
            
    return primeNums

# Check if specified number is a prime or not.
def is_prime(num):
    isprime = True
    if ( num > 1 ):
        for i in range(2,num):
            if ( num != i and (num % i) == 0 ):
                isprime = False
                break

    return isprime

# Get the prime factors
def get_factors(number,primes ):
    primefactors = []
    numval = number
    counter = 0
    while ( counter <= numval ):
        for num in primes:
            if ( number % num == 0 ):
                number = number/num
                primefactors.append(num)
        counter+=1
        
    return primefactors

# Calculate HCF by Prime Factors Method
def calculate_hcf_by_prime_factor(numbers,primes):
    hcfFactors = []
    combinedFactors = []
   
    for num in numbers:
        factors = get_factors(num,primes)
        print("The prime factorization of %d are %s" %(num,factors))
        hcfFactors.append(factors)
        combinedFactors = combinedFactors + factors
    
    # common element extraction form N lists 
    # using map() + intersection() 
    commonFactors = list(set.intersection(*map(set, hcfFactors)))

    if ( commonFactors.count == 1 ):
        # Most occurences
        maxoccurenceNum = max(set(combinedFactors), key = combinedFactors.count)
        commonFactors.append(maxoccurenceNum)
        
    print ("The most common factors are : " + str(commonFactors))
    
    # Now calculating HCFs
    hcf = 1
    for num in commonFactors:
        hcf = hcf * num

    return hcf

# Grouping factors by the number of occurences
def group_list(lst): 
      
    res =  [(el, lst.count(el)) for el in lst] 
    return list(OrderedDict(res).items())

# Get factor based on highest number of occurences in the list
def get_factor_by_num_of_occurence(lcmGrpFactors):
    lcmFinalFactors = []
    print(lcmGrpFactors)
    
    for factor in lcmGrpFactors:
        if ( len(lcmFinalFactors) == 0 ):
             lcmFinalFactors.append(factor)
        else:
            found = False
            for item in lcmFinalFactors:
                if ( item[0] == factor[0] ):
                    found = True
                    if ( item[1] < factor[1] ):
                        lcmFinalFactors.remove(item)
                        found = False

            if ( found == False ):
                lcmFinalFactors.append(factor)

    # Remove duplicates
    return list(dict.fromkeys(lcmFinalFactors))

# Calculate LCM by Prime Factors Method
def calculate_lcm_by_prime_factor(numbers,primes):
    
    lcmFactors = []
    lcmGrpFactors = []

    for num in numbers:
        factors = get_factors(num,primes)
        print("The prime factorization of %d are %s" %(num,factors))
        lcmGrpFactors = lcmGrpFactors + group_list(factors)
                   
        lcmFactors.append(factors)

    lcmFinalFactors = get_factor_by_num_of_occurence(lcmGrpFactors)

    print(lcmFinalFactors)
    
    lcm = 1
    for factor in lcmFinalFactors:
        lcmValue = factor[0] ** factor[1]
        lcm = lcm * lcmValue
       
    return lcm

# Calculate LCM by Division Method
def calculate_lcm_by_division_method(numbers,primes):

    origNumbers = numbers
    divisionTable = []
    ansFactors = []
    primeFact = 0

    while ( numbers.count(1) == 0 ):
        for primeNum in primes:
            divFound = False
            divisionTable = []
            for number in numbers:
                calcNum = 1
                if ( number % primeNum == 0 ):
                    calcNum = int(number/primeNum)
                    primeFact = primeNum
                    divFound = True
                else:
                    calcNum = number

                divisionTable.append(calcNum)
                                
            if ( divFound == True ):
                ansFactors.append(primeFact)
                print("%d | %s " % (primeFact,numbers))
                numbers = divisionTable
                print("-------------------------------------------------------")
                break
            
        
    print("  | %s \n\n" %numbers)

    # Remove duplicates
    numbers = list(dict.fromkeys(numbers))
    
    lcm = 1
    finalFactors = ansFactors + numbers

    for factor in (finalFactors):
        lcm = lcm * factor

    return lcm

# Verify Ansewer numbers (Only applicable for two numbers )

def verify_ans_for_hcf_and_lcm(numbers,hcfans,lcmans):

    res= 1
    for num in numbers:
        res = res * num

    print("\n\nThe product of %s are %d" %(numbers,res))

    product = hcfans * lcmans
    print("\n\nThe product of HCF (%d)  and LCM (%d) are %d" %(hcfans,lcmans,product))

    if ( product == res ):
        return True
    else:
        return False

