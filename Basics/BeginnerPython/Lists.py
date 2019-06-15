users = ['val', 'bob', 'mia', 'ron', 'ned']

first_user = users[0]
second_user = users[1]

newest_user = users[-1]

users[0] = 'valerie'
users[-2] = 'ronald'

users.append('amy')

print(users)

users = []
users.append('val')
users.append('bob')
users.append('mia')

users.insert(0, 'joe')
users.insert(3, 'bea')
print(users)

del users[-1]
print(users)

users.remove('joe')
print(users)

# 弹出元素
most_recent_user = users.pop()
print(most_recent_user)

first_user = users.pop(0)
print(first_user)

print(users)
num_users = len(users)
print("we have " + str(num_users) + " users")

users.append('hou')
users.append('jing')
users.append('ru')
print(users)

users.sort()
users.sort(reverse=True)

print(sorted(users))
print(sorted(users, reverse=True))

users.reverse()

for user in users:
    print(user)

for user in users:
    print("Welcome," + user + "!")

print("Welcome, we're glad to see you all!")

for number in range(1001):
    print(number)

for number in range(1, 1001):
    print(number)

numbers = list(range(1, 1000001))

ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]

youngest = min(ages)
print(youngest)

oldest = max(ages)
print(oldest)

total_years = sum(ages)
print(total_years)

finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']

first_three = finishers[:3]
print(first_three)

middle_three = finishers[1:4]
print(middle_three)

last_three = finishers[-3:]

copy_of_finishers = finishers[:]
print(copy_of_finishers)


squares = []
for x in range(1, 11):
    square = x ** 2
    squares.append(square)
print(squares)

squares = [x ** 2 for x in range(1, 11)]
print(squares)
