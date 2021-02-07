def every_three_nums(start):
    return list(range(start, 101, 3))


def remove_middle(lst, start, end):
    del lst[start:end + 1]
    return lst


def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2


def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        new_list = lst[:index]
        new_list.append(lst[index] * 2)
        new_list = new_list + lst[index + 1:]
        return new_list


def middle_element(lst):
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
