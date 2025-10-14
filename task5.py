# 练习8-1，2
def display_message():
    print('woxuelehenduo')

display_message()


def favorite_book(title):
    print(f'I like {title}')
favorite_book('king')
# 练习8-3,4,5
def make_shirt(size,mode):
    print(f'T should {size},{mode}')
make_shirt(23,'blue')
make_shirt(mode='red',size=2)

def make_shirt(size,mode='I love python'):
    print(f'T should {size},{mode}')
make_shirt('big',)
make_shirt('intermediate',)
make_shirt('small','love')

def describe_city(name,country='china'):
    print(f'{name} is in {country}')
describe_city('chansgha',)
describe_city('bay','us')
# 练习8-6,7,8
# def city_country(name,country):
#     return f'"{name.title()},{country.title()}"'

# print(city_country('jinan','china'))
# print(city_country('taishan','china'))
# print(city_country('xian','china'))

# def make_album(singer_name,album_name):
#     album={}        
#     # 把字典定义在内部 这样就可以每次都创建独立的字典了
#     album[singer_name]=album_name
#     return album
# print(make_album('wangfeng','nufang'))
# print(make_album('longjuanfeng','jay'))

# def make_album(singer_name,album_name):
#       album={}      
#     # 把字典定义在内部 这样就可以每次都创建独立的字典了
#       album[singer_name]=album_name
#       return album

# while True:
#     print('这是一个记录歌手姓名和歌手专辑的程序!\n(输入 quit 为退出):')
    
    
#     singer_name=input('请输入歌手姓名:')
#     if singer_name=='quit':
#         break
    
#     album_name=input('请输入专辑名称:')   
#     if album_name=='quit':
#         break
    
#     print(make_album(singer_name,album_name))


# 练习8-9~8-11
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
magicians=['a','b','c']
show_magicians(magicians)

magicians=['a','b','c']
sent_messages=[]
def send_messages(magicians,sent_messages):
    while magicians:
        current_magician=magicians.pop()
        print(f'正在发送:{current_magician}')
        sent_messages.append(current_magician)

send_messages(magicians,sent_messages)
print(magicians)
print(sent_messages)


# !!!!!!!!!
magicians=['a','b','c']
sent_messages=[]
def send_messages(magicians,sent_messages):
    while magicians:
        current_magician=magicians.pop()
        print(f'正在发送:{current_magician}')
        sent_messages.append(current_magician)

send_messages(magicians[:],sent_messages)
print(magicians)
print(sent_messages)


# 练习8-12~8-14
def make_sandwich(*toppings):
    print('你点的三明治有:')
    for topping in toppings:
        print(f'-{topping}')
make_sandwich('a')
make_sandwich('a','b')
make_sandwich('a','b','c')



def build_profile(first,last,**profile):
    
    profile['first_name']=first
    profile['last_name']=last
    return profile
user_profile=build_profile('du','qianjin',country='china',field='dianzi')
print(user_profile)
# def car_info(maker,num,**car):
#     car['car_maker']=maker
#     car['car_num']=num
#     return car
# mes=car_info('audi','a6l',color='red',packages='tire')
# print(mes)
# import make_car_function
# make_car_function.car_info('audi','a6l',color='red',packages='tire')
# from make_car_function import car_info
# car_info('audi','a6l',color='red',packages='tire')
# from make_car_function import car_info as jjj
# jjj('audi','a6l',color='red',packages='tire')
import make_car_function as m
m.car_info('audi','a6l',color='red',packages='tire')
print('hhh')

from make_car_function import *
car_info('audi','a6l',color='red',packages='tire')
print('hhh')
   
    
















