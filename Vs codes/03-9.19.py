# part 1！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
new= 'hello tust'
print(new) 
# ctrl+/ '''  '''       /注释快捷键
new1='lebron james'
print(new1.title())
# .title() upper lower 方法改变字符串的大小写
first_name='lebron'
last_name='james'
full_name=f'{first_name} {last_name}'
print(full_name.title())
# f 字符串 在字符串中使用变量 替换变量的值
print('\n\thello tust')
print(3**8)
print(8/2)
x,y,z=0,2,5 
print(x,y)
# MAX_VALUE=900000 常量 


# part 2 列表（存储东西的容器）位置（索引）！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
foods=['meat','rice','noodle']
print(foods)
print(foods[2])
print(foods[-1])
print(f'My favorite food is {foods[1].title()}')
foods[2]='tomato'
print(foods)
foods.append('potato')
print(foods)

foods2=[]
foods2.append('apple')
foods2.append('orange')
print(foods2)
foods2.insert(0,"banana")
print(foods2)
# 总结:动态的创建列表
# del foods2[0]
# print(foods2)
# print(foods2[0])
# new3=foods2.pop()
# print(foods2)
# print(new3)
new4=foods2.pop(1)
print(foods2)
bee = 'orange'
foods2.remove(bee)
print(foods2)
print(bee)
# 总结:使用 del ，pop，remove 删除列表中的元素 pop有返回值接着用前提是知道索引位置 remove是根据值来删除
cars=['bmw','audi','benchi']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(sorted(cars,reverse=True))
cars.reverse()
print(cars)
cars.reverse()
print(cars)
print(len(cars))
# 总结：组织列表 排序，打印，知道列表的长度
# part 3 操作列表 for循环！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
players=['jordan','lebron','curry']
print(players[1])
for player in players:
    print(player) 
    # 单复数命名
for player in players:
    print(f'{player.title()} is very powerfu !')
    print(f'\tI very like {player.title()} .\n')
print('today is over!.')
# 缩进问题
#  for 1 in 2 : 格式
for value in range(1,100):
    print(value)
for value in range(9):
    print(value)
# range 生成一系列数
numbers = list(range(2,28,2))
print(numbers)


squares=[]
for value in range(1,11):
    # square=value**2
    # squares.append(square)
    squares.append(value**2)
print(squares)
# 生成1~10的整数平方的列表
print(max(squares))
squares=[value**2 for value in range(1,11)]
print(squares)
# 列表解析难哦！

    
    

    
    






























































