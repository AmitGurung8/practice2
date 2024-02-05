def p1():
    combined = input("Paste the nums: ")
    nums = []
    # width = int(input("How many digits in each number: "))
    width = 4
    index = 0
    for i in range(0, int(len(combined))):
        nums.append(combined[index:index + width - (width // 2)])
        index += width
        if index >= len(combined):
            break
    nums.sort()
    minnum = min(nums)
    maxnum = max(nums)
    median = 0
    if len(nums) % 2 == 0:
        m1 = nums[len(nums) // 2 + 1]
        m2 = nums[len(nums) // 2]
        median = (m1 + m2) / 2
    else:
        median = nums[len(nums) // 2]
    q1 = 0
    median = int(median)
    midpoint = len(nums) // 2
    if len(nums) % 2 == 0:
        q1 = nums[midpoint - int(midpoint / 2)]
    else:
        q1 = nums[midpoint - int(midpoint / 2) - 1]

    q3 = 0
    if len(nums) % 2 == 0:
        q3 = nums[midpoint + int(midpoint / 2)]
    else:
        q3 = nums[midpoint + int(midpoint / 2) + 1]
    print("Min is:", minnum)
    print("Q1:", q1)
    print("Q2:", median)
    print("Q3:", q3)
    print("Max is:", maxnum)
    print("Range is:", int(maxnum) - int(minnum))
    print("IQR is:", int(q3) - int(q1))


def p3():
    mean = 0
    combined = int(input("Paste the nums: "))
    # width = int(input("How many digits in each number: "))
    width = 3
    vals = 0
    index = 0
    median = 0
    allvals = []
    for i in range(0, int(len(str(combined)) / width)):
        allvals.append(str(combined)[index:index + width])
        vals += 1
        index += width
    for i in allvals:
        mean += int(i)
    mean /= vals
    print("Mean is", mean);
    sum = 0
    allvals.sort()
    if len(allvals) % 2 == 0:
        median = float(allvals[len(allvals) // 2 - 1])
        median2 = float(allvals[len(allvals) // 2])
        median = (median + median2) / 2
    else:
        median = allvals[len(allvals) // 2]
    print("Median is", median)
    for i in allvals:
        val = int(i)
        val -= mean
        val *= val
        sum += val
    sum *= (1 / (vals - 1))
    print("Variance is", sum)
    sum = 0
    for i in allvals:
        val = int(i)
        val -= mean
        val *= val
        sum += val
    sum *= (1 / (vals - 1))
    sum = sum ** (1 / 2)
    print("Standard deviation is", sum)
    sum = sum / mean
    sum *= 100
    print("Coefficient of variation is", sum)


def p4():
    for i in range(0, 4):
        print("Row", i + 1)
        mean = float(input("Mean: "))
        deviation = float(input("Deviation: "))
        score = float(input("Score: "))
        z = (score - mean) / deviation
        print("Z score:", z)


def p5():
    combined = input("Paste the nums: ")
    nums = []
    # width = int(input("How many digits in each number: "))
    width = 4
    index = 0
    for i in range(0, int(len(combined))):
        nums.append(combined[index:index + width - (width // 2)])
        index += width
        if index >= len(combined):
            break
    nums.sort()
    mean = 0
    for i in nums:
        mean += int(i)
    mean /= len(nums)
    print("Mean is", mean);
    sum = 0
    for i in nums:
        val = int(i)
        val -= mean
        val *= val
        sum += val
    sum /= len(nums) - 1
    sum = sum ** (1 / 2)
    print("Standard deviation is", sum)
    for i in range(0, 2):
        score = int(input("Enter the raw score:  "))
        score -= mean
        score /= sum
        print("Z score:", score)
    score = float(input("Enter the Z score:  "))
    score = score * sum + mean
    print("Raw score:", score)
    dev = float(input("Enter the standard deviations:  "))
    dev = dev * sum + mean
    print("Raw score:", dev)
    print("Answer to (i) is", mean)


def p6():
    combined = input("Paste the nums: ")
    nums = []
    # width = int(input("How many digits in each number: "))
    index = 0
    for i in range(0, int(len(combined))):
        width = 0
        if index >= len(combined) - 2:
            width = len(combined) - index
            nums.append(int(combined[index:index + width]))
            break
        if combined[index + 1] == ",":
            width = 1
        elif combined[index + 2] == ",":
            width = 2
        nums.append(int(combined[index:index + width]))
        index += width + 2
        if index >= len(combined):
            break
    nums.sort()
    midpoint = len(nums) // 2
    q1 = 0
    q3 = 0
    if len(nums) % 2 == 0:
        q1 = nums[midpoint - int(midpoint / 2)]
        q1 += nums[midpoint - int(midpoint / 2) - 1]
        q1 /= 2
        q3 = nums[midpoint + int(midpoint / 2)]
        q3 += nums[midpoint + int(midpoint / 2) - 1]
        q3 /= 2
    iqr = float(q3) - float(q1)
    num1 = q1 - 1.5 * iqr
    num2 = q3 + 1.5 * iqr
    print("Any number less than", num1, "is an outlier")
    print("Any number greater than", num2, "is an outlier")
    for j in range(0, len(nums)):
        if nums[j] < num1 or nums[j] > num2:
            print(nums[j], "is an outlier")


def p7():
    print("25.04, larger")


while True:
    c = int(input("Enter the number of the problem you are on: "))
    if c == 1:
        p1()
    elif c == 2:
        print("five-number, median, 50%")
    elif c == 3:
        p3()
    elif c == 4:
        p4()
    elif c == 5:
        p5()
    elif c == 6:
        p6()
    elif c == 7:
        p7()
    elif c == 8:
        print("Can't help")
    elif c == 9:
        print("Skewed left, median")
    elif c == 10:
        print("75%")