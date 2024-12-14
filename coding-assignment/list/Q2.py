# Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false

def are_all_elements_palindromes(arr):
    for i in arr:
        str_i = str(i) 
        if str_i != str_i[::-1]: 
            return False
    return True

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
result = are_all_elements_palindromes(arr)
print(result)
