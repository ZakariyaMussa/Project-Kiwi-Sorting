def Kiwi_weight_data():
    

    kiwi_data = open("data.csv", "r")
    kiwi_dataread = kiwi_data.read()
    kiwi_dataread_list = kiwi_dataread.split("\n")


    for kiwi_weight in range(0, len(kiwi_dataread_list), 1):
        kiwi_dataread_list[kiwi_weight] = kiwi_dataread_list[kiwi_weight].replace('"', "");
        kiwi_dataread_list[kiwi_weight] = float(kiwi_dataread_list[kiwi_weight]);

    return kiwi_dataread_list
import sys
A = []
for i in range(len(A)):

	
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	A[i], A[min_idx] = A[min_idx], A[i]

	
A = Kiwi_weight_data()
print ("Sorted array :")
for i in range(len(A)):
	print (A[i],end=" ")
