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

    # add_sum_info = dict_slice(dict_current_addr, 0, 7)
    # csv_file_name=current_path+"\\"+addr+"addr_sum_info.csv"
    #     # #print(csv_file_name)
    # pd_add_sum_info=pd.DataFrame(add_sum_info,index=[0])
    #     # print(pd_add_sum_info)
    # pd_add_sum_info_right=pd_add_sum_info.T
    # pd_add_sum_info_right.to_csv(csv_file_name)
        #  #pd_add_sum_info.to_csv(csv_file_name)

    current_addr_txs=dict_current_addr_obj.txs
    # df_tx = pd.DataFrame(current_addr_txs)
    # #print(df_tx)
    #     # print(df_tx)
    # df_tx_right = df_tx.T
    #     #print(df_tx_right)
    # current_addr_txs_filename=current_path+"\\"+addr+"all_txs_sum_info.csv"
    # df_tx_right.to_csv(current_addr_txs_filename)

    global df_all_inputs
    df1=pd.DataFrame()
    for item in current_addr_txs:
        # print("一个交易")
        # print(item)
        # print(type(item))
        current_addr_an_tx_obj = dict_to_object(item)
        current_addr_inputs = current_addr_an_tx_obj.inputs
        # print("一个交易里所有输出")
        # print(current_addr_inputs)
        # print(type(current_addr_inputs))

        global all_info_in_one_input
        result=[]
        df_all_sequence=pd.DataFrame()
        df2 = pd.DataFrame()
        for item in current_addr_inputs:
            #print("inputs里的东西")
            #print(item)
            #上面可以把inputs拆好了


            s = pd.Series(item)
            #s.index = [0]

            df2 = df2.append(s, ignore_index=True)
        df1=df1.append(df2,ignore_index=True)
    df1_right=df1.T
    filename=addr+"addr_all_inpust2.csv"
    df1_right.to_csv(filename)
        #     se_an_sequen_now = pd.Series(item)
        #     all_sequence=pd.Series()
        #     df_all_squence = pd.concat([se_an_sequen_now, all_sequence], axis=1)
        # print(df_all_squence)
        # df_all_squence.to_csv()



            # dict_an_sequen=dict(item)
            # print("一个inputs里的东西转字典")
            # print(dict_an_sequen)
            # print(type(dict_an_sequen))
        #     se_an_sequen=pd.Series(item)
        #
        #     result.append(item)
        # print("试试输出一个inputs所有内容")
        # print(result)
            # df_an_inputs_an_squence=pd.DataFrame(item)
            # all_info_in_one_input=pd.DataFrame(index=["sequence","witness","script","index","prev_out","spending_outpoints","addr"])
            # all_info_in_one_input=all_info_in_one_input.append(df_an_inputs_an_squence)
            # print("一个交易所有信息")
            # print(all_info_in_one_input)

            #("分隔")
    #     df_all_inputs=pd.DataFrame()
    #     df_all_inputs=df_all_inputs.append(all_info_in_one_input)
    # df_all_inputs_right=df_all_inputs.T
    # filename=addr+"test_whole_addr_inputs.csv"
    # df_all_inputs_right.to_csv(filename)
    #     df_current_addr_inputs = pd.DataFrame(current_addr_inputs)
    #     df_all_inputs1=pd.DataFrame()
    #     df_all_inputs=df_all_inputs1.append(df_current_addr_inputs)
    # print(df_all_inputs)
    # df_all_inputs_right=df_all_inputs.T
    # current_addr_inputs_filename = current_path + "\\" + addr + "try1_all_inputs_sum_info.csv"
    # df_all_inputs_right.to_csv(current_addr_inputs_filename)




        #result = pd.concat(frames)

        # df_current_addr_inputs_all = pd.DataFrame()
        # df_current_addr_inputs_all=df_current_addr_inputs_all.append(df_current_addr_inputs)
        # df_current_addr_inputs_all_right = df_current_addr_inputs_all.T
        # current_addr_inputs_filename = current_path + "\\" + addr + "try1_all_inputs_sum_info.csv"
        # df_current_addr_inputs_all_right.to_csv(current_addr_inputs_filename)
        #return df_prev_out_all_right


        # for i in current_addr_inputs:
        #       #print(i)
        #       #dct=list(i)
        #       current_inputdict_obj=dict_to_object(i)
        #       current_prevout=current_inputdict_obj.prev_out
        #       df_current_prev_out=pd.DataFrame(current_prevout)
        #       print(df_current_prev_out)#正常输出
        #       df_current_prev_out_right = df_current_prev_out.T
        #       current_prevout_filename = current_path + "\\" + addr + 'prev-out.csv'
        #
        #       #df_current_prev_out_right.to_csv(current_prevout_filename)
        #       # print("成功")
        #
        #       df_prev_out_all = df_prev_out_all.append(df_current_prev_out)
        # df_prev_out_all_right = df_prev_out_all.T
        # df_prev_out_all_right.to_csv(current_prevout_filename)

