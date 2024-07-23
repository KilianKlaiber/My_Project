from merge_sort import merge


def kilian2_merge(new_list) -> list:
    
    while len(new_list) >= 2:  
        item1 = new_list.pop(0)
        if not isinstance(item1,list):
            item1 = [item1]
        item2 = new_list.pop(0)
        if not isinstance(item2,list):
            item2 = [item2]
        
        new_item = merge(item1, item2)
        new_list.append(new_item)
    
    return new_list