#Remove_duplicate_from_list.py

dup_list = [1,1,2,2,3,4,4,5]
final_list = []
for item in dup_list:
    if item not in final_list:
        final_list.append(item)
print(final_list)
