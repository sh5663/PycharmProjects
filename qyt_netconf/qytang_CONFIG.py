# IOS-XE native 的XML数据，创建环回口、配置描述、配置IP地址
CONFIG0 = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>0</name>
        <description>netconf_configed</description>
        <shutdown xc:operation="remove"/>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# IOS-XE native 的XML数据，修改环回口、shutdown、删除IP地址
CONFIG1 = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>0</name>
        <description>netconf_configed</description>
        <shutdown xc:operation="merge"/>
        <ip>
          <address>
            <primary xc:operation="delete"/>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

#思科 ietf-interface 为设备配置环回口及IP地址
CONFIG2 = """<config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>Loopback0</name>
          <description xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">dashu666 wa</description>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">ianaift:softwareLoopback</type>
          <enabled xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">true</enabled>
          <link-up-down-trap-enable xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">enabled</link-up-down-trap-enable>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
              <ip>1.1.1.1</ip>
              <netmask xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">255.255.255.255</netmask>
            </address>
          </ipv4>
        </interface>
      </interfaces>
    </config>"""

#CE12800的XML数据，切换为三层接口、添加描述、配置接口IP地址
CONFIG3 = '''<config>
      <ethernet xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <ethernetIfs>
          <ethernetIf operation="merge">
            <ifName>GE1/0/2</ifName>
            <l2Enable>disable</l2Enable>
          </ethernetIf>                   
        </ethernetIfs>
      </ethernet>
      <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <interfaces>
          <interface>
            <ifName>GE1/0/2</ifName>
            <ifDescr>Config by NETCONF</ifDescr>
            <ifmAm4>
              <am4CfgAddrs>
                <am4CfgAddr operation="remove">   <!-- CE要求必须先删除main地址，而且必须填写正确原来的地址信息 -->
                  <addrType>main</addrType>
                  <ifIpAddr>123.45.67.89</ifIpAddr>
                </am4CfgAddr>
                <am4CfgAddr operation="merge">
                  <subnetMask>255.255.255.0</subnetMask>
                  <addrType>main</addrType>
                  <ifIpAddr>2.2.33.3</ifIpAddr>
                </am4CfgAddr>
              </am4CfgAddrs>
            </ifmAm4>
          </interface>
        </interfaces>
      </ifm>
    </config>'''

#CE12800的XML数据，创建环回口，配置IP地址
CONFIG4 = """<config>
<ifm content-version="1.0" format-version="1.0" xmlns="http://www.huawei.com/netconf/vrp">
<interfaces>
<interface>
<ifName>loopback0</ifName>
<ifmAm4>
<am4CfgAddrs>
<am4CfgAddr operation="merge">
<ifIpAddr>22.22.22.22</ifIpAddr>
<subnetMask>255.255.255.255</subnetMask>
<addrType>main</addrType>
</am4CfgAddr>
</am4CfgAddrs>
</ifmAm4>
</interface>
</interfaces>
</ifm>
    </config>
"""

#CE12800的XML数据，配置OSPF
CONFIG5 = """<config>
      <ospfv2 xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <ospfv2comm>
          <ospfSites>
            <ospfSite>
              <processId>1</processId>
              <areas>
                <area>
                  <areaId>0.0.0.0</areaId>
                  <interfaces>
                    <interface operation="merge">
                      <ifName>GE1/0/0</ifName>
                      <configCost>10</configCost>
                      <networkType>broadcast</networkType>
                    </interface>
                    <interface operation="merge">
                      <ifName>LoopBack0</ifName>
                    </interface>
                  </interfaces>
                </area>
              </areas>
            </ospfSite>
          </ospfSites>
        </ospfv2comm>
      </ospfv2>
    </config>"""

#IOS-XE native 的XML数据，配置OSPF
CONFIG6 = """<config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <ospf>
              <process-id>
                <id>1</id>
              </process-id>
            </ospf>
          </router-ospf>
        </router>
        <interface>
          <GigabitEthernet>
            <name>1</name>
            <ip>
              <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <ospf>
                  <process-id>
                    <id>1</id>
                    <area>
                      <area-id>0</area-id>
                    </area>
                  </process-id>
                  <network>
                    <broadcast xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
                  </network>
                  <priority>255</priority>
                </ospf>
              </router-ospf>
            </ip>
          </GigabitEthernet>
          <Loopback>
            <name>0</name>
            <ip>
              <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <ospf>
                  <process-id>
                    <id>1</id>
                    <area>
                      <area-id>0</area-id>
                    </area>
                  </process-id>
                </ospf>
              </router-ospf>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""