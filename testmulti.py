import get_multi_org_dict
import get_org_dic

import pandas as pd
import os

import test_main_add_feed

global current_addr
global current_path




focus_addr = get_org_dic.return_addr()

test_main_add_feed.try1()

list_all_addr1 = test_main_add_feed.get_pre_out_addr()
list_all_addr = list(set(list_all_addr1))  # 用一下集合的唯一性


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
    for i in list_all_addr:
        current_addr = i;
        url = " https://blockchain.info/rawaddr/"
        current_url = url + current_addr
        print(current_url)
        #path1 = "E:\\hj\\ex\\python2\\cnn data process\\0515 mutli"

        #文件夹名漏了一个p,不过成功在输出名字的文件夹下输出了
        path1 = "E:\\hj\\ex\\ython2\\cnn data process\\0515 mutli"+"\\"

        path2 = current_addr
        #current_path = path1 + focus_addr + "\\" + path2
        current_path=path1+focus_addr+"\\"+path2
        #os.makedirs(current_path)
        try:
          if not os.path.exists(current_path):
              os.makedirs(current_path)
              #os.mkdir(current_path)
        except:
          print("文件夹创建出错")

        dict_current_addr =get_multi_org_dict.get_an_addr_sum_2(current_url)
        dict_current_addr_obj = dict_to_object(dict_current_addr)

        add_sum_info = dict_slice(dict_current_addr, 0, 7)
        csv_file_name = current_path + "\\" + current_addr + "addr_sum_info.csv"

        pd_add_sum_info = pd.DataFrame(add_sum_info, index=[0])

        pd_add_sum_info_right = pd_add_sum_info.T
        pd_add_sum_info_right.to_csv(csv_file_name)

        current_addr_txs = dict_current_addr_obj.txs
        df_tx = pd.DataFrame(current_addr_txs)

        df_tx_right = df_tx.T

        current_addr_txs_filename = current_path + "\\" + current_addr + "all_txs_sum_info.csv"
        df_tx_right.to_csv(current_addr_txs_filename)

        global df_all_inputs
        df1 = pd.DataFrame()
        df_one_input_preout = pd.DataFrame()
        # df_a_prevout = pd.DataFrame()
        for item in current_addr_txs:

            current_addr_an_tx_obj = dict_to_object(item)
            current_addr_inputs = current_addr_an_tx_obj.inputs

            global all_info_in_one_input
            result = []
            df_all_sequence = pd.DataFrame()
            df2 = pd.DataFrame()

            for item in current_addr_inputs:
                # print("inputs里的东西")
                # print(item)
                s = pd.Series(item)
                # df2 = df2.append(s, ignore_index=True)
                df1 = df1.append(s, ignore_index=True)

                # 上面可以把inputs拆好了
                dict_an_input_obj = dict_to_object(item)

                an_prev_out = dict_an_input_obj.prev_out
                # print(an_prev_out)
                dict_an_prev_out = dict(an_prev_out)
                s_a_prev_out = pd.Series(dict_an_prev_out)
                df_a_prevout = df_a_prevout.append(s_a_prev_out, ignore_index=True)

        df1_right = df1.T
        all_inputs_filename = current_path + "\\" + current_addr + "addr_all_inpust.csv"
        df1_right.to_csv(all_inputs_filename)

        df_prev_out_right = df_a_prevout.T
        prev_out_filename = current_path + "\\" + current_addr + "prev_out.csv"
        df_prev_out_right.to_csv(prev_out_filename)