from napalm import get_network_driver

driver = get_network_driver('ios')
SW1 = driver('203.0.113.1','qytang','qytang')
SW1.open()
SW1.load_merge_candidate(filename='D:/PycharmProjects/Python之路/6.0第三方库/napalm/napalm_config.cfg')

biduidata = SW1.compare_config()
if len(biduidata) >0:
    print(biduidata)
    SW1.commit_config()
else:
    print('NO changes needed')
    SW1.discard_config()