def binary_tree_search(tree: list, value: int) -> bool:
    """
    Search a value in a binary tree.
    Return `True` if a value exists
    Return `False` if not.
    """
    result = False
    if not tree:
        return result
    for i in tree:
        if i == value:
            result = True
            break
        elif isinstance(i, list):
            result = binary_tree_search(i, value)
            if result:
                return result
    return result


tree = [10, [5, [3, None, None], [7, None, None]], [15, None, [20, None, None]]]
result = binary_tree_search(tree, 15)
print(result)
