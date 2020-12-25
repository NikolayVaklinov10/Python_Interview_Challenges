def solution(id_list):

    # Initiate unique Id
    unique_id = 0

    # XOR for recovery id in id list
    for i in id_list:
        print("This is the current id begin checked: ", i)
        print("This is the current unique id: ", unique_id)
        print("This is the result of the XOR:", (unique_id^i))

    return unique_id











