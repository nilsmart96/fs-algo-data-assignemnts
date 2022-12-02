"""
Assignment Quicksort Nils Marthiensen (Python 3.10.4) 2022-10-17

Explanation

Plan:

1) Choose element that all other elements in the input list are compared to (I call this pivot element going forward)
2) Compare the value of each element in the list to the value of the pivot element and put lower values in front and higher 
    values behind the pivot element
3) Call the function again for the elements left of the pivot element and similarly for the elements on the right (recursion).
    -> Repeatedly start at 1) for every sublist that gets created until each sublist is of length 1.
4) Then everything is sorted

Implementation:

1) Choose pivot element (I choose the last element in a given list for this example, consequences of that will be discussed later).

2) Compare the value of each element in the list to the value of the pivot element and restructure accordingly:
    2.1) I start by iterating over the elements in the list starting at the front (left)
    2.2) For each element I check whether it is smaller (or equal) than the pivot element
    2.3) Only if a smaller (or equal) element is found, a second iterator moves one step to the right
        (This one starts "one position in front of the list" (index[-1]), implemented this would be the last element in the list.)
    2.4) Now the current element of the first iterator (2.1) gets swapped with the element at the second iterator (2.3)
    2.5) When the first iterator (2.1) reaches the pivot element, two things happen:
        2.5.1) I move the second iterator to the right similar to (2.3)
        2.5.2) I swap the pivot element with the element where the second iterator is now at, similar to (2.4)
    2.6) Now all values left of the pivot element are smaller and right of the pivot element are bigger than the pivot element

3) Call the function again for the elements left of the pivot element and similarly for the elements on the right (reucursion),
    repeat for every sublist that gets created:
    3.1) I look at the leftest part of the original list that is not sorted (always excluding the pivot element)
    3.2) If the function gets called on just one element I move on as this part of the list is already sorted
    3.3) Repeat the same for the right side (3.1, 3.2)
    3.4) This process finishes when only 1-item-lists are left

4) Now the list is sorted in ascending order.
"""

# Function for quicksort, needs three parameters: 
# 1) the list that is to be sortet (list_)
# 2) the index from where to sort (left)
# 3) the index until where to sort (right)
# In the beginning we want to sort the whole list,
# so left=0 and right=len(list_)-1. But this becomes 
# important when calling the function recursively
# to sort the different sublists.
def quicksort(list_, left, right):
    # If the length of the subarray that is to be sorted is 
    # 1, quicksort does nothing. The follwoing if statement
    # checks if at least two elements are present (3.2).
    if left < right:
        # Retrieve the current position of the pivot element,
        # using the function below (pivot_split).
        pivot_pos = pivot_split(list_, left, right)
        # Call quicksort recursively on all elements left of
        # the pivot element, excluding the latter (3).
        quicksort(list_, left, pivot_pos - 1)
        # Call quicksort recursively on all elements right of
        # pivot element, excluding the latter (3).
        quicksort(list_, pivot_pos + 1, right)
    # No need to include a return for the sorted list, as the 
    # function automatically finishes when the list is sorted.
    # This is because the if-statement is no longer met.

# Second function that returns the current index of the pivot element.
# It is also used to sort the other values around the pivot element.
def pivot_split(list_, left, right):
    # Second iterator from the left (2.3).
    i = left - 1
    # Store loction of the pivot element, here
    # always the last element of the list (1).
    pivot = list_[right]
    # Start iterating over the list from the left (2.1).
    for j in range(left, right):
        # Check for every element if it is smaller (or equal)
        # than the pivot element (2.2).
        if list_[j] <= pivot:
            # Add one to the second iterator if the condition
            # is met (2.3).
            i += 1
            # Swap the elements at the two respective iterator
            # positions (2.4).
            list_[i], list_[j] = list_[j], list_[i]
    # Move the second iterator one position to the right (2.5.1).
    i += 1
    # Swap the pivot element with the element at the current position 
    # of the second iterator (2.5.2).
    list_[i], list_[right] = list_[right], list_[i]
    # The current position of the pivot element gets returned.
    return i

