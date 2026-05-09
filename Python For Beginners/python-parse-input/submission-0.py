from typing import List

def read_integers() -> List[int]:
    return_list = input().split(",")
    for index, value in enumerate(return_list):
        return_list[index]=int(value)
    return return_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
