import math
def grouper(iterable):
    prev = None
    group = []
    for item in iterable:
        if not prev or item - prev <= 15:
            group.append(item)
        else:
            yield group
            group = [item]
        prev = item
    if group:
        yield group

if __name__ == "__main__":
	dicts={}
	numbers = [123, 124, 128, 160, 167, 213, 215, 230, 245, 255, 257, 400, 401, 402]
	dicts=(dict(enumerate(grouper(numbers), 1)))
	for i in dicts:
		print(len(dicts[i])-1)
	#print(dicts)
