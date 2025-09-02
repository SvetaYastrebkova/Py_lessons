customers_string = '''
id,first_name,last_name,email,gender,ip_address
1,Rania,Andrichuk,randrichuk0@sina.com.cn,Female,126.245.12.84
2,Leola,O'Carroll,locarroll1@yahoo.co.jp,Female,227.67.176.74
3,Libbi,Stanner,lstanner2@bing.com,Female,198.53.118.19
4,Tracey,Caldeiro,tcaldeiro3@loc.gov,Male,4.214.3.211
5,Marnia,Beesley,mbeesley4@google.com,Female,2.52.219.173
6,Norry,Dalzell,ndalzell5@goo.ne.jp,Female,131.35.31.168
7,Clementius,Shipway,cshipway6@baidu.com,Male,51.143.228.172
8,Diena,Dymoke,ddymoke7@nature.com,Female,132.80.141.247
9,Maribelle,Hedworth,mhedworth8@qq.com,Female,229.72.101.234
10,Lindsy,Sire,lsire9@nifty.com,Female,25.235.88.187
'''
lines = customers_string.strip().split("\n")
headers = lines[0].split(",")

customers_dict = {}

for line in lines[1:]:
    values = line.split(",")
    row = {}
    for i in range(len(values)):
        row[headers[i]] = values[i]  # сохраняем все поля, включая ip_address
    customers_dict[values[5]] = row  # ключ верхнего словаря — ip_address

# Вывод
for ip in customers_dict:
    print(ip, ":", customers_dict[ip])
