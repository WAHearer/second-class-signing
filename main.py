import requests
import json
import time
urlForQuery='https://young.ustc.edu.cn/login/wisdom-group-learning-bg/mobile/item/enrolmentList'
headers={
    'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlBCMjMwMDAyNTMifQ.LMt-fqc2kijbgtmWVRO4YRCv8AyrVrwR11IUSDp-aDQ'
}
response=requests.get(url=urlForQuery,headers=headers,verify=False).json()
for course in response['result']['records']:
    urlForSign='https://young.ustc.edu.cn/login/wisdom-group-learning-bg/mobile/item/enter/'+course['id']
    headersForSign={
        'Content-type':'application/json;charset=UTF-8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275',
        'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlBCMjMwMDAyNTMifQ.LMt-fqc2kijbgtmWVRO4YRCv8AyrVrwR11IUSDp-aDQ'
    }
    json={}
    requests.post(url=urlForSign,headers=headersForSign,json=json,verify=False)

urlForAppealList='https://young.ustc.edu.cn/login/wisdom-group-learning-bg/mobile/item/publicItem'
params={
    'disPlayInPublicPeriod':'1'
}
response=requests.get(url=urlForAppealList,headers=headers,params=params,verify=False).json()
for course in response['result']['records']:
    urlForAppeal='https://young.ustc.edu.cn/login/wisdom-group-learning-bg/item/appeal/add'
    json={            #可以自行添加证据图片
        'appealType':'add_hours',
        'appealTypeName':'学时添加',
        'reason':'二课小程序出错无法签到',
        'personList':[{'userName':'张天赫','userCode':'PB23000253','checked':True}],
        'itemId':course['id']
    }
    requests.post(url=urlForAppeal,headers=headers,json=json,verify=False)
    time.sleep(3)