# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: pip install Pinyin2Hanzi
"""
import sys
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

sys.path.append('..')
from pinyintokenizer import PinyinTokenizer

dagparams = DefaultDagParams()


def pinyin2hanzi(pinyin_sentence):
    pinyin_list, _ = PinyinTokenizer().tokenize(pinyin_sentence)
    result = dag(dagparams, pinyin_list, path_num=1)
    return ''.join(result[0].path)


if __name__ == '__main__':
    print(f"{pinyin2hanzi('wo3')}")
    print(f"{pinyin2hanzi('jintianxtianqibucuo')}")
    print(f"{pinyin2hanzi('liudehua')}")
