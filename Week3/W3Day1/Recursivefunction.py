def rec_fibbo_fact():
    
    def rec_factorial(num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * rec_factorial(num - 1)
        
        
    def rec_fibbo(terms):
        if terms == 1 or terms == 2:
            return 1
        else:
            return rec_fibbo(terms-1) + rec_fibbo(terms-2)
        
    num = int(input("Enter number: "))
    print("Factorial of",num,"is",rec_factorial(num))
    print(f"Fibbo's {num}th term is: {rec_fibbo(num)}")
    

    
def normal_fibbo_fact():
    

    def normal_fibbo(rangeFibbo):
        terms = [1,1]
        if rangeFibbo == 1:
            return 1
        if rangeFibbo == 2:
            return [1,1]
        a = 1
        b = 1
        
        for i in range (3 , rangeFibbo +1):
            next_term = a+b
            terms.append(next_term)
            a = b
            b = next_term        
            
        return terms

    terms = int ( input("Enter the number of terms: ") )
    print("Normal Fibbo :",normal_fibbo(terms))

    def normal_fact():
        fact = 1
        num = int(input("Enter number: "))
        for i in range(1,num+1):
            fact = fact*i
        return fact

    print("Normal Factorial:",normal_fact())
    
print("Normal Fibbo and Factorial")
normal_fibbo_fact()

print()
print("Recursive Fibbo and Factorial")
rec_fibbo_fact()
# rec_factorial(num)
# rec_fibbo(num)