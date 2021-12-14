def left_join(hash1,hash2):
    output = []
    single_elem = []
    for elem in hash1.map:
        if elem:
            current = elem.head
            
            while current:
                single_elem.append(current.data[0])
                single_elem.append(current.data[1])
                if hash2.contains(current.data[0]):
                    single_elem.append(hash2.get(current.data[0]))
                else:
                    single_elem.append(None)
                output.append(single_elem)
                single_elem = []
                current = current.next
    return output