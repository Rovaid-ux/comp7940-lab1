import json
import requests
site="https://api.npoint.io/2b57052af2060e84dc86"
# Write the functions convert_number and replace_number here
# Follow the logic below.
# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']
# Debug
for i in text:
    print("parse " + str(i))
# call the function convert_number
# convert all elements (except the first one) into number and
    # return it as a list
y = convert_number(text[0])
print("y")
print(y)
# call the function replace_number
# replace all number 1 by the number 10 in the function
z = replace_number(number_list = y, being_replace = 1, to_replace =10)
print("z")
print(z)
sum = 0
for i in z:
    sum = sum + i
    print("sum = " + str(sum) + "; i =" + str(i))
print ("Total = " + str(sum))




def convert_number(list_str):
    converted_list = []
    for item in list_str:
        try:
            item_int = int(item)
            converted_list.append(item_int)
        except ValueError:
            print(f"Skipping item '{item}' as it cannot be converted to an integer.")
    return converted_list

def replace_number(number_list,being_replace, to_replace):
    modified_list = []
    for number in number_list:
        if(number == being_replace):
            modified_list.append(to_replace)
        else:
            modified_list.append(number)
    return modified_list
    