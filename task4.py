# 练习7-1~7-3
# car=input('What kind of car do you want?' )
# print(f'Let me see if I can find you a {car}')
# num=input('请问有多少人用餐: ')
# num=int(num)
# if num>8:
#     print('请稍等')
# else:
#     print('有位置')


# num=input('请输入一个数字: ')
# num=int(num)
# if num %10 ==0:
#     print('是10的整数倍')
# else:
#     print('不是10的整数倍')

# 练习7-4~7-7
# prompt='请输入配料的名'
# prompt+='\n(输入 quit 为退出):'
# messgae=""
# while messgae !='quit':
#     messgae=input(prompt)
#     if messgae !='quit':
#         print(f'我会在披萨中添加{messgae}')

# prompt='你的年龄是多少？'     
# prompt+='\n(输入 quit 为退出):'

# while True:
#     age=input(prompt)
#     if age=='quit':
#         break
#     age=int(age)
#     if age<3:
#         print('免费')
#     elif 3<=age<12:
#         print('10美元')
#     elif age>=12:
#         print('15美元') 

# prompt='请输入配料的名'
# prompt+='\n(输入 quit 为退出):'
# messgae=""
# while messgae !='quit':
#     messgae=input(prompt)
#     if messgae !='quit':
#         print(f'我会在披萨中添加{messgae}')

# prompt='请输入配料的名'
# prompt+='\n(输入 quit 为退出):'
# active=True
# while active:
#     message=input(prompt)
#     if message=='quit':
#         active=False
#     else:
#         print(f'我会在披萨中添加{message}')

# prompt='请输入配料的名'
# prompt+='\n(输入 quit 为退出):'
# while True:
#     message=input(prompt)
#     if message=='quit':
#         break
#     else:
#         print(f'我会在披萨中添加{message}')
# num=0
# while num < 10:
#     num += 1
#     print(num)
# 练习7-8~7-10
# sandwich_orders=['pastrami','beef','chicken','veggie']
# finished_sandwiches=[]
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     print(f'I made your {sandwich} sandwich.')
#     finished_sandwiches.append(sandwich)

# print('The following sandwiches have been made:')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# final
# sandwich_orders=['pastrami','beef','chicken','veggie','pastrami','pastrami']
# print('Deli has run out of pastrami.')
# while 'pastrami'in sandwich_orders:
#       sandwich_orders.remove('pastrami')
# finished_sandwiches=[]
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     print(f'I made your {sandwich} sandwich.')
#     finished_sandwiches.append(sandwich)

# print('The following sandwiches have been made:')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

responses={}
while True:
     name=input('What is your name?')
     response=input('if you visit one place in the world,where would you go?')
     responses[name]=response
     repeat=input('Would you like to let another person respond? (yes/no)')
     if repeat=='no':
         break
print('\n下面是调查结果')
for name,response in responses.items():
    print(f'{name} would like to go to {response}.')