"""
Time Complexity

Explanation

For quicksort the time complexity is heavily dependend on the scenario: 
    Average and Good Case: O(n * log(n))
    Bad Case: O(n²)

What are the average, good and bad case scenarios?
    Average Case: Pivot element is somewhere between the median and the largest/smallest value
    Good Case: Pivot element is the median of the list
    Bad Case: Pivot element is the largest or smallest value in the list

How are the different Big-O notations derived?
    The main thing driving the time complexity is the for-loop in the "pivot_split" function. Two aspects influence the result:
    1) How long does the for-loop take?
    2) How often is it performed?

    1) The for-loop always loops through all elements of the list, no matter the scenario, giving it a time complexity of "n".
        It's n-1 to be exact, the pivot element is excluded. But this really doesn't matter when taking n to infinity.

    2) This is dependent on the scenario (Recall (3.4) above, quicksort finishes when only 1-item-lists are left):
        2.1) Good Case:
            The list (or its sublists) are always split exactly in half after each iteration. Simply put, if the length of the input list is doubled,
            the loop has to run one more time to achieve (3.4). Mathematically this can be described as log base 2 of "n":
            First iteration: 1 * n
            Second iteration: 2 * n/2
            Third iteration: 4 * n/4
            And so fourth -> simplified, n elements are multiplied by log(n) levels, resulting in O(n * log(n))
            (Not achievable on an unsorted list, as we don't know the median)
        2.2) Average Case:
            The average case is complex to model mathematically, but it doesn't change the time complexity of the good case fundamentally.
            The factor n in the front is a little larger, as the list is not always split exactly at the median. Simplified its still O(n * log(n))
            (This is the case that happens when sorting a random list with the algorithm introduced above)
        2.3) Bad Case:
            The input list is split into an empty list and a list of length n-1 after the first iteration. One more element in the input means one 
            more run of the loop to achieve (3.4):
            First iteration: 1 * n
            Second iteration: 1 * n-1
            Third iteration: 1 * n-2 
            And so fourth -> simplified, n elements are multiplied by n levels (of length 1/2n on average), resulting in O(n * 1/2n). Taken to infinity 
            this equals O(n²)
            (This is the case that happens when sorting a already sorted list with the algorithm introduced above)

Can the implementation above be optimized?
    Yes. Moving the pivot element to be always in the middle or at a random location in the list, rather than the back, can improve the performance on a 
    sorted list to the good or average case O(n * log(n)), as we are now able to split axactly at the median (When choosing the middle in a sorted list).
    A random list is not affected by this. I include the version with the middle-element-pivot below ("quicksort_opti"). If one doesn't know if the input
    list is sorted or not, this is definitely the better choice.

Let's have a look if my function is actually producing results that comply with the average, best and bad cases specified above. And if the same goes for
the optimized version.

Note that the implementation above does not work for sorted lists larger than 1000 elements. Longer lists produce a "Maximum Recursion Depth" error. It 
can be avoided by increasing the maximum recursion depth allowed in the script (import sys; sys.setrecursionlimit(some_value)), default is 1000. If 
increased too much, maximum memory of the machine is exceeded. A better solution would be a version of the quicksort function that "memorizes" the values
from one recursion before and starts again with a new "first" recursion. The optimized version below also works (at least until a list-length of something 
like 10^300). When recalling the time complexity this makes sense, as in the case of a sorted list, one recursion is added for each element in the list, 
given the implementation above. For a random list or the optimized implementation, log base 2 of n would still be below 1000 with a list-length of 10^300.
"""

def quicksort_opti(list_, left, right):

    if left < right:
        pivot_pos = pivot_split_opti(list_, left, right)
        quicksort_opti(list_, left, pivot_pos - 1)
        quicksort_opti(list_, pivot_pos + 1, right)

