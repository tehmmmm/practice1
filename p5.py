def stats(nums):
    lowest = min(nums)
    highest = max(nums)
    average = sum(nums) / len(nums)
    return lowest, highest, average
nums = [4, 8, 15, 16, 23, 42]
lo, hi, avg = stats(nums)
print(lo, hi, avg)
def grade(marks, passing=50):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"
print(grade(55), grade(55, passing=60))
