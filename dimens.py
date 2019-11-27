#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/16 11:31
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : dimens.py
# @Software   : PyCharm
# @Description: 生成dimens文件
"""
手机====================
1440x2560: xxxhdpi:4.0        dpi=640
1080x1920: xxhdpi: 3.0        dpi=480
720x1280:  xhdpi： 2.0        dpi=320
480x800:   hdpi：  1.5        dpi=240
320x480:   mdpi：  1.0（基准） dip=160
240x320:   ldpi：  0.75       dip=120

TV=======================
720x1280:  mdpi：1.0（基准）
1080x1920: hdpi：1.5

根据基准分辨率获取缩放比
"""

import os

# 基准宽高，单位px.(设计稿的尺寸,TV是横屏，切换为手机时是竖屏，这里需要修改)
base_x = 1280
base_y = 720
base_txt_size = 100


def main():
    # TV=====================================
    make_dir_and_file(x=1280, y=720)
    make_dir_and_file(x=1280, y=768)
    make_dir_and_file(x=1920, y=1080)
    make_dir_and_file(x=2560, y=1440)
    # Phone==================================
    # make_dir_and_file(x=720, y=1280)
    # make_dir_and_file(x=1080, y=1920)
    # make_dir_and_file(x=1440, y=2560)


def make_dir_and_file(x, y):
    xml_head = '<?xml version="1.0" encoding="utf-8"?>\n'
    resource_head = '<resources>\n'
    resource_end = '</resources>'

    # 命名规则：values-高x宽
    dir_path = './gen/values-%dx%d' % (y, x)
    file_name_x = 'lay_x.xml'
    file_name_y = 'lay_y.xml'
    file_name_str = 'string.xml'

    # 屏幕密度，取两位小数
    density_x = round((x / base_x), 2)
    density_y = round((y / base_y), 2)

    # 写入lay_x文件
    file_path = dir_path + "/" + file_name_x
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file = open(file_path, 'w', encoding='utf-8')
    file.write(xml_head)
    file.write(resource_head)
    for n in range(1, base_x + 1):
        px_x = n * density_x
        file.write('<dimen name="x%d">%.2fpx</dimen>\n' % (n, px_x))
    file.write(resource_end)
    file.close()

    # 写入lay_y文件
    file_path = dir_path + "/" + file_name_y
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file = open(file_path, 'w', encoding='utf-8')
    file.write(xml_head)
    file.write(resource_head)
    for m in range(1, base_y + 1):
        px_y = m * density_y
        file.write('<dimen name="y%d">%.2fpx</dimen>\n' % (m, px_y))
    file.write(resource_end)
    file.close()

    # 写入string.xml文件
    file_path = dir_path + "/" + file_name_str
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file = open(file_path, 'w', encoding='utf-8')
    file.write(xml_head)
    file.write(resource_head)
    for m in range(2, base_txt_size + 1, 2):
        px_x = m * density_x
        file.write('<dimen name="text_size_%d">%.2fpx</dimen>\n' % (m, px_x))
    file.write(resource_end)
    file.close()

    print('写入完成:', dir_path)


if __name__ == '__main__':
   main()