def pivot_split_opti(list_, left, right):
    
    # This line is the only change. Here the current middle 
    # element gets swapped with the right (or last) one, 
    # achieving a split at the median for sorted lists.
    list_[len(list_[left:right]) // 2 + left], list_[right
    ] = list_[right], list_[len(list_[left:right]) // 2 + left]

    i = left - 1
    pivot = list_[right]

    for j in range(left, right):

        if list_[j] <= pivot:
            i += 1
            list_[i], list_[j] = list_[j], list_[i]

    i += 1
    list_[i], list_[right] = list_[right], list_[i]

    return i

# Needed to take the time of the different runs. There are
# more precise options out there, but it is fine for us here.
import time
# Needed to produce lists for the average scenario.
import random
# Needed to visualize the results.
import matplotlib.pyplot as plt

# Specifying how often each list is to be sorted to produce replicable results. 
iterations_input = int(input("Enter over how many iterations you want to average the results: "))

# Function to time how long it takes to sort each list.
def get_time(list_):

    time_begin = time.time()
    # When adding "_opti" to "quicksort", the performance 
    # of the optimized version can be observed.
    quicksort(list_, 0, len(list_) - 1) 
    time_end = time.time()
    total_time = time_end - time_begin

    return total_time

# Specifying the different lengths of lists to test.
# Can be increased when testing the optimized version.
lengths_to_run = [50, 100, 200, 400, 800]

# Creating empty lists to store the intermediate results 
# for further operations. Here a value for each run is 
# appended to the respective list. In order to get the 
# average of the entered iterations these need further 
# processing.
ascending_lists_avg = []
random_lists_avg = []
descending_lists_avg = []

# Creating empty lists to store the final results 
# for analysis and visualization.
ascending_lists_results = []
random_lists_results = []
descending_lists_results = []

# i is used to specify which part of the respective avg 
# list is to be averaged to get the results list.
i = 0

# Testing the different scenarios by first cycling through
# the different lengths of lists, specified above.
for lengths in lengths_to_run:

    # For each length cyling through the number of 
    # iterations specified by the user.
    for iterations in range(0, iterations_input):
    
        # First for a list with ascending values.
        ascending_list = list(range(0, lengths))
        result = get_time(ascending_list)
        ascending_lists_avg.append(result)

        # Then for a list with randomly ordered values. Here the 
        # random library comes into play.
        random_list = list(range(0, lengths))
        random.shuffle(random_list)
        result = get_time(random_list)
        random_lists_avg.append(result)

        # And finally for a list with descending values.
        descending_list = list(range(0, lengths))
        descending_list = descending_list[::-1]
        result = get_time(descending_list)
        descending_lists_avg.append(result)

    # Now the intermediate results have to be processed to get an average for 
    # each length of input list, using the "i" specifyed above.
    ascending_lists_results.append(sum(ascending_lists_avg[i * iterations_input:
    ]) / len(ascending_lists_avg[i * iterations_input:]))

    random_lists_results.append(sum(random_lists_avg[i * iterations_input:
    ]) / len(random_lists_avg[i * iterations_input:]))

    descending_lists_results.append(sum(descending_lists_avg[i * iterations_input:
    ]) / len(descending_lists_avg[i * iterations_input:]))
    
    # Add one to average the values for the second, third etc. length specified in "lenghts_to_run". 
    i += 1

# Plotting the results to see if they match with my description of the time complexity above.
plt.plot(lengths_to_run, ascending_lists_results, label = "Ascending List")
plt.plot(lengths_to_run, random_lists_results, label = "Random List")
plt.plot(lengths_to_run, descending_lists_results, label = "Descending List")
plt.ylabel("seconds")
plt.xlabel("length of the respective lists")
plt.title("time it takes to sort different lists (averaged over " + str(iterations_input) + " iterations)")
plt.legend()
plt.show()

"""
It can be observed that both sorted lists (ascending and descending) have a time complexity close to O(n²), while the random list is closer to O(n * log(n)).
The longer time of the ascending list is likely due to my implementation. The if-statement in the "pivot_split" function is always fulfilled, while it is 
never fulfilled in the descending variant. Either way both are performing pretty badly compared to a random list.

Using the optimized version all three lists perform close to O(n * log(n)).
"""