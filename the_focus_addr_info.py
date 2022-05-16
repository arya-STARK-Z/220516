import get_org_dic


import os

import pandas as pd

#df_prev_out_all=pd.DataFrame()


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
    global df_prev_out_all

    global df_prev_out_all_right
    df_prev_out_all_right=pd.DataFrame()
    global  df_current_addr_inputs_all
    df_current_addr_inputs_all=pd.DataFrame()
    global addr
    addr=get_org_dic.return_addr()  # 地址 用来写文件名的
    global path
    path="E:\\hj\\ex\\python2\\cnn data process\\0515 mutli\\"
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
        # #print(csv_file_name)
    pd_add_sum_info=pd.DataFrame(add_sum_info,index=[0])
        # print(pd_add_sum_info)
    pd_add_sum_info_right=pd_add_sum_info.T
    pd_add_sum_info_right.to_csv(csv_file_name)
        #  #pd_add_sum_info.to_csv(csv_file_name)

    current_addr_txs=dict_current_addr_obj.txs
    df_tx = pd.DataFrame(current_addr_txs)
    print(df_tx)
        # print(df_tx)
    df_tx_right = df_tx.T
        #print(df_tx_right)
    current_addr_txs_filename=current_path+"\\"+addr+"all_txs_sum_info.csv"
    df_tx_right.to_csv(current_addr_txs_filename)


    for item in current_addr_txs:
        current_addr_an_tx_obj = dict_to_object(item)
        current_addr_inputs = current_addr_an_tx_obj.inputs
        df_current_addr_inputs = pd.DataFrame(current_addr_inputs)
        df_current_addr_inputs_all = pd.DataFrame()
        df_current_addr_inputs_all=df_current_addr_inputs_all.append(df_current_addr_inputs)

        for i in current_addr_inputs:
              #print(i)
              #dct=list(i)
              current_inputdict_obj=dict_to_object(i)
              current_prevout=current_inputdict_obj.prev_out
              df_current_prev_out=pd.DataFrame(current_prevout)
              print(df_current_prev_out)#正常输出
              df_current_prev_out_right = df_current_prev_out.T
              current_prevout_filename = current_path + "\\" + addr + 'prev-out.csv'

              #df_current_prev_out_right.to_csv(current_prevout_filename)
              # print("成功")

              df_prev_out_all = df_prev_out_all.append(df_current_prev_out)
        df_prev_out_all_right = df_prev_out_all.T
        df_prev_out_all_right.to_csv(current_prevout_filename)

    df_current_addr_inputs_all_right = df_current_addr_inputs_all.T
    current_addr_inputs_filename = current_path + "\\" + addr + "try1_all_inputs_sum_info.csv"
    df_current_addr_inputs_all_right.to_csv(current_addr_inputs_filename)
    return df_prev_out_all_right

def get_all_addr_related_2_focus_addr():
    addr_all = try1().iloc[7]
    # print(addr_all)
    addr_all_list = list(addr_all)
    print(addr_all_list)
    print(type(addr_all_list))
    #看看要不要输出CSV,直接读列表也行啊
    return addr_all_list#返回关心地址涉及的所有地址






 #       for item in current_addr_txs:
 #         current_addr_an_tx_obj=dict_to_object(item)
  #        current_addr_inputs=current_addr_an_tx_obj.inputs
 #         df_current_addr_inputs=pd.DataFrame(current_addr_inputs)
  #        df_current_addr_inputs_right=df_current_addr_inputs.T
  #        current_addr_inputs_filename=current_path+"\\"+current_addr+"try1_all_inputs_sum_info.csv"
 #         df_current_addr_inputs_right.to_csv(current_addr_inputs_filename)



       #创建文件夹模块
       # try:
        #    if not os.path.exists(current_path):
        #     os.mkdir(current_path)
       # except:
         #   print("文件夹创建出错")

  #写地址总数据CSV模块
       # dict_current_addr=get_org_dic.get_an_addr_sum_2(current_url)
       # add_sum_info = dict_slice(dict_current_addr, 0, 7)
       # csv_file_name=current_path+'\\'+current_addr+'addr_sum_info.csv'
       # #print(csv_file_name)
      #  pd_add_sum_info=pd.DataFrame(add_sum_info,index=[0])
        #print(pd_add_sum_info)
       # pd_add_sum_info_right=pd_add_sum_info.T
       # pd_add_sum_info_right.to_csv(csv_file_name)
      #  #pd_add_sum_info.to_csv(csv_file_name)






