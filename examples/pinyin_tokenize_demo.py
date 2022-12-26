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
    print(f"{m.tokenize('liudehua')}")
    print(f"{m.tokenize('liu de hua')}")
    print(f"{m.tokenize('good luck')}")
    print(f"{m.tokenize('xi anjiaotongdaxue')}")
