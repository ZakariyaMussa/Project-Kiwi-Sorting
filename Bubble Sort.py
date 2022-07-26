from collections import Counter
#import txt file, read data from it, convert string data into float
def Kiwi_weight_data():


    kiwi_data = open("data.csv", "r")
    kiwi_dataread = kiwi_data.read()
    kiwi_dataread_list = kiwi_dataread.split("\n")


    for kiwi_weight in range(0, len(kiwi_dataread_list), 1):
        kiwi_dataread_list[kiwi_weight] = kiwi_dataread_list[kiwi_weight].replace('"', "");
        kiwi_dataread_list[kiwi_weight] = float(kiwi_dataread_list[kiwi_weight]);

    return kiwi_dataread_list

def bubbleSort(arr):
	n = len(arr)


	for i in range(n):
		swapped = False

	
		for j in range(0, n-i-1):

			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		
		if swapped == False:
			break
		
arr = Kiwi_weight_data()

bubbleSort(arr)

print ("Sorted array :")
for i in range(len(arr)):
	print (arr[i],end=" ")


