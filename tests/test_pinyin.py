# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys
import unittest

sys.path.append('..')
from pinyintokenizer import PinyinTokenizer


class PinyinTestCase(unittest.TestCase):
    def setUp(self):
        m = PinyinTokenizer()
        m.setup()
        print('model:', m)

    def test_chinese_seg(self):
        new_m = PinyinTokenizer()
        r = new_m.tokenize('我爱北京天安门')
        print(r)
        self.assertTrue(r[0] == [])

    def test_chinesepinyin_seg(self):
        m = PinyinTokenizer()
        r = m.tokenize('wo3')
        print(r)
        self.assertTrue(r[0] == ['wo'])
        r = m.tokenize('wo3 ai bei3 jing1')
        print(r)
        self.assertTrue(r[0] == ['wo', 'ai', 'bei', 'jing'])
        r = m.tokenize('nihao')
        print(r)
        self.assertTrue(r[0] == ['ni', 'hao'])
        r = m.tokenize('liudehua3')
        print(r)
        self.assertTrue(r[0] == ['liu', 'de', 'hua'])
        r = m.tokenize('liude hua3')
        print(r)
        self.assertTrue(r[0] == ['liu', 'de', 'hua'])

    def test_badcase(self):
        m = PinyinTokenizer()
        r = m.tokenize("lvyou")
        print(r)
        self.assertTrue(r[0] == ['lv', 'you'])
        r = m.tokenize("lv2you")
        print(r)
        self.assertTrue(r[0] == ['lv', 'you'])
        self.assertTrue(r[1] == ['2'])

        r = m.tokenize("nv3ren2")
        print(r)
        self.assertTrue(r[0] == ['nv', 'ren'])
        self.assertTrue(r[1] == ['3', '2'])

        r = m.tokenize("nvyougongnue")
        print(r)

        r = m.tokenize("nuedai") # 虐待
        print(r)

        r = m.tokenize("jielue")  # 劫掠
        print(r)


if __name__ == '__main__':
    unittest.main()
