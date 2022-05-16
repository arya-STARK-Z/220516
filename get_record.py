#基础工具
import json
import  urllib.request



def get_recordf(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json



