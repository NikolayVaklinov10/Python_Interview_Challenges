
def shell_sort(arr):
    sub_list_count = len(arr)/2

    # While we still have sub lists
    while sub_list_count > 0:
        for start in range(sub_list_count):
            # Use a gap insertion
            gap_insertion_sort(arr, start, sub_list_count)

        sub_list_count = sub_list_count / 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):

        current_value = arr[i]
        position = i

        # Using the Gap
        while position >= gap and arr[position-gap] > current_value:
            arr[position] = arr[position-gap]
            position = position-gap

        # Set current value
        arr[position] = current_value


arr = [45, 67, 23, 45, 21, 24, 7, 2, 6, 4,90]
shell_sort(arr)
print(arr)





