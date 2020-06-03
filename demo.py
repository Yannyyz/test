# import requests
# import lxml.html
# url="https://user.qzone.qq.com/582629001"
# a=requests.get(url).content.decode("utf-8")
#
# page=lxml.html.fromstring(a)
# c=page.xpath('//title/text()')
# print(c)


a='pgv_pvi=7161477120; pgv_pvid=1713887860; RK=PJLQLHuNFj; ptcz=be4f7338cd733b7a83852df1df0d9142041023071a54d5363c93ea5f21daa945; tvfe_boss_uuid=0faf2c93ac25c77e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225911267%22%2C%22%24device_id%22%3A%2216f54cf1053519-0939762a70a007-6701b35-2073600-16f54cf1054b1d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2216f54cf1053519-0939762a70a007-6701b35-2073600-16f54cf1054b1d%22%7D; pac_uid=0_fd818cbfe5e9e; ptui_loginuin=582629001; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; cpu_performance_v8=1; o_cookie=582629001; luin=o0582629001; lskey=0001000038b9d96bb3dfa2384ddd3eb100beec1868a2a76ed8a95421b1f6527a7e12bc30590e0a15e7f90691; _qpsvr_localtk=0.16934309472988396; pgv_si=s3886512128; pgv_info=ssid=s9499515620; uin=o0582629001; skey=@m4CqZBl2N; p_uin=o0582629001; pt4_token=jnBu9bsIM06Z5vHnp0C7wka4mgWEi3bgW1cipMw19Ts_; p_skey=nIAuroYDdoMT1lEWQ08ZS4IokVm89aIoZ4JawOInSXk_; Loading=Yes'
b={

}
c=a.replace(' ','')
d=c.split(";")
for i in d:
    key,value=i.split("=",1)
    b[key]=value
print(b)