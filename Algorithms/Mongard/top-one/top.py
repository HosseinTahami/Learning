def top(array):

    values_dict = {}
    result = []

    for i in array:
        
        if i in values_dict:
            values_dict[i]+=1
        else:
            values_dict[i]=1
    
    maximum_repeat = max(values_dict.values())

    for i in values_dict:
        if values_dict[i] == maximum_repeat:
            result.append(i)
    
    return result

print(top([1,1,2,2,4,5]))