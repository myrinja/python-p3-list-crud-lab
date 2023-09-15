def create_an_empty_list():
    return []

def create_a_list():
    my_list= [1,2,3,4]
    return my_list
    

def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    return my_list
    

def add_element_to_start_of_list(my_list, element):
    my_list.insert(0,element)
    return my_list

def remove_element_from_end_of_list(list):
    list=[1,2,3,4]
    list.pop()
    return list

def remove_element_from_start_of_list(list):
    list = [1,2,3,4]
    del list[0]
    return list

def retrieve_first_element_from_list(list):
    return list[0]


def retrieve_element_from_index(list, index):

    return list[index]

def retrieve_last_element_from_list(list):
    return list[-1]
