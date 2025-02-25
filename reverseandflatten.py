#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği
#gibi,non-scalar verilerden de oluşabilir. 
#Örnek olarak:

sample_list_1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(sample_list_1):
    flattened = []
    for item in sample_list_1:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

output_1 = flatten_list(sample_list_1)
print(output_1)


#Question2

sample_list_2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(sample_list_2):
    reversed_list = []
    for item in sample_list_2[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

output_2 = reverse_list(sample_list_2)
print(output_2)
