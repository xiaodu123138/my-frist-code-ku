def car_info(maker,num,**car):
    car['car_maker']=maker
    car['car_num']=num
   
    
    return car
mes=car_info('audi','a6l',color='red',packages='tire')
print(mes)

