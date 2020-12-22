
def calc_overlap(coor1, dim1, coor2, dim2):
    """
    Takes in 2 coordinates and their length in that dimension
    """

    # Find greater of the two coordinates
    # (this is either the point to the most right
    # or the higher point, depending on the dimension)

    # The greater point would be the start of the overlap
    greater = max(coor1, coor2)

    # The lower point is the end of the overlap
    lower = min(coor1+dim1, coor2+dim2)

    # Return a tuple of Nones if there is no overlap

    if greater >= lower:
        return None, None

    # Otherwise, get the overlap length
    overlap = lower-greater

    return greater, overlap


















