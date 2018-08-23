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
    out = LinkedList()
    curr, curr2 = inp1.head, inp2.head

    while True:
        if curr._next is None:
            curr._next = curr2
            return
        temp, curr._next = curr._next, curr2
        if curr2._next is None:
            curr2._next = temp
            return
        temp2, curr2._next = curr2._next, temp
        curr, curr2 = temp, temp2
    current = inp1.head
    while current.next is not None:
        print(current.val)
        current = current.next
    return inp1
