# 练习3-1~3-3
names=['jack','rose']
print(names[0])
print(names[1])

names=['jack','rose']
print(f'Hello,{names[0].title()}!')
print(f'Hello,{names[1].title()}!')

modes=['bike','car']
print(f'I would like to own a nice {modes[1]}.')

# 练习3-4~3-7
lists=['jack','rose','lebron']
print(f'I would like to invite {lists[0].title()} to join in dinner.')
print(f'I would like to invite {lists[2].title()} to join in dinner.')

print(f'{lists[0].title()} can not join in it.')
lists[0]='curry'
print(f'I would like to invite {lists[0].title()} to join in dinner.')
print(lists)

print('I seeked for a big table.')
lists.insert(0,'love')
lists.insert(len(lists)//2,'smith')
lists.append('durant')
print(lists)
print(f'I would like to invite {lists[-1].title()} to join in dinner.')

print('I only invite two person to join in it.')
num1=lists.pop()
print(f'{num1},sorry!')
num2=lists.pop()
print(f'{num2},sorry!')
print(f'{lists[0].title()} is lucky!')
print(f'{lists[1].title()} is lucky!')
del lists[0:]
print(lists)

# 练习3-8~3-10
places=['taishan','beijing','shanghai']
print(places)
places1=sorted(places)
print(places1)
print(places)
places1=sorted(places,reverse=True)
print(places1)
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

places=['taishan','beijing','shanghai']
# print(places[7]) error
print(places[2])


# 练习4-1~4-2 for循环 遍历
pizzas=['liulian','beef','backon']
for pizza in pizzas:
    # print(piza)
    print(f'I like {pizza} piza.')
print('I really love pizza!')

animals=['dog','cat','pig']
for animal in animals:
    # print(animal.title())
    print(f'A {animal} would make a great pet.')
print('Any of these animals would make a great pet!')

# 练习4-3~4-9
for num in range(1,21):
    print(num)
# numbers=list(range(1,10000001))
# print(numbers)

# for num in numbers:
#     print(num)
# numbers=list(range(1,1001))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

numbers=list(range(1,21,2))
print(numbers)
for number in numbers:
    print(number)

numbers=list(range(3,31,3))
for number in numbers:
    print(number)
print(numbers)

numbers=list(range(1,11))
for number in numbers:
    print(number**3)
lifangs=[]
for value in range(1,11):
    # lifang=value**3
    # lifangs.append(lifang)
    lifangs.append(value**3)
print(lifangs)
for lifang in lifangs:
    print(lifang)
lifangs=[value**3 for value in range(1,11)]
print(lifangs)
# 列表解析 太妙了~~~

# 练习4-10~4-12
animals=['dog','cat','fox','pig']
for animal in animals:
    # print(animal.title())
    print(f'A {animal} would make a great pet.')
print('Any of these animals would make a great pet!')
print(f'The first two items in the list are:')
for animal in animals[0:2]:
    print(animal)
for animal in animals[1:3]:
    print(animal)
for animal in animals[-2:]:
    print(animal)
    
pizzas=['liulian','beef','backon']
for pizza in pizzas:
    # print(piza)
    print(f'I like {pizza} piza.')
print('I really love pizza!')

friend_pizza=pizzas[:]
pizzas.append('pork')
friend_pizza.append('sheep')
print(pizzas)
print(friend_pizza)
print(f'"My favorite pizzas are" :')
for pizza in pizzas:
    print(pizza)
for friend in friend_pizza:
    print(friend)

# 练习4-13
foods=('a','b','c')
for food in foods:
    print(food)
# foods[0]='c'
# foods[0]='d'
# foods[1]='e'
# print(foods)
# 上面三行是错误的
foods=('a','e','f')
for food in foods:
    print(food)


# 练习5-1~5-2 if 语句
car='audi'
print('Is car =="aud"? I predict Fasle')
print(car=='aud')

pizzas=['liulian','beef','backon']
if 'bef' not in pizzas:
    print('you are right')
else:
    print('you are wrong')
    
# 练习5-3~5-7
alien_color='red'
if alien_color=='green':
    print('you get five points')
if alien_color=='red':
    print('you get five points')

alien_color='red'
if alien_color=='green':
    print('you get five points')
else:
    print('you get ten points')
if alien_color=='red':
    print('you get five points')
else:
    print('you get ten points')

alien_color='blue'
if alien_color=='green':
    print('you get five points')
elif alien_color=='red':
    print('you get ten points')  
elif alien_color=='blue':
    print('you get fif points')

age=101
if age<2:
    print('fant')
elif 2<=age<4:
    print('baby')
elif 4<=age<13:
    print('child')
elif 13<=age<20:
    print('teen')
elif 20<=age<65:
    print('adult')
else:
    print('elder')
fruits=['apple','orange','strawberry']
if 'apple' in fruits:
    print('yes')
faovrite_fruits=['apple','orange']
if 'huolongguo' not in fruits:
    print('no')
if 'banana' not in fruits:
    print('yes')

# 练习5-8~5-11
users=['admin','b','c','d']
for user in users:
    if user=='admin':
        print(f'Hello {user},I miss you!')
    else:
        print(f'Hello {user},thank you!')
u=[]
if not  u:
    print('we need users')
else:
    print('yes')

current_users=['love','b','B','d']
new_users=['LOVE','curry','bob','d']
for new_user in new_users:
    if new_user in current_users:
        print(f'the {new_user} is bad,you need a new username!')
    else:
        print(f'the {new_user} is ok!')

# current_users1=[]
# for user in current_users:
#     current_users1.append(user.lower())
current_users=['love','b','B','d']
new_users=['LOVE','curry','bob','d']
current_users1=[user.lower() for user in current_users]
# 列表解析式！
print(current_users1)
for new_user in new_users :
    if new_user.lower() in current_users1:
        print(f'the {new_user} is bad,you need a new username!')
    else:
        print(f'the {new_user} is ok!')

numbers=list(range(1,10))
print(numbers)
for num in numbers:
    # print(num)
    if num ==1:
        print('1st')
    elif num==2:
        print('2nd')
    elif num==3:
        print('3rd')
    else:
        print(f'{num}th')
# 练习6-1~6-3
messages={
    'f_name':'lebron','l_name':'james','age':41,'city':'US'
    }
print('姓:',messages['f_name'].title())
print('名:',messages['l_name'].title())



num={'lebron':23,'curry':30,'durant':35}   
for name,num1 in num.items():
    print(f'{name} like {num1}')

fun={'int':'整形','float':'浮点型'}  
for term,meaning in fun.items():
    print(f'{term}: \n\t{meaning}')
# print(fun['point'])
# print(fun.get('point','no value'))


# 练习6-5~6-6
mes={'a':1,'b':2}
for num1,num2 in mes.items():
    print(f'{num1},{num2}')
for num1 in mes.keys():
    print(num1)
for num2 in mes.values():
    print(num2)

faovrite_languages={
    "james":'English',
    'jack':'Chinese',
    "rose":'English'
}
approve=['james','rose','bob']
for person in approve:
    if person in faovrite_languages:
        print(f'{person}感谢参与')
    else:
        print(f'{person} i want invite you')


# 练习6-7~6-12.
messages1={
    'f_name':'lebron','l_name':'james','age':41,'city':'US'
    }
# print('姓:',messages['f_name'].title())
# print('名:',messages['l_name'].title())
messages2={
    'f_name':'curry','l_name':'james','age':41,'city':'US'
    }       
messages3={
    'f_name':'love','l_name':'james','age':41,'city':'US'
    }          
peoples=[messages3,messages2,messages1,]
for people in peoples:
    print(people)

favorite_places={'james':['a','b'],
                 'love':['c','d']
                 }
    
for name,places in favorite_places.items():
    print(name,':')
    for  place in places:
           print(place)
          
        


num={'lebron':[2,3,4],'curry':[42,22],'durant':[2424,2424]}   
for name,num1 in num.items():
    print(f'{name} like {num1}')


cities={'changsha':{'country':'china','fact':'nice'},
        'beijing':{'country':'china','fact':'core'}
        
        }
        
for city,mes in cities.items():
    print(city,":")
    for mes1,mes2 in mes.items():
        print(f'{mes1}:{mes2}')
        




        
           
    
        
        

       
    
    

    
    
    




        



    

    

    
   







































