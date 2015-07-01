balance = 2548
annualInterestRate = 0.18
monthlyInterestRate = (annualInterestRate)/12.0
Payment=0
tmpBalance = balance
while(tmpBalance>0):
    tmpBalance = balance
    Payment = Payment +10
    for a in range(0,12):
        tmpBalance=tmpBalance-Payment 
        tmpBalance=tmpBalance+(monthlyInterestRate*tmpBalance)
print "Lowest Payment: "+str(Payment)