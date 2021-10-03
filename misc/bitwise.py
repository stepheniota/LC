'''
cool bitwise operations I learned to do in python
'''

def is_even(num: int) -> bool:
    '''Fast `is_even?` operation using bitwise and'''
    return not num & 1

