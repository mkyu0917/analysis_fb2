from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN='EAACEdEose0cBAPiVNvFvexj7aOZAiStnfsCTuXj2pZCKOcdlEBwTSDzgTmpHl8mmAcV8tSnp7C32KhHFAcy9pm1ysIHCgAxXeN7jQOIPuqOk4IYHzZCafdIcjKa67VEgwF75bjNSbZAfymZBnoDG2YNIFj762XIIQAS0aeZABxCoXodOgCmUbEWu9an9q20G9jbC9JFh6kswZDZD'
BASE_URL_FB_API='https://graph.facebook.com/v3.0'

def fb_gen_url( #url을 만들어내는 함수,
    base ='https://graph.facebook.com/v3.0',
    node='',
    **params):
    url = '%s/%s/?%s' % (base, node , urlencode(params)) #url 규칙임, 주소마다 다름
    return url

def fb_name_to_id(pagename): #  node와 토큰을 받아서  json _ result 값을 받아서 id를 받아 오도록 파싱
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN) #url을 생성하는 함수에서 노드값에 pagename 과 토큰값을 받아서 출력
    print("까르르륵",url)
    json_result = json_request(url=url)
    return json_result.get('id') # 파싱에서 id값을 도출해서 리턴

def fb_limit_request(number='50'): #한번에 출력으로 받아올 값을 지정
        return number


def  fb_fetch_posts(pagename, since, until):
        pageid = fb_name_to_id(pagename)# pageid에 id값을 받아오는 함수값 할당

        #완전한 데이터를 받아오기 위해서 받아올 필드값과 기간, 갯수를 포함한 주
        url = fb_gen_url(
        node=pageid + '/posts',
        fields='id,message,link,name,type,shares,created_time,\
        reactions.limit(0).summary(true),\
        comments.limit(0).summary(true)',
        since=since,
        until=until,
        limit=fb_limit_request(),
        access_token=ACCESS_TOKEN)

        json_result = json_request(url=url)
        print('제이슨 결과값',json_result)


        hasnext = True # hasnext가 True 이면

        while hasnext is True:

            json_result = json_request(url=url)

            pages = None if json_result is None else json_result.get('paging') # result 값이 None이 아니면 page를 얻음
            data = None if json_result is None else json_result.get('data')  # result 값이 None이 아니면 data를 얻음
            next = None if json_result is None else json_result.get('next')

            url = None if pages is None else pages.get('next') # 제이슨리퀘스트 안에 필드값?
            hasnext = url is not None #None이 아니면 True 반환 None이면 False반환 루프탈출

            yield data #paging를 파싱해서 data에 접속하고 값을 받아온것을 지속적으로 전달.

