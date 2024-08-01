def product(nums):
    length = len(nums)
    if length == 0:
        return []

    forward = [1] * length
    backward = [1] * length
    result = [1] * length

    # Compute forward products
    for i in range(1, length):
        forward[i] = forward[i-1] * nums[i-1]

    # Compute backward products
    for i in range(length-2, -1, -1):
        backward[i] = backward[i+1] * nums[i+1]

    # Combine forward and backward products
    for i in range(length):
        result[i] = forward[i] * backward[i]

    return result

print(product([1, 2, 3, 4]))
