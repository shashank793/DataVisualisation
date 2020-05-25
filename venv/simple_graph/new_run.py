import mysql.connector
# import pprint
# import json
import csv


def connect():
    # mydb = mysql.connector.connect(
    #     host='',
    #     user='',
    #     passwd='',
    #     database=''
    # )
    #
    # mycursor = mydb.cursor()
    #
    # query1 = "select * from <table_name> where <condition> regexp binary ('<somestring>') limit 20"
    #
    # mycursor.execute(query1)
    #
    # get_date = []
    #
    # date = mycursor.fetchall()
    #
    # for i in date:
    #     t = i[1]
    #     get_date.append(t)
    #
    # # print(get_date)
    #
    # get_data = []
    #
    # for regress_date in get_date:
    #     mycursor.execute("select <column_1>,<column_2> from <table_name_2> where <condition> regexp binary ('{0}') limit 200".format('<somestring>'))
    #     for row in mycursor:
    #         diag_report = [row[0],row[1]]
    #         get_data.append(diag_report)
    #
    # # get_data = [['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/rundir_1/somestring.1234', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/abc.18_09_27_08_11_14_9225/sdjskldfjlsdkf.72407941', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/jkklksdjl.1801530891', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/lm_cacheOp_nonshare.338542882', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/jkklksdjl.830907331', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.486139676', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.763695022', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.934571762', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1962628155', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1283571447', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.191048937', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.2031314760', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.302512185', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.2001347714', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.418189006', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1222852619', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1516334821', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.617764484', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.437411102', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1663978629', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1281928660', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1826043304', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.1188901547', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.270810527', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/l2_perf_counter_coreid_variation.473838680', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.933176599', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.1659278116', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.762266341', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.325344574', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.1134991335', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.106322536', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.1985939939', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.911247093', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.1663180499', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_all_readshared.108432010', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_readshared.839582839', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_readshared.2136135721', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_readshared.1851883502', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_readshared.1469337946', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_cleanunique.1261561193', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_cleanunique.1537648339', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_cleanunique.1390017694', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeback.751875638', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeback.1335514331', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeback.893550005', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeback.61037170', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeback.1235384310', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.1146731115', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.671397669', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.49854513', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.2140184946', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.228066516', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.1753749242', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.282568531', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.1666592998', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.381146902', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.369132766', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.1119580922', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.419340714', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.59056825', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeclean.594628045', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random.663942128', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random.1235351593', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random.1953837103', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random.1139533766', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random.1079079992', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.1885515047', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.1178716158', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random.651704443', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.1558470458', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.1260302875', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.2068145284', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.478971456', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.1826314529', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_random_ram.1050684495', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_writeunique.1655135020', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_cleanunique_l2miss_allway_occupied.871760973', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.140283950', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.709634752', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.506633432', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.615232025', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1718134242', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1543350330', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1404270731', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.716952360', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1025364138', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.796908803', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1873172993', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1050575663', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.491984553', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1556477361', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.585605374', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_l1cacheop.366484471', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/coherent_ctrl_reg.1352338795', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/cache_aware_l1cacheop.2016099640', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/lsnldjflkdjlk.1142194850', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/lsnldjflkdjlk.782265908', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/lsnldjflkdjlk.868979374', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/lsnldjflkdjlk.1604671427', '"LLone"'], ['/abc/proj_awara/user1/somedir/proj_1/proj1_2018_09_27_06_00_02/conf_1/LLone.18_09_27_08_11_14_9225/lsnldjflkdjlk.198164842', '"LLone"']]
    #
    # diag_report = []
    #
    # proj = 'proj_1'
    # for i in get_date:
    #     for j in get_data:
    #         if i in j[-2]:
    #             # print("here")
    #             seq = j[-2].split('/')
    #             seq = seq[-1]
    #             clone = seq.split('.')
    #             sequence = clone[0]
    #             seed = clone[1]
    #             str = i.strip('proj_1_')
    #             str = str.split('_',3)
    #             time = str[3].replace('_','')
    #             date_time = str[2]+'/'+str[1]+'/'+str[0]
    #             data = [proj,date_time,time,sequence,seed]
    #             diag_report.append(data)

    diag_report = [['proj_1', '27/09/2018', '060002', 'sdskslkj', '543289057'], ['proj_1', '27/09/2018', '060002', 'mnbdvkjd', '72407941'], ['proj_1', '27/09/2018', '060002', 'jkklksdjl', '1801530891'],]

    return diag_report

def createDict(diag_report):
    dict = {}
    for i in diag_report:
        # print(i)
        key = i[0]
        key_1 = i[1]
        key_2 = i[2]
        key_3 = i[3]
        value = i[4]
        try :
            if key in dict.keys():
                if key_1 in dict[key].keys():
                    if key_2 in dict[key][key_1].keys():
                        if key_3 in dict[key][key_1][key_2].keys():
                            dict[key][key_1][key_2][key_3].append(value)
                        else:
                            dict[key][key_1][key_2][key_3] = [value]
                    else:
                        dict[key][key_1][key_2] = {key_3:[value]}
                else:
                    dict[key][key_1] = {key_2 : {key_3 : [value]}}
            else:
                dict[key] = {key_1 : {key_2 : {key_3 : [value]}}}

        except ValueError:
            print("Failed")
    return  dict
    # app_json = json.dumps(dict)
    # return app_json
    # print(app_json)

def createRevDict(diag_report):
    rev_dict = {}
    for i in diag_report:
        key = i[0]
        key_1 = i[-2]
        key_2 = i[1]
        key_3 = i[-1]
        value = i[2]
        try :
            if key in rev_dict.keys():
                if key_1 in rev_dict[key].keys():
                    if key_2 in rev_dict[key][key_1].keys():
                        if key_3 in rev_dict[key][key_1][key_2].keys():
                            rev_dict[key][key_1][key_2][key_3].append(value)
                        else:
                            rev_dict[key][key_1][key_2][key_3] = value
                    else:
                        rev_dict[key][key_1][key_2] = {key_3:value}
                else:
                    rev_dict[key][key_1] = {key_2 : {key_3 : value}}
            else:
                rev_dict[key] = {key_1 : {key_2 : {key_3 : value}}}

        except ValueError:
            print("Failed")
    return rev_dict
    # app_json = json.dumps(rev_dict)
    # print(app_json)

def create_list(data_dict):
    local_list = []
    for key in data_dict:
        for key_1 in data_dict[key]:
            for key_2 in data_dict[key][key_1]:
                for key_3 in data_dict[key][key_1][key_2]:
                            list = [key,key_1,key_2,key_3,data_dict[key][key_1][key_2][key_3]]
                            local_list.append(list)
    # print(local_list)
    return local_list

def create_diag_CSV(list):
    local_list = []
    for i in list:
        temp_list = [i[0],i[1],i[2],i[3],i[4],len(i[4])]
        local_list.append(temp_list)
    # print(local_list)
    header = ['project', 'date', 'time_stamp', 'sequence', 'seed','seed_count']
    with open('GraphVisualisationLearning\/diag_data.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for i in local_list:
            writer.writerow(i)

def create_seed_CSV(list):
    header = ['project', 'sequence', 'date', 'seed', 'time']
    with open('GraphVisualisationLearning\/seed_data.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for i in list:
            writer.writerow(i)


if __name__ == "__main__":

    diag_data = connect()
    diag_dict = createDict(diag_data)
    seed_dict = createRevDict(diag_data)

    diag_list = create_list(diag_dict)
    seed_list = create_list(seed_dict)

    create_diag_csv = create_diag_CSV(diag_list)
    create_seed_csv = create_seed_CSV(seed_list)



