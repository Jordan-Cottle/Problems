# solution to https://open.kattis.com/problems/sumoftheothers

while True:
    try:
        nums = input().split()

        if( len(nums) < 2):
            break

        total = sum([int(num) for num in nums])
        print (total // 2)
    except:
        break
