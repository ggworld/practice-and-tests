import xml.etree.ElementTree as ET

my_xml='''<?xml version="1.0" encoding="UTF-8" ?>
<log>
 <entry id="1">
 <message>Application started</message>
 </entry>
 <entry id="2">
 <message>Application ended</message>
 </entry>
 <entry id="3">
 <message>Application ended</message>
 </entry>
 <entry id="4">
 <message>Application ended</message>
 </entry>
 <entry id="5">
 <message>Application ended</message>
 </entry>
</log>
'''

root = ET.fromstring(my_xml)

def ids_by_message(root,str_to_search):
    l_to_ret=[]
    for ent in root.findall('./entry'):
        if ent.find('./message').text==str_to_search:
            l_to_ret.append(ent.get('id'))
    return l_to_ret

if __name__=='__main__':
    print(ids_by_message(root,'Application started'))
