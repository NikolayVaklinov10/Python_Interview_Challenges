def selection_sort(arr):

    # For every slot in array
    for fill_slot in range(len(arr)-1, 0,-1):
        position_of_max = 0

        # For every set of 0 to fill_slot+1
        for location in range(1, fill_slot+1):
            # Set maximum's location
            if arr[location] > arr[position_of_max]:
                position_of_max = location

        temp = arr[fill_slot]
        arr[fill_slot] = arr[position_of_max]
        arr[position_of_max] = temp


arr = [3, 5, 2, 7, 6, 8, 12, 40, 21]
selection_sort(arr)
print(arr)


