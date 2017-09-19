# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

def odd_filter(list):
    odd_list = []
    for i in list:
        if i%2 == 1:
            odd_list.append(i)
    return odd_list
print(odd_filter([1, 2, 3, 4, 5, 66, 83, 98, 101]))  # should print [1, 3, 5]