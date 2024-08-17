


username = "qiuze"

a  = [username[0].upper()+username[1:],username]
#年份
b = ['2019','2020','2021','2022','2023']
c= ['.','!']
for b1  in b:
    for a1 in a:
        for c1 in c:
            print(a1+b1+c1)


for i in range(0,9):
    for j in range(0,9):
        print(username+str(i)+str(i)+str(i)+str(i))