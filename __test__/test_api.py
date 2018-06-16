from collect.api import api

url= api.fb_gen_url( #url메소드 호출후 return 값 확인
                    'https://graph.facebook.com/v3.0', # 기본  api url
                    node='',  # pagename
                    a=10,b=20 # **param
                   )

print(url)

url2 = api.fb_name_to_id('leagueoflegends') # 노드값을 넣어서 주소값 출력
print(url2)


for data in api.fb_fetch_posts('leagueoflegends','2017-01-01','2017-12-31'):
    print(data)