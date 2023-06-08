# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
from pinyintokenizer import PinyinTokenizer

if __name__ == '__main__':
    m = PinyinTokenizer()
    print(f"{m.tokenize('wo3')}")
    print(f"{m.tokenize('nihao')}")
    print(f"{m.tokenize('lv3you2')}")  # 旅游
    print(f"{m.tokenize('liudehua')}")
    print(f"{m.tokenize('liu de hua')}")  # 刘德华
    print(f"{m.tokenize('womenzuogelvyougongnue')}")  # 我们做个旅游攻略
    print(f"{m.tokenize('xi anjiaotongdaxue')}")  # 西安交通大学

    # not support english
    print(f"{m.tokenize('good luck')}")
