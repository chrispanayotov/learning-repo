# Implement the function unique_in_order which takes as argument a sequence and 
# returns a list of items without any elements with the same value next 
# to each other and preserving the original order of elements.

def unique_in_order(iterable):
    answer_list = []
    for index, value in enumerate(iterable):
        if value not in answer_list or value != iterable[index-1]:
            answer_list.append(value)
    return answer_list


unique_in_order('AAAABBBCCDAABBB') # == ['A', 'B', 'C', 'D', 'A', 'B']