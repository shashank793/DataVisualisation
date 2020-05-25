import re
import pprint
from datetime import datetime
import json
import collections
import csv

data_dict = {}

def data_handle():
    diag_report_data = []
    data = [['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/debreak_prem/debreak_prem_mask', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_2/rundir_1/MAP/Lolster/debreak_prem/debreak_prem_mask','abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/LL_pref', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/LL_lock', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/LL_flush', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/first_inv', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/LL_safe_ops', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/LL_safe_ops','abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_2/MAP/Lolster/lotsof/notinline', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/quentisential', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/sims_range', 'abc'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/lotsof/sims_range','xyz_12'],
            ['/random/dir_2/rundir_1_2017_09_05_13/Conf_1/rundir_1/MAP/Lolster/meme/waitrear_waitrearNonassigned_victor', 'abc'],
            ['/random/dir_2/rundir_1LX_2019_09_05_13/Conf_3/rundir_3/MAP/Lolster/meme/waitrear_waitrearNonassigned_victor','npm'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_2/MAP/Lolster/debreak_prem/debreak_prem_mask/t01/debreak_prem_mask','abc'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_2/MAP/Instagram/dragon_ball_z/t11/dragon_ball_z','xyz_12'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_2/MAP/Instagram/dragon_ball_z/t24/dragon_ball_z','xyz_12'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Instagram/dragon_ball_z/t22/dragon_ball_z','abc'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Instagram/dragon_ball_z/t30/dragon_ball_z','abc'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Instagram/dragon_ball_z/t31/dragon_ball_z','abc'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Instagram/dragon_ball_z/t32/dragon_ball_z','abc'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Instagram/dragon_ball_z/t25/dragon_ball_z','xyz_12'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Instagram/dragon_ball_z/t39/dragon_ball_z','xyz_12'],
            ['/random/dir_2/rundir_1_2017_12_15_14/Conf_1/rundir_3/MAP/Lolster/dragon_ball_z/t25/dragon_ball_z','xyz_12']]


    for i in data:
        row = i[0].split('/')

        proj_data = row[3].split('_',1)
        proj = proj_data[0]
        date = proj_data[1].strip('{0}'.format(proj))
        date = date[:-3]
        date = date.replace('_', '')
        date = datetime.strptime(date, '%Y%m%d').strftime('%d/%m/%Y')
        if row[-1] == row[-3]:
            del row[-1]
            x = len(row)
            diag_data = [proj,date, row[4], row[5], i[1],'/'.join(row[6:x - 1]), row[-1]]
        else:
            x = len(row)
            diag_data = [proj,date,row[4], row[5],i[1] ,'/'.join(row[6:x]),1]
        diag_report_data.append(diag_data)


    count = 1
    curr_key = 0
    comp_key = 0
    temp_x = []

    for curr_key in range(curr_key,len(diag_report_data)):
        if comp_key >= len(diag_report_data):
            break
        curr_key = comp_key
        comp_key += 1
        temp_count = count

        if len(temp_x) == 0:
            #print("\nIn len 0")
            pass
        else:
            #print("\nHi")
            makeDict(temp_x, temp_count)

        if curr_key < len(diag_report_data):
            x = diag_report_data[curr_key]
            temp_x = x
        
        if x[-1] == 1:
            continue
        else:
            count = 1
            length = len(diag_report_data)
            for comp_key in range(curr_key+1,length):
                y = diag_report_data[comp_key]
                if y[-1] == 1:
                    continue
                else:
                    if (x[0] == y[0]) and (x[1] == y[1]) and (x[2] == y[2]) and (x[3] == y[3]) and (x[4] == y[4]) and (x[5] == y[5]):
                        count += 1
                    else:
                        # print("breaking loop")
                        break


def makeDict(i,value):
    # print("\nHere Shashank ")
    # print("\nIn make dict : ",i)
    # print("\ncount : ",value)
    pattern = '^\w+$'
    key_1 = i[0]
    key_2 = i[1]
    key_3 = i[2]
    key_4 = i[3]
    key_5 = i[4]
    key_6 = i[5]
    try:
        if i[-1] != 1 and re.match(pattern, i[-1]):
            #print("Here \n")
            # value = 1
            try:
                if key_1 in data_dict.keys():

                    if key_2 in data_dict[key_1].keys():

                        if key_3 in data_dict[key_1][key_2].keys():

                            if key_4 in data_dict[key_1][key_2][key_3].keys():

                                if key_5 in data_dict[key_1][key_2][key_3][key_4].keys():

                                    if key_6 in data_dict[key_1][key_2][key_3][key_4][key_5].keys():
                                        data_dict[key_1][key_2][key_3][key_4][key_5][key_6].append(value)
                                    else:

                                        data_dict[key_1][key_2][key_3][key_4][key_5][key_6] = value
                                        # dict[key_1][key_2][key_3][key_4][key_5][key_6] = value

                                        # print(dict[key_1][key_2][key_3][key_4][key_5][key_6].values())
                                else:
                                    data_dict[key_1][key_2][key_3][key_4][key_5] = {key_6: value}
                                    # dict[key_1][key_2][key_3][key_4][key_5] = {key_6: value}
                            else:
                                data_dict[key_1][key_2][key_3][key_4] = {key_5: {key_6: value}}
                                # dict[key_1][key_2][key_3][key_4] = {key_5: {key_6: value}}
                        else:
                            data_dict[key_1][key_2][key_3] = {key_4: {key_5: {key_6: value}}}
                            # dict[key_1][key_2][key_3] = {key_4: {key_5: {key_6: value}}}
                    else:
                        data_dict[key_1][key_2] = {key_3: {key_4: {key_5: {key_6: value}}}}
                        # dict[key_1][key_2] = {key_3: {key_4: {key_5: {key_6: value}}}}

                else:
                    data_dict[key_1] = {key_2: {key_3: {key_4: {key_5: {key_6: value}}}}}
                    # dict[key_1] = {key_2: {key_3: {key_4: {key_5: {key_6: value}}}}}

            except AttributeError or TypeError or ValueError:
                print("\nError Key Value Pair\n")
                pass
        else:
            # value = 1
            try:
                if key_1 in data_dict.keys():
                    if key_2 in data_dict[key_1].keys():
                        if key_3 in data_dict[key_1][key_2].keys():
                            if key_4 in data_dict[key_1][key_2][key_3].keys():
                                if key_5 in data_dict[key_1][key_2][key_3][key_4].keys():
                                    if key_6 in data_dict[key_1][key_2][key_3][key_4][key_5].keys():
                                        data_dict[key_1][key_2][key_3][key_4][key_5][key_6] = 1
                                    else:
                                        data_dict[key_1][key_2][key_3][key_4][key_5][key_6] = 1
                                else:
                                    data_dict[key_1][key_2][key_3][key_4][key_5] = {key_6: 1}
                            else:
                                data_dict[key_1][key_2][key_3][key_4] = {key_5: {key_6: 1}}
                        else:
                            data_dict[key_1][key_2][key_3] = {key_4: {key_5: {key_6: 1}}}
                    else:
                        data_dict[key_1][key_2] = {key_3: {key_4: {key_5: {key_6: 1}}}}
                else:
                    data_dict[key_1] = {key_2: {key_3: {key_4: {key_5: {key_6: 1}}}}}

            except AttributeError or TypeError or ValueError:
                print("\nError Key Value Pair\n")
                pass

    except TypeError:
        pass


def create_list(dict_top):
    local_list = []
    for key in data_dict:
        for key_1 in data_dict[key]:
            for key_2 in data_dict[key][key_1]:
                for key_3 in data_dict[key][key_1][key_2]:
                    for key_4 in data_dict[key][key_1][key_2][key_3]:
                        for key_5 in data_dict[key][key_1][key_2][key_3][key_4]:
                            list = [key,key_1,key_2,key_3,key_4,key_5,data_dict[key][key_1][key_2][key_3][key_4][key_5]]
                            local_list.append(list)

    return local_list

if __name__ == "__main__":
    data_handle()
    list = create_list(data_dict)
    header = ['project', 'date', 'config', 'rundir', 'flow_name', 'diag', 'num_of_clones']
    with open('GraphVisualisationLearning\/ConfigData.csv','w',newline='') as f:
        writer = csv.writer(f,delimiter = ',')
        writer.writerow(header)
        for i in list:
            writer.writerow(i)
