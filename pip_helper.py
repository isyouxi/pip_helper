#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
      @file:pip_util.py
      @des:下载｜安装 对应（win或any）pip版本的安装包

      # pip 命令说明
      # https://pip.pypa.io/en/stable/user_guide/
      # pip uninstall SomePackage     卸载包
      # pip search SomePackage        卸载包
      # pip uninstall SomePackage     卸载包
      # pip show                      显示安装包信息
      # pip show -f SomePackage       查看指定包的详细信息
      # pip list                      列出已安装的包
      # pip list -o                   查看可升级的包

"""
from pip._internal.cli.main import main

pip_source = {
      '官方源': 'https://pypi.org/simple/',# 下载win版本包 建议用官方源
      '阿里云': 'http://mirrors.aliyun.com/pypi/simple/',
}

local_down_dir = {
      'base': 'Z:\\var\\log\\mine\\',#目录根地址
      'win': 'win-pages',
      'any': 'any-pages',
}


def get_pip_link(page_name):
      """
      获取pip官方的包源地址 当下载不到的时候可以查看下
      :param page_name: 包名称
      :return:
      """
      if page_name.find('==') > -1:
            page_name = page_name[:page_name.rfind('==')]
      return 'https://pypi.org/project/{0}/#files'.format(page_name)


def freeze_requirements():
      """
      导出对比 requirements 文件 未列出到包
      :return:
      """
      main(['freeze',
            'requirements.txt'])


def down_pip_any_pages(pages=[], source='官方源'):
      """
      下载对应（any版本）的pip包到 win-pages目录
      :param pages:  指定需要下载到包名称
      :param source: 指定下载到源地址
      :return:
      """
      for pn in pages:
            main(['download',
                  '-i', pip_source[source],
                  '--only-binary=:all:',
                  # '--platform', 'win_amd64',
                  '--platform', 'any',
                  '--python-version', '37',
                  '--implementation', 'cp',
                  '--abi', 'none',
                  '--abi', 'cp37m',
                  # '-r', 'requirements.txt',
                  pn,
                  '-d', local_down_dir['any']])
            print("[{1}] 对应 pip link ：{0}".format(get_pip_link(pn), pn))


def down_pip_win_pages(pages=[], source='官方源'):
      """
      下载对应（win版本）的pip包到 win-pages目录
      :param pages:  指定需要下载到包名称
      :param source: 指定下载到源地址
      :return:
      """
      for pn in pages:
            main(['download',
                  '-i', pip_source[source],
                  '--only-binary=:all:',
                  '--platform', 'win_amd64',
                  # '--platform', 'any',
                  '--python-version', '37',
                  '--implementation', 'cp',
                  # '--abi', 'none',
                  # '-r', 'requirements.txt',
                  '--abi', 'cp37m',
                  pn,
                  '-d', local_down_dir['win']])
            print("[{1}] 对应 pip link ：{0}".format(get_pip_link(pn), pn))


def install_pip_win_pages(pages=[]):
      for pn in pages:
            print("执行安装包 [{0}]".format(pn))
            main(['install',
                  '--no-index',
                  '--find-links='+local_down_dir['base']+local_down_dir['win'],
                  pn])


def install_pip_any_pages(pages=[]):
      for pn in pages:
            print("执行安装包 [{0}]".format(pn))
            main(['install',
                  '--no-index',
                  '--find-links='+local_down_dir['base']+local_down_dir['any'],
                  # '-r', 'requirements.txt',
                  pn])


if __name__ == '__main__':
      down_pip_win_pages(pages=["pymongo==3.11.3"], source='官方源')
      # down_pip_any_pages(pages=["pymongo==3.11.3"], source='官方源')
      # install_pip_any_pages(pages=[])
      # install_pip_win_pages(pages=[])

