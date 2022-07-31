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

def insertionSort(arr):  	
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
	return arr	

    
arr = Kiwi_weight_data()


insertionSort(arr)
for i in range(len(arr)):
	print (arr[i], end=" ")


