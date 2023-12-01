import sys

def do_the_number_county(string):
	if string[0].isdigit():
		return int(string[0])

	x = next(filter(string.startswith, numbers), None)
	return numbers.get(x, 0)

numbers = {
	'one'  : 1,
	'two'  : 2,
	'three': 3,
	'four' : 4,
	'five' : 5,
	'six'  : 6,
	'seven': 7,
	'eight': 8,
	'nine' : 9,
}

f = open('day1.txt', 'r')
file = f.readlines()

part1 = 0
part2 = 0

for line in file:
	part1 += 10 * int(next(filter(str.isdigit, line)))
	part1 += int(next(filter(str.isdigit, line[::-1])))

	for i in range(len(line)):
		a = do_the_number_county(line[i:])
		if a:
			break

	for i in range(len(line) - 1, -1, -1):
		b = do_the_number_county(line[i:])
		if b:
			break

	part2 += 10 * a + b

print('Day 1 Part 1:', part1)
print('Day 2 Part 2:', part2)