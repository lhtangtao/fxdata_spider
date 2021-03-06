# fxdata_spider
工作需要定制的爬虫

目前第一阶段的工作内容都放在get_info_from_163文件夹中

在此文件夹中有以下几个文件夹，所存放的文件及内容介绍如下:

·curl文件夹 curl.py 主要提供curl各种资源，如curl某个特定的url，curl某个特定的class和category，curl某个特定的class

·http文件夹下的cache文件夹是根据class 和category 读取数据库中已存在的资源的url和文件大小  这个文件是由http.py生成的

kind_info是每种kind（多个curl资源组成某种kind）的url地址和总的大小，这个文件是由class_info.py生成的config

config_linux_to_curl里的内容为你所需要执行curl操作的linux机器的ip 登录帐号和密码

tools文件夹下存放链接数据库以及链接linux的函数

使用的时候直接调用根目录下的main函数即可

日志文件说明

linux_curl_log : 在什么时间 curl了什么东西，包括url 大小 class 和category 开始和结束的时候还会输出debug日志以及一共循环执行了多少次kind


原理图：
![网络拓扑图](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/%E7%BD%91%E7%BB%9C%E6%8B%93%E6%89%91%E5%9B%BE.png)

![基本流程图](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/%E5%9F%BA%E6%9C%AC%E6%B5%81%E7%A8%8B%E5%9B%BE.png)

![基本函数图](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/%E5%9F%BA%E6%9C%AC%E5%87%BD%E6%95%B0%E5%9B%BE.png)
第一步：使用get_all_cache()函数 根据class 和 category 从数据库中筛选出小于10mb的资源，放入各自的文件夹中 /http/cache/各类文件

kind为各种curl指定的class和category的集合，不同的kind由不同的class和category组合而成。而他们所执行的curl的url都是上文中/http/cache中的url

第二步：使用calculate_kind函数获取没中kind所curl的资源并且写入到/kind_info/cache_service下 里面的信息包含了各种class资源的大小 和各种class+category的资源大小

第三步：输入开始时间和结束时间开始执行规律的curl操作 在执行前和执行后都获取一次debug信息 

开始的时间请务必设定为5*n+1 即第6，11，16分钟之类的，这样的话，执行第一次curl会在五分钟维度内的第一分钟后，第二次curl会在五分钟纬度内的第三分钟之后

所有执行的curl操作都写入到curl_log文件中 这个文件就是日后用来分析用的文件

目前共五个kind 每个kind分为两部分，中间间隔120秒 

固定每五分钟执行一次kind 五个kind一个循环，直到到达指定的结束时间

第四步：使用get_resource_verbose函数，从curl_log中获取每个资源执行了多少次，随后从数据库中获取该资源的大小并且写入到resource_list_verbose中

第五步：使用hot_list函数，根据次数*每个资源的大小求出总共的service_size后从大到小排序并且根据class和总榜单写入相应的文件中。

![函数图](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/%E5%87%BD%E6%95%B0%E5%9B%BE.png)
![kind是什么 ](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/curl_kind%20%E5%85%B3%E7%B3%BB.png)
------------------------------------------------------------------------------------------------------------

目前实现功能：

1.get_all_cache（）获取
从内网的数据库中获取所有的已存在的资源，按照class和category分类。如下图所示
![获取所有的资源信息](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/cache_info_list.png)

2.calculate_kind（）计算每种kind的资源信息，如下图所示
![kind的信息](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/kind_info.png)

![kind_list信息](https://github.com/lhtangtao/fxdata_spider/blob/master/get_info_from_163/pic/kind_list.png)

3.根据开始和结束时间，循环执行curl操作。先判断开始时间是否大于当前时间，再判断开始时间是否小于预期结束时间。

4.在指定的时间开始执行curl操作，所执行的操作会被写入到curl_log中如下图所示：（可以通过user_agent来区分点播的种类，移动端或者pc端）

5.通过设置node可以设置执行多少次kind循环一次

所做的curl信息，写入到curl_log中，后续的一些操作，包括重定向日志 服务日志 是否出错热榜资源的统计等信息都是从curl_log中提取执行的

