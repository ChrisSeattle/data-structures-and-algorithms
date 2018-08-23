from .linked_list import LinkedList, Node


def merge_lists(inp1, inp2):
    """ Takes in two LinkedLists and returns one LinkedList that is the nodes
        of the inputs placed in alternating order (starting with the beginning
        of inp1). This should work as long as both inputs are non-circular
        LinkedLists of any length.
    """
    # isinstance(inp1, LinkedList)
    if inp1.head is None:
        if inp2.head is None:
            return None
        return inp2
    if inp2.head is None:
        return inp1
    curr, curr2 = inp1.head, inp2.head

    while True:
        if curr.next is None:
            curr.next = curr2
            return
        temp, curr.next = curr.next, curr2
        if curr2.next is None:
            curr2.next = temp
            return
        temp2, curr2.next = curr2.next, temp
        curr, curr2 = temp, temp2
    return inp1
