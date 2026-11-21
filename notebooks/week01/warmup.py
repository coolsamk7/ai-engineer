nums = (int(x) for x in ["1", "2", "3"])
print(sum(nums))
print(sum(nums))


def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_item("x"))
print(add_item("y"))
print(add_item("z", ["w"]))

squares = {n: n * n for n in range(4) if n % 2 == 0}

print(squares)

try:
    int("abc")
except ValueError as e:
    print("bad", e)
finally:
    print("done")

print("---")
nums = (int(x) for x in ["1", "2", "3"])
print(type(nums))
print(list(nums))
print(list(nums))

nums_list = [int(x) for x in ["1", "2", "3"]]
print(type(nums_list))
print(sum(nums_list), sum(nums_list))

nums = (int(x) for x in ["1", "2", "3"])
print(next(nums))
print(next(nums))
print(sum(nums))
print(sum(nums))
