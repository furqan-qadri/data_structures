# check if an array contains a duplicate
def containsDuplicate(array):
    hashset=set()
    for nums in array:
        if nums in hashset:
            return True
        hashset.add(nums)
    return False

print(containsDuplicate([1,1,2,3]))
print(containsDuplicate([1,4,2,3]))
        