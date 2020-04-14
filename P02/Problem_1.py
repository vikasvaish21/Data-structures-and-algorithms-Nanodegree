def sqrt(x):
    i_start = 0
    i_end = x // 2

    
    if x < 0:
        return None
    
    if (x == 0 or x == 1):
        return x
    
    while i_start <= i_end:
        middle = (i_start + i_end) // 2
        middle_pov = middle * middle

        if middle_pov == x:
            return middle
        elif middle_pov < x:
            i_start = middle + 1
            result = middle
        else:
            i_end = middle - 1

    return result
        
# Normal cases
print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass \n" if (5 == sqrt(27)) else "Fail \n")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")
