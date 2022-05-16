#这个的url是靠列表传参的
import time

import get_record



def get_an_addr_sum_2(url):

    dict_addr_sum=get_record.get_recordf(url)
    time.sleep(40)
    return dict_addr_sum