import get_org_dic


import os

import pandas as pd




def dict_slice(adict, start, end):
    keys = adict.keys()
    dict_slice = {}
    for k in list(keys)[start:end]:
        dict_slice[k] = adict[k]
    return dict_slice

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = Dict()
    for k, v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst


def try1():
    df_a_prevout = pd.DataFrame()

    df_prev_out_right = pd.DataFrame()
    global df_prev_out_all

    global df_prev_out_all_right
    df_prev_out_all_right=pd.DataFrame()
    global  df_current_addr_inputs_all
    df_current_addr_inputs_all=pd.DataFrame()
    global addr
    addr=get_org_dic.return_addr()  # 地址 用来写文件名的
    global path
    path="E:\\hj\\ex\\python2\\cnn data process\\0515 mutli"
    global current_path
    current_path=path+"\\"+addr
    try:
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    except:
       print("文件夹创建出错")


    dict_current_addr = get_org_dic.get_an_addr_sum()
    dict_current_addr_obj=dict_to_object(dict_current_addr)

    add_sum_info = dict_slice(dict_current_addr, 0, 7)
    csv_file_name=current_path+"\\"+addr+"addr_sum_info.csv"

    pd_add_sum_info=pd.DataFrame(add_sum_info,index=[0])

    pd_add_sum_info_right=pd_add_sum_info.T
    pd_add_sum_info_right.to_csv(csv_file_name)

    current_addr_txs=dict_current_addr_obj.txs
    df_tx = pd.DataFrame(current_addr_txs)

    df_tx_right = df_tx.T

    current_addr_txs_filename=current_path+"\\"+addr+"all_txs_sum_info.csv"
    df_tx_right.to_csv(current_addr_txs_filename)

    global df_all_inputs
    df1=pd.DataFrame()
    df_one_input_preout = pd.DataFrame()
    #df_a_prevout = pd.DataFrame()
    for item in current_addr_txs:

        current_addr_an_tx_obj = dict_to_object(item)
        current_addr_inputs = current_addr_an_tx_obj.inputs


        global all_info_in_one_input
        result=[]
        df_all_sequence=pd.DataFrame()
        df2 = pd.DataFrame()


        for item in current_addr_inputs:
            #print("inputs里的东西")
            #print(item)
            s = pd.Series(item)
            #df2 = df2.append(s, ignore_index=True)
            df1 = df1.append(s, ignore_index=True)


            #上面可以把inputs拆好了
            dict_an_input_obj=dict_to_object(item)




            an_prev_out=dict_an_input_obj.prev_out
           # print(an_prev_out)
            dict_an_prev_out=dict(an_prev_out)
            s_a_prev_out=pd.Series(dict_an_prev_out)
            df_a_prevout=df_a_prevout.append(s_a_prev_out,ignore_index=True)


    df1_right = df1.T
    all_inputs_filename =current_path+"\\"+ addr + "addr_all_inpust.csv"
    df1_right.to_csv(all_inputs_filename)


    df_prev_out_right=df_a_prevout.T
    prev_out_filename=current_path+"\\"+addr+"prev_out.csv"
    df_prev_out_right.to_csv(prev_out_filename)
    return df_prev_out_right

def get_pre_out_addr():
    addr_all = try1().iloc[7]
    # print(addr_all)
    addr_all_list = list(addr_all)
    print(addr_all_list)
    print(type(addr_all_list))
    # 看看要不要输出CSV,直接读列表也行啊
    return addr_all_list  # 返回关心




