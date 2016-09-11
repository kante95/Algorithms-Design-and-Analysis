def countSplit(a,b):
    i = 0
    j = 0
    split = 0
    result = []
    while(i<len(a) or j<len(b)):
        if(i==len(a)):
        	result.append(b[j])
        	j+=1
        elif(j==len(b)):
        	result.append(a[i])
        	i+=1
        else:
            if(a[i]<b[j]):
                result.append(a[i])
                i+=1
            else:
                split+=len(a)-i 
                result.append(b[j])
                j+=1
    return [split,result]


def Count(array,n):
	if n==1:
		return 0,array
	A = array[:int(n/2)]
	B = array[int(n/2):]

	leftInversion,sort1 = Count(A,len(A))
	rightInversion,sort2 = Count(B,len(B))
	splitInversion,sort = countSplit(sort1,sort2)
	return [leftInversion + rightInversion + splitInversion,sort]


fname = "IntegerArray.txt"
array = [int(line.rstrip('\n')) for line in open(fname)]
result,sorted = Count(array,len(array)) 
print(result)


