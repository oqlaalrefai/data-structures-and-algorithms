from code_challenges.linked_list.linked_list import LinkedList

def zip_lists( list1, list2):

    if not list1 :
        return list1 
    if not list2 :
        return list1 
    output =LinkedList()
    current1 =list1.head
    current2 =list2.head
    while current1 :
        output.append(current1.data)
        if current2 :
            output.append(current2.data)
            current2 = current2.next
        current1= current1.next
    while current2 :
        output.append(current2.data)
        current2 =current2.next
    return output
if __name__ == '__main__':

    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
 
    list2 = LinkedList()
    list2.append(0)
    list2.append(5)
    list2.append(15)
    list2.append(25)
    print(zip_lists(list1,list2))