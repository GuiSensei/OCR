#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
对图片a.jpg进行文字识别
"""

#安装aip模块：pip install baidu-aip
from aip import AipOcr

# 读取图片
def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()  

def ocr_pic(file):
    """ 你的 APPID AK SK，在百度云获取，https://cloud.baidu.com/"""
    APP_ID = '10665005'  
    API_KEY = '2ly8CzT3FhvU6nIlbemyxR58'  
    SECRET_KEY = 'Aetgo4i2O35HNH1M8Kn5ROFv6BdgRrPC' 
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 定义参数变量
    options = {'detect_direction': 'true','language_type': 'CHN_ENG',}  

    # 调用通用文字识别接口
    result = client.basicGeneral(get_file_content(file), options)['words_result']

    if 'error_code' in result:
        print('错误代码：',result['error_code'],'\n错误原因：',result['error_msg'])
        exit()
        
    words = ''
    for each in result:
        words += each['words']
    return words

if __name__ == "__main__":
    file = "a.jpg"  
    print(ocr_pic(file))



