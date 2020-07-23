import hcm_lcm_modules as mod

def main():
    primes = mod.fill_prime_number(50)

    hcfNumbers = [18,27]
    hcfNumbers = [18,12]
    hcfNumbers = [20,50,120]

    print ("\n\nHCF Prime Factor Method")
    ans = mod.calculate_hcf_by_prime_factor(hcfNumbers,primes)
    print ("\nThe HCF of %s is %d" %(hcfNumbers,ans))
    
    lcmNumbers = [6,8]
    lcmNumbers = [24,300]
    lcmNumbers = [10,12,15,75]
    lcmNumbers = [330, 75, 450, 225, 180]
    lcmNumbers = [330, 75, 450, 225, 80]

    print ("\n\nLCM Prime Factor Method\n\n")
    ans = mod.calculate_lcm_by_prime_factor(lcmNumbers,primes)
    print ("\nThe LCM of %s is %d " %(lcmNumbers,ans))

    print ("\n\nLCM Prime by Division Method\n\n")
    ans = mod.calculate_lcm_by_division_method(lcmNumbers,primes)
    print ("\nThe LCM of %s is %d" %(lcmNumbers,ans))

    # Now Find HCF and LCM for numbers
    numbers = [20,50]
    print ("\n\nHCF Prime Factor Method")
    hcfans = mod.calculate_hcf_by_prime_factor(numbers,primes)
    print ("\nThe HCF of %s is %d" %(numbers,hcfans))

    print ("\n\nLCM Prime by Division Method\n\n")
    lcmans = mod.calculate_lcm_by_division_method(numbers,primes)
    print ("\nThe LCM of %s is %d" %(numbers,lcmans))

    if ( mod.verify_ans_for_hcf_and_lcm(numbers,hcfans,lcmans) == True ):
        print("\nAnswer are correct")
    else:
        print("Answer are incorrect")


# Execute main function
if __name__== "__main__":
  main()









