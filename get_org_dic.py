#基础工具
import time

import get_record


addr="1MfLPJxzyDZr33WK79BKzAqsuvFnzi9TK1"

url="https://blockchain.info/rawaddr/"+addr
#返回一个地址的原始数据
#url="https://blockchain.info/rawaddr/12DA8mpQCnTB1cEHLPFU7ckP44zN5Xmgu3“
#https://blockchain.info/rawaddr/1MfLPJxzyDZr33WK79BKzAqsuvFnzi9TK1
def get_an_addr_sum():

    dict_addr_sum=get_record.get_recordf(url)
    time.sleep(30)
    return dict_addr_sum

def return_addr():
    addr1=addr
    return addr1