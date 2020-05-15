import json
s='''{"log":[
{"entry" :{ "id":"2"},
 "message" : "Application ended"},
 {"entry" :{ "id":"3"},
 "message" : "Application started"}]
 }
'''

def ids_by_message_j(json,str_to_search):
    l_to_ret=[]
    for i in js['log']:
       if i['message']==str_to_search:
        l_to_ret.append(i['entry']['id'])
    return l_to_ret
    
if __name__=='__main__":
    print(ids_by_message_j(js,"Application started"))
