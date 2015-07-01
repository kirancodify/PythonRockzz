balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
monthlyInterestRate = (annualInterestRate)/12.0
unpaidBalance = balance
totalPaid = 0
for month in range (0, 12):
    print "Month: " + str(month+1)
    minimumPayment = unpaidBalance*monthlyPaymentRate
    print "Minimum monthly payment: " + str("{0:.2f}".format(minimumPayment))
    unpaidBalance = unpaidBalance - minimumPayment
    interest = monthlyInterestRate * unpaidBalance
    unpaidBalance = unpaidBalance + interest
    print "Remaining balance: " + str("{0:.2f}".format(unpaidBalance))
    totalPaid = totalPaid+minimumPayment
    #print unpaidBalance
    #print interest
    #print minimumPayment

print "Total paid: " + str("{0:.2f}".format(totalPaid))
print "Remaining balance: " + str("{0:.2f}".format(unpaidBalance))