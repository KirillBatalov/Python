students = input().split(', ')
years = list(map(int, input().split(', ')))
year2filter = int(input())
for i in range(len(years)):
    if years[i] >= year2filter:
        print(students[i])

