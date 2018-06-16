import sys
from urllib.request import Request, urlopen #url 요청하고 서버에서 데이터받아오는 라이브러리
from datetime import * #별표 다불러옴
import json


def json_request(
        url = 'https://graph.facebook.com/v3.0', #api주소 데이터가 들어있음
        encording = 'utf-8',#utf-8 로 변환해서 받아온다.
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()),file=sys.stderr)
        ):

    try:
        request = Request(url)  # api주소에 데이터를 요청함
        resp = urlopen(request) # api주소에서 데이터를 받아옴
        resp_body = resp.read().decode(encording) # api주소에서 받아온 풀어서 읽어옴

        json_result = json.loads(resp_body) #읽어온것을 python dict형식로드함
        print('%s: success for request[%s]' %(datetime.now(),url))

        if callable(success) is False: # 만약에 함수를 부를 수 있으면 false가 실행되고 json으로불러온 값이 리턴
            return json_result

        else:
            success(json_result) # 함수를 불렀으면 succss함수 매개변수에 json_result전달

    except Exception as e:          #try실행중에 에러가 발생하면 함수매개변수로 e전달
        if callable(error) is True:
                error(e)
