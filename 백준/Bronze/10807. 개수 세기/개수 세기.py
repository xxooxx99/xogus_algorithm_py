nums = []
a = int(input())
nums = list(map(int,input().split()))
if len(nums) != a:
    print("input error")
    sys.exit()
else:
    b = int(input())
    print(nums.count(b))