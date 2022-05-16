import get_multi_org_dict
import get_org_dic
import get_record
import the_focus_addr_info
import pandas as pd
import os


global current_addr
global current_path

#df_prev_out_all=pd.DataFrame()


focus_addr = get_org_dic.return_addr()

list_all_addr1 = the_focus_addr_info.get_all_addr_related_2_focus_addr()
list_all_addr = list(set(list_all_addr1))  # 用一下集合的唯一性

the_focus_addr_info.try1()

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
    for i in list_all_addr:
        current_addr = i;
        url = " https://blockchain.info/rawaddr/"
        current_url = url + current_addr
        print(current_url)
        #path1 = "E:\\hj\\ex\\python2\\cnn data process\\0515 mutli"
        path1 = "E:\\hj\\ex\\ython2\\cnn data process\\0515 mutli\\"

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

        dict_current_addr = get_multi_org_dict.get_an_addr_sum_2(current_url)
        dict_current_addr_obj = dict_to_object(dict_current_addr)

        add_sum_info = dict_slice(dict_current_addr, 0, 7)
        csv_file_name = current_path + "\\" + current_addr + "addr_sum_info.csv"
        # #print(csv_file_name)
        pd_add_sum_info = pd.DataFrame(add_sum_info, index=[0])
        # print(pd_add_sum_info)
        pd_add_sum_info_right = pd_add_sum_info.T
        pd_add_sum_info_right.to_csv(csv_file_name)
        #  #pd_add_sum_info.to_csv(csv_file_name)

        current_addr_txs = dict_current_addr_obj.txs
        df_tx = pd.DataFrame(current_addr_txs)
        # print(df_tx)
        df_tx_right = df_tx.T
        # print(df_tx_right)
        current_addr_txs_filename = current_path + "\\" + current_addr + "all_txs_sum_info.csv"
        df_tx_right.to_csv(current_addr_txs_filename)

        for item in current_addr_txs:
            current_addr_an_tx_obj = dict_to_object(item)
            current_addr_inputs = current_addr_an_tx_obj.inputs
            df_current_addr_inputs = pd.DataFrame(current_addr_inputs)
            df_current_addr_inputs_right = df_current_addr_inputs.T
            current_addr_inputs_filename = current_path + "\\" + current_addr + "try1_all_inputs_sum_info.csv"
            df_current_addr_inputs_right.to_csv(current_addr_inputs_filename)
            for i in current_addr_inputs:
                # print(i)
                # dct=list(i)
                current_inputdict_obj = dict_to_object(i)
                current_prevout = current_inputdict_obj.prev_out
                df_current_prev_out = pd.DataFrame(current_prevout)
                #df_current_prev_out_right = df_current_prev_out.T
                current_prevout_filename = current_path + "\\" + current_addr + 'prev-out.csv'
                #df_current_prev_out_right.to_csv(current_prevout_filename)
                print("成功")
                df_prev_out_all = df_prev_out_all.append(df_current_prev_out)
            df_prev_out_all_right = df_prev_out_all.T
            df_prev_out_all_right.to_csv(current_prevout_filename)
            #return df_prev_out_all_right

            # df_prev_out_all = df_prev_out_all.append(df_current_prev_out)
                # df_prev_out_all_right=df_prev_out_all.T
