#1 create the list of 10nums print the sum of last 4 elements of the list ,
#2 find out the difference between max and min element of the list ,
#3 insert a num in a list at sixth position this num must be 1/3 of num stored at 4th postion

#1
nums = [10,20,30,60,70,80,160,170,180,190]
sum = 0
for num in nums[-4:]:
    sum += num
print("sum of last 4 digits is :",sum)

#2
diff = max(nums) - min(nums)
print("Max - Min =",diff)

#3
new_num = nums[3] // 3
nums.insert(5,new_num)
print("New String is :",nums)

