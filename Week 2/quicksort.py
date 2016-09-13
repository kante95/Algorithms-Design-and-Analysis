comparison1 = 0
comparison2 = 0
comparison3 = 0

def partition1(a,l,r):
	p = a[l]
	k = l+1
	for j in range(l+1,r):
		if a[j]<p:
			a[j],a[k]= a[k],a[j]
			k+=1
	a[l],a[k-1] = a[k-1],a[l]
	return k-1


def partition2(a,l,r):
	p = a[r-1]
	a[l],a[r-1] = a[r-1],a[l]
	k = l+1
	for j in range(l+1,r):
		if a[j]<p:
			a[j],a[k]= a[k],a[j]
			k+=1
	a[l],a[k-1] = a[k-1],a[l]
	return k-1

def partition3(a,l,r):
	p = sorted([a[l],a[r-1],a[int((l+r-1)/2)]])[1]
	if p == a[l]:
		pos = l
	elif p==a[r-1]:
		pos = r-1
	else:
		pos = int((l+r-1)/2)
	a[l],a[pos] = a[pos],a[l]
	k = l+1

	for j in range(l+1,r):
		if a[j]<p:
			a[j],a[k]= a[k],a[j]
			k+=1
	a[l],a[k-1] = a[k-1],a[l]
	return k-1

def quickSort1(array,i,n):
	global comparison1
	if i<n:
		comparison1 += n-i-1
		split = partition1(array,i,n)
		quickSort1(array,i,split)
		quickSort1(array,split+1,n)

def quickSort2(array,i,n):
	global comparison2
	if i<n:
		comparison2 += n-i-1
		split = partition2(array,i,n)
		quickSort2(array,i,split)
		quickSort2(array,split+1,n)

def quickSort3(array,i,n):
	global comparison3
	if i<n:
		comparison3 += n-i-1
		split = partition3(array,i,n)
		quickSort3(array,i,split)
		quickSort3(array,split+1,n)


fname = "QuickSort.txt"
array = [int(line.rstrip('\n')) for line in open(fname)]
quickSort1(array,0,len(array))
array = [int(line.rstrip('\n')) for line in open(fname)]
quickSort2(array,0,len(array))
array = [int(line.rstrip('\n')) for line in open(fname)]
quickSort3(array,0,len(array))
print(comparison1,comparison2,comparison3)
