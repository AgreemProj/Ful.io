import re

def number_validation(number):    
    phone_pattern = '^[+]?[\d{1}]?[(|-|\s]?\d{3}[)]?[-|\s|\.]?\d{3}[-|\s|\.]?\d{4,5}$'
    match = re.search(phone_pattern, number)
    if match:
        return "Valid"
    else:
        return "Invalid"

if __name__ == '__main__':
    number = input("contact number : ")
    print(number_validation(number))