def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    triplets = []

    for i in range(len(nums) - 2):
        # Skip the same element to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1  # We need a larger sum
            elif total > 0:
                right -= 1  # We need a smaller sum
            else:
                # Found a triplet
                triplets.append((nums[i], nums[left], nums[right]))
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
    
    return triplets

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)  # Output: [(-1, -1, 2), (-1, 0, 1)]
