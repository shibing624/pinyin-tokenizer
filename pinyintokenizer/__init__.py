# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
__version__ = '0.0.3'


class PyTrieNode(object):
    def __init__(self, key="", seq=()):
        self.key = key
        self.end = len(seq) == 0
        self.children = {}
        if len(seq) > 0:
            self.children[seq[0]] = PyTrieNode(seq[0], seq[1:])

    def add(self, seq):
        if len(seq) == 0:
            self.end = True
        else:
            key = seq[0]
            value = seq[1:]
            if key in self.children:
                self.children[key].add(value)
            else:
                self.children[key] = PyTrieNode(key, value)

    def find(self, sentence):
        for i in range(len(sentence)):
            j = len(sentence) - i
            if len(sentence) >= j:
                key = sentence[:j]
                if key in self.children:
                    buffer, success = self.children[key].find(sentence[j:])
                    if success:
                        # Generalize special case handling
                        if buffer and self.is_special_case(buffer[-1]):
                            b1, s1 = self.children[key].find(buffer[:-1])
                            _, s2 = self.children[buffer[-1]].find(sentence[j + len(buffer):])
                            if s1 and s2:
                                return key + b1, True
                        return key + buffer, True
        return "", self.end

    def is_special_case(self, char):
        # Define the special case condition here
        return char in ['g']


