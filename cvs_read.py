line_counter = 0 # 줄 생성 함수
data_header = [] #data의 필드값을 저장하는 list
customer_list = [] #customer 개별 list를 저장하는 list

with open("customers.csv") as customer_data: #customer.csv 파일을 customer_data에 저장
    while True:
        data = customer_data.readline() #readlines 나 read도 해보자!
        if not data: 
            break
        if line_counter == 0: #데이터가 없을 때, loop 종료
            data_header = data.split(",")
        else:
            data2 = data.split(",")
            customer_list.append(data2)
            
        
        line_counter += 1

print("Header :\t", data_header)
for i in range(0, 10):
    print("Data", i, ":\t\t", customer_list[i])
print(len(customer_list)) # 몇 개의 리스트?

import pprint

pprint.pprint(customer_list)






