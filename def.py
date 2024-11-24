def send_request(args):
    url , params , body = args
    print (url,params,body)
send_request(["https://" , {"a": 1} , "dsdsds"])
    