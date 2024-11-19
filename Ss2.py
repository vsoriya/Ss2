# 1. ប្រើ while loop
# បង្កើតលំដាប់លេខដោយប្រើ while loop:

numbers = []
a = 1
while a < 10:
    numbers.append(a)
    a += 2

print(numbers)  # [1, 3, 5, 7, 9]





# 2. ប្រើ map និង lambda
# ប្រើ map ដើម្បីបំលែងលំដាប់ចេញ:

numbers = list(map(lambda x: x, range(1, 10, 2)))
print(numbers)  # [1, 3, 5, 7, 9]
# ពន្យល់:
#
# ប្រើ lambda function ក្នុង map ដើម្បីប្តូរតម្លៃ range ជា list។





# 3. ប្រើ filter ដោយប្រើ Even/Odd Logic
# ស្វែងរកលេខអសមអាពី range:

numbers = list(filter(lambda x: x % 2 != 0, range(1, 10)))
print(numbers)  # [1, 3, 5, 7, 9]
# ពន្យល់:
#
# ប្រើ filter ដើម្បីជ្រើសតែលេខអសមអាពី range(1, 10)។






# 4. ប្រើ NumPy (បើត្រូវការ library ផ្ទៃក្រៅ)
import numpy as np

numbers = np.arange(1, 10, 2).tolist()
print(numbers)  # [1, 3, 5, 7, 9]
# ពន្យល់:
#
# ប្រើ numpy.arange ដើម្បីបង្កើតលំដាប់ចេញជាតារាង, បន្ទាប់មកបំលែងទៅជា list។






# 5. ប្រើ Function ដោយផ្ទាល់
# សរសេរ function ដើម្បីបង្កើត list:

def create_odd_numbers(start, stop, step):
    numbers = []
    while start < stop:
        numbers.append(start)
        start += step
    return numbers

print(create_odd_numbers(1, 10, 2))  # [1, 3, 5, 7, 9]



print( "hello ")












