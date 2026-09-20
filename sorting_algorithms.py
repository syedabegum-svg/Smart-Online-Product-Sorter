# ---------------- MERGE SORT ----------------

def merge_sort(products, key, reverse=False):

    # Base case
    if len(products) <= 1:
        return products

    # Find middle
    mid = len(products) // 2

    # Divide the list
    left = merge_sort(products[:mid], key, reverse)
    right = merge_sort(products[mid:], key, reverse)

    # Merge the two halves
    return merge(left, right, key, reverse)


def merge(left, right, key, reverse):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if reverse:
            condition = left[i][key] >= right[j][key]
        else:
            condition = left[i][key] <= right[j][key]

        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result