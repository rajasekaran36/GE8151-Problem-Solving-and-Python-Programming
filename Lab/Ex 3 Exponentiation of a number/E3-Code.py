x = int(input("Enter any number"))
final_result = 0
for i in range(0,101):
    power = i
    fact = power
    pow_result = 1
    fact_result = 1

    while(power !=0):
        pow_result = pow_result * x
        power = power - 1
    while (fact != 0):
        fact_result = fact_result * fact
        fact = fact - 1
    term_result = pow_result/fact_result

    final_result = final_result + term_result
	
print("e power:",x,"value is", final_result)