class PinyinTokenizer(object):
    def __init__(self):
        self.root = PyTrieNode()
        self.root.end = False
        self.setup()

    def add(self, seq):
        self.root.add(seq)

    def setup(self):
        self.add(["a"])
        self.add(["ai"])
        self.add(["an"])
        self.add(["ang"])
        self.add(["ao"])
        self.add(["e"])
        self.add(["ei"])
        self.add(["en"])
        self.add(["er"])
        self.add(["o"])
        self.add(["ou"])
        self.add(["b", "a"])
        self.add(["b", "ai"])
        self.add(["b", "an"])
        self.add(["b", "ang"])
        self.add(["b", "ao"])
        self.add(["b", "ei"])
        self.add(["b", "en"])
        self.add(["b", "eng"])
        self.add(["b", "i"])
        self.add(["b", "ian"])
        self.add(["b", "iao"])
        self.add(["b", "ie"])
        self.add(["b", "in"])
        self.add(["b", "ing"])
        self.add(["b", "o"])
        self.add(["b", "u"])
        self.add(["c", "a"])
        self.add(["c", "ai"])
        self.add(["c", "an"])
        self.add(["c", "ang"])
        self.add(["c", "ao"])
        self.add(["c", "e"])
        self.add(["c", "en"])
        self.add(["c", "eng"])
        self.add(["c", "i"])
        self.add(["c", "ong"])
        self.add(["c", "ou"])
        self.add(["c", "u"])
        self.add(["c", "uan"])
        self.add(["c", "ui"])
        self.add(["c", "un"])
        self.add(["c", "uo"])
        self.add(["ch", "a"])
        self.add(["ch", "ai"])
        self.add(["ch", "an"])
        self.add(["ch", "ang"])
        self.add(["ch", "ao"])
        self.add(["ch", "e"])
        self.add(["ch", "en"])
        self.add(["ch", "eng"])
        self.add(["ch", "i"])
        self.add(["ch", "ong"])
        self.add(["ch", "ou"])
        self.add(["ch", "u"])
        self.add(["ch", "uai"])
        self.add(["ch", "uan"])
        self.add(["ch", "uang"])
        self.add(["ch", "ui"])
        self.add(["ch", "un"])
        self.add(["ch", "uo"])
        self.add(["d", "a"])
        self.add(["d", "ai"])
        self.add(["d", "an"])
        self.add(["d", "ang"])
        self.add(["d", "ao"])
        self.add(["d", "e"])
        self.add(["d", "eng"])
        self.add(["d", "i"])
        self.add(["d", "ia"])
        self.add(["d", "ian"])
        self.add(["d", "iao"])
        self.add(["d", "ie"])
        self.add(["d", "ing"])
        self.add(["d", "iu"])
        self.add(["d", "ong"])
        self.add(["d", "ou"])
        self.add(["d", "u"])
        self.add(["d", "uan"])
        self.add(["d", "ui"])
        self.add(["d", "un"])
        self.add(["d", "uo"])
        self.add(["f", "a"])
        self.add(["f", "an"])
        self.add(["f", "ang"])
        self.add(["f", "ei"])
        self.add(["f", "en"])
        self.add(["f", "eng"])
        self.add(["f", "o"])
        self.add(["f", "ou"])
        self.add(["f", "u"])
        self.add(["g", "a"])
        self.add(["g", "ai"])
        self.add(["g", "an"])
        self.add(["g", "ang"])
        self.add(["g", "ao"])
        self.add(["g", "e"])
        self.add(["g", "ei"])
        self.add(["g", "en"])
        self.add(["g", "eng"])
        self.add(["g", "ong"])
        self.add(["g", "ou"])
        self.add(["g", "u"])
        self.add(["g", "ua"])
        self.add(["g", "uai"])
        self.add(["g", "uan"])
        self.add(["g", "uang"])
        self.add(["g", "ui"])
        self.add(["g", "un"])
        self.add(["g", "uo"])
        self.add(["h", "a"])
        self.add(["h", "ai"])
        self.add(["h", "an"])
        self.add(["h", "ang"])
        self.add(["h", "ao"])
        self.add(["h", "e"])
        self.add(["h", "ei"])
        self.add(["h", "en"])
        self.add(["h", "eng"])
        self.add(["h", "ong"])
        self.add(["h", "ou"])
        self.add(["h", "u"])
        self.add(["h", "ua"])
        self.add(["h", "uai"])
        self.add(["h", "uan"])
        self.add(["h", "uang"])
        self.add(["h", "ui"])
        self.add(["h", "un"])
        self.add(["h", "uo"])
        self.add(["j", "i"])
        self.add(["j", "ia"])
        self.add(["j", "ian"])
        self.add(["j", "iang"])
        self.add(["j", "iao"])
        self.add(["j", "ie"])
        self.add(["j", "in"])
        self.add(["j", "ing"])
        self.add(["j", "iong"])
        self.add(["j", "iu"])
        self.add(["j", "u"])
        self.add(["j", "uan"])
        self.add(["j", "ue"])
        self.add(["j", "un"])
        self.add(["k", "a"])
        self.add(["k", "ai"])
        self.add(["k", "an"])
        self.add(["k", "ang"])
        self.add(["k", "ao"])
        self.add(["k", "e"])
        self.add(["k", "en"])
        self.add(["k", "eng"])
        self.add(["k", "ong"])
        self.add(["k", "ou"])
        self.add(["k", "u"])
        self.add(["k", "ua"])
        self.add(["k", "uai"])
        self.add(["k", "uan"])
        self.add(["k", "uang"])
        self.add(["k", "ui"])
        self.add(["k", "un"])
        self.add(["k", "uo"])
        self.add(["l", "a"])
        self.add(["l", "ai"])
        self.add(["l", "an"])
        self.add(["l", "ang"])
        self.add(["l", "ao"])
        self.add(["l", "e"])
        self.add(["l", "ei"])
        self.add(["l", "eng"])
        self.add(["l", "i"])
        self.add(["l", "ia"])
        self.add(["l", "ian"])
        self.add(["l", "iang"])
        self.add(["l", "iao"])
        self.add(["l", "ie"])
        self.add(["l", "in"])
        self.add(["l", "ing"])
        self.add(["l", "iu"])
        self.add(["l", "ong"])
        self.add(["l", "ou"])
        self.add(["l", "u"])
        self.add(["l", "u:"])
        self.add(["l", "v"])
        self.add(["l", "ue"])
        self.add(["l", "ve"])
        self.add(["l", "uan"])
        self.add(["l", "un"])
        self.add(["l", "uo"])
        self.add(["m", ""])
        self.add(["m", "a"])
        self.add(["m", "ai"])
        self.add(["m", "an"])
        self.add(["m", "ang"])
        self.add(["m", "ao"])
        self.add(["m", "e"])
        self.add(["m", "ei"])
        self.add(["m", "en"])
        self.add(["m", "eng"])
        self.add(["m", "i"])
        self.add(["m", "ian"])
        self.add(["m", "iao"])
        self.add(["m", "ie"])
        self.add(["m", "in"])
        self.add(["m", "ing"])
        self.add(["m", "iu"])
        self.add(["m", "o"])
        self.add(["m", "ou"])
        self.add(["m", "u"])
        self.add(["n", "a"])
        self.add(["n", "ai"])
        self.add(["n", "an"])
        self.add(["n", "ang"])
        self.add(["n", "ao"])
        self.add(["n", "e"])
        self.add(["n", "ei"])
        self.add(["n", "en"])
        self.add(["n", "eng"])
        self.add(["n", "g"])
        self.add(["n", "i"])
        self.add(["n", "ian"])
        self.add(["n", "iang"])
        self.add(["n", "iao"])
        self.add(["n", "ie"])
        self.add(["n", "in"])
        self.add(["n", "ing"])
        self.add(["n", "iu"])
        self.add(["n", "ong"])
        self.add(["n", "ou"])
        self.add(["n", "u"])
        self.add(["n", "u:"])
        self.add(["n", "ue"])
        self.add(["n", "v"])
        self.add(["n", "ve"])
        self.add(["n", "uan"])
        self.add(["n", "uo"])
        self.add(["p", "a"])
        self.add(["p", "ai"])
        self.add(["p", "an"])
        self.add(["p", "ang"])
        self.add(["p", "ao"])
        self.add(["p", "ei"])
        self.add(["p", "en"])
        self.add(["p", "eng"])
        self.add(["p", "i"])
        self.add(["p", "ian"])
        self.add(["p", "iao"])
        self.add(["p", "ie"])
        self.add(["p", "in"])
        self.add(["p", "ing"])
        self.add(["p", "o"])
        self.add(["p", "ou"])
        self.add(["p", "u"])
        self.add(["q", "i"])
        self.add(["q", "ia"])
        self.add(["q", "ian"])
        self.add(["q", "iang"])
        self.add(["q", "iao"])
        self.add(["q", "ie"])
        self.add(["q", "in"])
        self.add(["q", "ing"])
        self.add(["q", "iong"])
        self.add(["q", "iu"])
        self.add(["q", "u"])
        self.add(["q", "uan"])
        self.add(["q", "ue"])
        self.add(["q", "un"])
        self.add(["r", "an"])
        self.add(["r", "ang"])
        self.add(["r", "ao"])
        self.add(["r", "e"])
        self.add(["r", "en"])
        self.add(["r", "eng"])
        self.add(["r", "i"])
        self.add(["r", "ong"])
        self.add(["r", "ou"])
        self.add(["r", "u"])
        self.add(["r", "uan"])
        self.add(["r", "ui"])
        self.add(["r", "un"])
        self.add(["r", "uo"])
        self.add(["s", "a"])
        self.add(["s", "ai"])
        self.add(["s", "an"])
        self.add(["s", "ang"])
        self.add(["s", "ao"])
        self.add(["s", "e"])
        self.add(["s", "en"])
        self.add(["s", "eng"])
        self.add(["s", "i"])
        self.add(["s", "ong"])
        self.add(["s", "ou"])
        self.add(["s", "u"])
        self.add(["s", "uan"])
        self.add(["s", "ui"])
        self.add(["s", "un"])
        self.add(["s", "uo"])
        self.add(["sh", "a"])
        self.add(["sh", "ai"])
        self.add(["sh", "an"])
        self.add(["sh", "ang"])
        self.add(["sh", "ao"])
        self.add(["sh", "e"])
        self.add(["sh", "ei"])
        self.add(["sh", "en"])
        self.add(["sh", "eng"])
        self.add(["sh", "i"])
        self.add(["sh", "ou"])
        self.add(["sh", "u"])
        self.add(["sh", "ua"])
        self.add(["sh", "uai"])
        self.add(["sh", "uan"])
        self.add(["sh", "uang"])
        self.add(["sh", "ui"])
        self.add(["sh", "un"])
        self.add(["sh", "uo"])
        self.add(["t", "a"])
        self.add(["t", "ai"])
        self.add(["t", "an"])
        self.add(["t", "ang"])
        self.add(["t", "ao"])
        self.add(["t", "e"])
        self.add(["t", "eng"])
        self.add(["t", "i"])
        self.add(["t", "ian"])
        self.add(["t", "iao"])
        self.add(["t", "ie"])
        self.add(["t", "ing"])
        self.add(["t", "ong"])
        self.add(["t", "ou"])
        self.add(["t", "u"])
        self.add(["t", "uan"])
        self.add(["t", "ui"])
        self.add(["t", "un"])
        self.add(["t", "uo"])
        self.add(["w", "a"])
        self.add(["w", "ai"])
        self.add(["w", "an"])
        self.add(["w", "ang"])
        self.add(["w", "ei"])
        self.add(["w", "en"])
        self.add(["w", "eng"])
        self.add(["w", "o"])
        self.add(["w", "u"])
        self.add(["x", "i"])
        self.add(["x", "ia"])
        self.add(["x", "ian"])
        self.add(["x", "iang"])
        self.add(["x", "iao"])
        self.add(["x", "ie"])
        self.add(["x", "in"])
        self.add(["x", "ing"])
        self.add(["x", "iong"])
        self.add(["x", "iu"])
        self.add(["x", "u"])
        self.add(["x", "uan"])
        self.add(["x", "ue"])
        self.add(["x", "un"])
        self.add(["y", "a"])
        self.add(["y", "an"])
        self.add(["y", "ang"])
        self.add(["y", "ao"])
        self.add(["y", "e"])
        self.add(["y", "i"])
        self.add(["y", "iao"])
        self.add(["y", "in"])
        self.add(["y", "ing"])
        self.add(["y", "o"])
        self.add(["y", "ong"])
        self.add(["y", "ou"])
        self.add(["y", "u"])
        self.add(["y", "uan"])
        self.add(["y", "ue"])
        self.add(["y", "un"])
        self.add(["z", "a"])
        self.add(["z", "ai"])
        self.add(["z", "an"])
        self.add(["z", "ang"])
        self.add(["z", "ao"])
        self.add(["z", "e"])
        self.add(["z", "ei"])
        self.add(["z", "en"])
        self.add(["z", "eng"])
        self.add(["z", "i"])
        self.add(["z", "ong"])
        self.add(["z", "ou"])
        self.add(["z", "u"])
        self.add(["z", "uan"])
        self.add(["z", "ui"])
        self.add(["z", "un"])
        self.add(["z", "uo"])
        self.add(["zh", "a"])
        self.add(["zh", "ai"])
        self.add(["zh", "an"])
        self.add(["zh", "ang"])
        self.add(["zh", "ao"])
        self.add(["zh", "e"])
        self.add(["zh", "en"])
        self.add(["zh", "eng"])
        self.add(["zh", "i"])
        self.add(["zh", "ong"])
        self.add(["zh", "ou"])
        self.add(["zh", "u"])
        self.add(["zh", "ua"])
        self.add(["zh", "uai"])
        self.add(["zh", "uan"])
        self.add(["zh", "uang"])
        self.add(["zh", "ui"])
        self.add(["zh", "un"])
        self.add(["zh", "uo"])

    def tokenize(self, sent):
        """
        Tokenize a sentence into pinyin list.
        :param sent: pinyin sentence
        :return: pinyin_list, invalid pinyin list

        :example:
            m = PinyinTokenizer()
            words, invalid_words = m.tokenize("liudehua")
            print("words: {}".format(words))
        """
        words = []
        invalid_words = []
        while len(sent) > 0:
            buf, succ = self.root.find(sent)
            if succ:
                words.append(buf)
                sent = sent[len(buf):]
            else:
                invalid_words.append(sent[0])
                sent = sent[1:]
        return words, invalid_words


if __name__ == "__main__":
    m = PinyinTokenizer()
    words, invalid_words = m.tokenize("liudehua")
    print("words: {}".format(words))
