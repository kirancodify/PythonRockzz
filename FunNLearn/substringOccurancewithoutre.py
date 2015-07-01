# Find occurance of substring in a string without using re package
s = 'azcbobobegghakl'
substr = 'bob'

pos = 0
indices = []
while True:
    i = s.find(substr,pos)
    if i==-1:
        break
    indices.append(i)
    pos = i+1
    #print indices

print("Number of times bob occurs is: " + str(len(indices)))