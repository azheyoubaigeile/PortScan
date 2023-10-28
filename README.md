# PortScan

端口扫描

## 简介

本工具是一个简单的多线程端口扫描工具。它可以通过命令行参数指定目标IP地址和一个包含端口列表的字典文件，然后使用多个线程并行扫描这些端口，检查它们是否开放。你还可以设置扫描线程数量以及其他选项。最后，程序将输出已开放的端口信息。

## 使用

**使用说明**![image-20231028203800659](C:\Users\luo\AppData\Roaming\Typora\typora-user-images\image-20231028203800659.png)

  -h, --help                                    show this help message and exit
  -u URL, --url=URL                     你要扫描的IP地址
  -f FILE, --file=FILE                      包含端口列表的字典文件
  -t COUNT, --thread=COUNT    扫描威胁系数
  -p PORTS, --ports=PORTS        扫描特定端口，以逗号分隔

**扫描启动**

用法一：通过字典全方面扫描

```
python PortScan.py -u "192.168.80.129" -f "Port_top100.txt" -t 9
```

用法二：扫描特定端口

```
python PortScan.py -u "192.168.80.129" -p 80,135,3306 -t 9
```

**测试用例**![image-20231028204113965](C:\Users\luo\AppData\Roaming\Typora\typora-user-images\image-20231028204113965.png)![image-20231028204120521](C:\Users\luo\AppData\Roaming\Typora\typora-user-images\image-20231028204120521.png)