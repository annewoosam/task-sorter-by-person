
# A mash-up of
# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
# https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# Adds items to a dictionary key which stands for assignee then sorts by assignee
print("To add a task specify who and what in the append instruction - the system will sort tasks by name alphabetically and add new tasks to each person. You can arrow up to edit who and what for the next item: append_task(task, 'Who', 'What')")
print("When done enter: print(sorted(task.items()))")
print("Does not yet account for duplicates in an individual's task list.")

def append_task(dict_obj, key, value): 
# Check if key exist in dict or not 
    if key in dict_obj: 
# Key exist in dict. 
# Check if type of value of key is list or not 
        if not isinstance(dict_obj[key], list): 
# If type is not list then make it list 
            dict_obj[key] = [dict_obj[key]] 
# Append the value in list 
        dict_obj[key].append(value) 
    else: 
# As key is not in dict, 
# so, add key-value pair 
        dict_obj[key] = value 
# Dictionary of strings and ints 
task = {}                                                                                      
print(sorted(task.items()))