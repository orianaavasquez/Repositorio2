def hello_world():
    print("Hello World")
    return True

def get_minimum(my_list):
    min_value=my_list[0]
    for element in my_list:
        if min_value >= element:
            min_value =element
    return min_value



hello_world()
