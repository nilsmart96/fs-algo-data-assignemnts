test = [3, 6, 4, 7, 9, 1, 2]

rounded_half = round(len(test) / 2)

#print(rounded_half)


def merge_sort(list_):
    if len(list_) > 1:
        start = len(list_) // 2
        list_1 = list_[:start]
        list_2 = list_[start:]
        print(list_1)
        print(list_2)
    
        merge_sort(list_1)
        merge_sort(list_2)
        #for i in range(len(list_)):
            #if i < (round(start / 2)):
            #merge_sort(list_1)
            #merge_sort(list_2)
            #i += 1

#def merge_sort(list_):
 #   if len(list_) <= 1:
  #      return list_
   # 
    #left_list = []
    #right_list = []
    #length_list = len(list_)

    #for i in range(0,round(length_list / 2)):
     #   left_list.append(list_[i])
      #  merge_sort(left_list)
       # print(left_list)
    #for i in range(round(length_list / 2), length_list):
     #   right_list.append(list_[i])
      #  merge_sort(right_list)
       # print(right_list)

    

merge_sort(test)

print(test)

# Correct Version:

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1