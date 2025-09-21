# part1 列表的切片

players=['jordan','lebron','curry']
print(players[1:])
print(players[-3:])
print("下面是金牌和银牌的获奖者名单:")
for player in players[:2]:
    print(player)
# 对列表中的部分元素（切片）进行操作
friend_players=players[:]
players.append("durant")
friend_players.insert(1,"yao")
print(friend_players)
print(players)
# 切片创建副本

# 元组：不可变的列表!!!!!!!

# players=('jordan','lebron','curry')
# players[1]="love"
# print(players)
players=('jordan','lebron','donic')
for player in players:
    print(player)
# 可以给定义元组的变量赋值


# part2 if语句 条件测试
ages=[18,22,30]
if ages[0] != 19:
   print("i am so happy now")
age1 =20
age2 =22
score= age1>=23 or age2<=24
print(score)
if 17 not in ages:
    print("hello")
# 关键字in 和 not in 检查特定的值是否在列表中very useful
ages=[18,22,30]
if ages[0]==19:
    print('yes')
else:
    print('no')
# if else 非常适合2选择1的情况
# if elif else 多个else 即多种情况 例如景区门票按年龄分分配
# 最后的else代码块可以设置成当且仅当的情况 可以防止无效甚至是恶意的数据    
# 执行多个代码块 就用一系列独立的if语句；只执行一个代码块就用if-else-else结构   
    # example
foods=['apple','orange' ,'banana']
for food in foods:
   if food == 'orange':
         print(f"sorry,your {food} is not enough !")
   else:
        print(food)
print("happy our")

foods1=[]
if foods1:
    print('you choose')
else:
    print("your list is empty !")
# 确定列表不是空的
fixed_foods=('apple','orange' ,'banana')
client_foods=["apple",'juzi']
for client_food in client_foods:
    if client_food in fixed_foods:
        print(f"your {client_food} is enough")
    else:
        print('sorry,your food is not enough')
print('happy to you')


# part 3 字典 将相关信息关联起来 it is 一系列键值对
alien0={'point':2,'color':'red'}
print(alien0['color'])
# 访问字典中的值
print(alien0)

alien0['food']='milk'
print(alien0)
alien0['point']=3
print(alien0)
# 修改和添加字典的值   字典名[键]=值
del alien0['color']
print(alien0)
game_scores={
    "jack":2,
    "rose":3,
    "aton":6
    }
score=game_scores['jack']
print(f"jace's score is {score}")
# 由类似对象组成的字典即多个对象表示共同的信息 ，之前是一个对象的多个信息。

# afternoon！！！！！
alien0={'point':2,'color':'red'}
newvalue=alien0.get("p","no-value")
print(newvalue)
# .get() 访问值
  
  
alien1={
    'point':2,
    'color':'red',
    'sex':'male'
    }
for name,score in alien1.items():
    # print(f'my {name.title()} is {score}!')
    print(f'\n{name}:\n{score}')
for name in alien1.keys():
    print(name.title())


# example1
favorite_players={'jordan':1,'lebron':2,'curry':3}
friend_players=['jordan','love']
for name in favorite_players.keys():
    print(f'Hi,{name}')
    if name in friend_players:
        name1=favorite_players[name]
        print(f'i am very happy to see {name1}')
# friend_players是一个列表 方括号且没有键值对，针对于键的操作.keys()

favorite_players={'jordan':1,'lebron':1,'curry':3}
for player in sorted(favorite_players.keys()):
    print(player)
print(favorite_players)
print('下面是各类球员的总得分:')
for score in set(favorite_players.values()):
    print(score)
# 这是针对于值的操作。。。。。.values()   // 

# example创建100个吃汉堡的年轻人
youngers=[]
for younger in range(1000):
    new_younger={'look':'handsome',"language":'English'}
    youngers.append(new_younger)
    print(youngers)
    
for younger1 in youngers[:5]:
    print(younger1)
print(f'总共有多少个：{len(youngers)}')
# 字典列表 就是把字典嵌套到列表里面
food = {
        'type':'thick',
        'toppings':['milk','apple','bread']
        }
print(f'you need {food["type"]} food include following toppings:')
for topping in food['toppings']:
    print('\t'+topping)
# 把列表嵌套在字典里面
# 字典中的一个键关联多个值 就可以列表嵌套字典！！！！！！
f_lan={
      "jack":['c','python'],
      "curry":['c'],
      "love":['c++','c','python'] 
      }

for name, languange in f_lan.items():
        print(f"{name.title()} very like are:")
    
        for language1 in languange:
            print(language1)
# 字典包含字典 比如多个网站用户，有自己独特的用户名
NBA_players = {
'king':{
   'full_name':'lebron james',
   'age': 41
    },
'killer':{
    'full_name':'kevin durant',
     'age':37
    }

  }
for playername,playerage in NBA_players.items():
    print(f'\nPlayname:{playername}')
    
    
    
    print(f'\nFull_name is {playerage['full_name']}')
    print(f'playerage is {playerage['age']}')
players=['jordan','lebron','curry']
# //


    
    
    

    
            
        
         

    


    

    
        
    

    

    






        
        

    
    

        
        

    

          

    


   

    





    






















