import json
from urllib.request import urlopen
import datetime

# 内閣府公式から
link = "https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv"

def lambda_handler(event, context):
    # TODO implement
    
    f = urlopen(link)
    content = f.read()
    
    print(content)
    
    print("test")
    
    decoded = content.decode("shift_jis").split()
    
    # print(decoded)
    
    # print(decoded[0:2])
    
    dic = {}
    
    for i in decoded:
        key, val = i.split(',')
        dic[key] = val
    print(dic)
    
    date_now = datetime.datetime.now()
    
    thisyear = date_now.year
    
    years_list = [thisyear - 2, thisyear - 1, thisyear, thisyear + 1, thisyear + 2]
    
    dic_years = {}
    
    for key, val in dic.items():
        for y in years_list:
            if(str(y) in key):
                print("------------")
                print(key)
                print(val)
                print(f"{y}")
                print("------------")
                dic_years[key] = val
                
    print(dic_years)
    
    return {
        'statusCode': 200,
        'body': json.dumps(dic_years, ensure_ascii=False)
    }
