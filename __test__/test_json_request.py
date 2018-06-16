from collect.api import web_request as wr
url='http://ws.bus.go.kr/api/rest/busRouteInfo/getRoutePath?ServiceKey=EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D&_type=json&busRouteId=100100112'

def success_fetch_user_list(response): #web_request 파일에서 받은 json_result값을 매개변수로 받아옴.
    print(response)
    #success가 호출되었을때 매개변수인 response는 json_result값을 받음

def error_fetch_user_list(e): #wr에 있는 json_requset를 호출하고 , try 문에서 문제가 발생하면 e메세지 출력
    print(e)
    #success가 실행되지 않았을때 에러메세지 출력

wr.json_request(url=url, success=success_fetch_user_list, error=error_fetch_user_list)
# wr.json_request이 매개변수를 받음

