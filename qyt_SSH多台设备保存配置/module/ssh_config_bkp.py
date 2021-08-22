from _datetime import datetime
date = datetime.now()
date1 = str(date)[0:16]
date1 = date1.replace(' ','_')
date1 =date1.replace(':','_')
# print(date1)
def config_bkp(namet,configt):
    config = open('e:/Cisco/python/'+ namet+'_'+date1+ '.txt',mode='w+')
    config.write(configt)
    config.close()
    print(namet + ' config backup finished')