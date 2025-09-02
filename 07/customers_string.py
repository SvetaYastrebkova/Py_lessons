customers_string = ''' id,first_name,last_name,email,gender,ip_address 1,Rania,Andrichuk,randrichuk0@sina.com.cn,Female,126.245.12.84 2,Leola,O'Carroll,locarroll1@yahoo.co.jp,Female,227.67.176.74 3,Libbi,Stanner,lstanner2@bing.com,Female,198.53.118.19 4,Tracey,Caldeiro,tcaldeiro3@loc.gov,Male,4.214.3.211 5,Marnia,Beesley,mbeesley4@google.com,Female,2.52.219.173 6,Norry,Dalzell,ndalzell5@goo.ne.jp,Female,131.35.31.168 7,Clementius,Shipway,cshipway6@baidu.com,Male,51.143.228.172 8,Diena,Dymoke,ddymoke7@nature.com,Female,132.80.141.247 9,Maribelle,Hedworth,mhedworth8@qq.com,Female,229.72.101.234 10,Lindsy,Sire,lsire9@nifty.com,Female,25.235.88.187 '''

def convert_str_list(csv_string: str) -> list[list[str]]:
    # убираем пустые строки и пробелы
    lines = [line.strip() for line in csv_string.strip().splitlines() if line.strip()]
    # превращаем каждую строку в список значений
    return [line.split(",") for line in lines]

# Применение
list1 = convert_str_list(customers_string)

# Проверка
for row in list1:
    print(row)
