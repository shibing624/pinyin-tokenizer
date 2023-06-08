[![PyPI version](https://badge.fury.io/py/pinyintokenizer.svg)](https://badge.fury.io/py/pinyin-tokenizer)
[![Downloads](https://pepy.tech/badge/pinyintokenizer)](https://pepy.tech/project/pinyin-tokenizer)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub contributors](https://img.shields.io/github/contributors/shibing624/pinyin-tokenizer.svg)](https://github.com/shibing624/pinyin-tokenizer/graphs/contributors)
[![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![python_vesion](https://img.shields.io/badge/Python-3.5%2B-green.svg)](requirements.txt)
[![GitHub issues](https://img.shields.io/github/issues/shibing624/pinyin-tokenizer.svg)](https://github.com/shibing624/pinyin-tokenizer/issues)
[![Wechat Group](http://vlog.sfyc.ltd/wechat_everyday/wxgroup_logo.png?imageView2/0/w/60/h/20)](#Contact)

# Pinyin Tokenizer
pinyin tokenizer（拼音分词器），将连续的拼音切分为单字拼音列表，开箱即用。python3开发。


**Guide**

- [Feature](#Feature)
- [Install](#install)
- [Usage](#usage)
- [Contact](#Contact)
- [Citation](#Citation)
- [Related-Projects](#Related-Projects)

# Feature

- 基于前缀树（PyTrie）高效快速把连续拼音切分为单字拼音列表，便于后续拼音转汉字等处理。

# Install

- Requirements and Installation

```
pip install pinyintokenizer
```

or

```
git clone https://github.com/shibing624/pinyin-tokenizer.git
cd pinyin-tokenizer
python setup.py install
```


# Usage

## 拼音切分（Pinyin Tokenizer）

example：[examples/pinyin_tokenize_demo.py](examples/pinyin_tokenize_demo.py):


```python
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
```

output:

```shell
(['wo'], ['3'])
(['ni', 'hao'], [])
(['lv', 'you'], ['3', '2'])
(['liu', 'de', 'hua'], [])
(['liu', 'de', 'hua'], [' ', ' '])
(['wo', 'men', 'zuo', 'ge', 'lv', 'you', 'gong', 'nue'], [])
(['xi', 'an', 'jiao', 'tong', 'da', 'xue'], [' '])
(['o', 'o', 'lu'], ['g', 'd', ' ', 'c', 'k'])
```
- `tokenize`方法返回两个结果，第一个为拼音列表，第二个为非法拼音列表。


## 连续拼音转汉字（Pinyin2Hanzi）
先使用本库[pinyintokenizer](https://pypi.org/project/pinyintokenizer/)把连续拼音切分，再使用[Pinyin2Hanzi](https://pypi.org/project/Pinyin2Hanzi/)库把拼音转汉字。

example：[examples/pinyin2hanzi_demo.py](examples/pinyin2hanzi_demo.py):


```python
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
```

output:

```shell
我
今天天气不错
刘德华
```



# Contact

- Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/pinyin-tokenizer.svg)](https://github.com/shibing624/pinyin-tokenizer/issues)
- 邮件我：xuming: xuming624@qq.com
- 微信我：加我*微信号：xuming624*, 进Python-NLP交流群，备注：*姓名-公司名-NLP*
<img src="docs/wechat.jpeg" width="200" />


# Citation

如果你在研究中使用了pinyin-tokenizer，请按如下格式引用：

APA:
```latex
Xu, M. pinyin-tokenizer: Chinese Pinyin tokenizer toolkit for NLP (Version 0.0.1) [Computer software]. https://github.com/shibing624/pinyin-tokenizer
```

BibTeX:
```latex
@misc{pinyin-tokenizer,
  title={pinyin-tokenizer: Chinese Pinyin tokenizer toolkit for NLP},
  author={Xu Ming},
  year={2022},
  howpublished={\url{https://github.com/shibing624/pinyin-tokenizer}},
}
```


# License


授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加**pinyin-tokenizer**的链接和授权协议。


# Contribute
项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：

 - 在`tests`添加相应的单元测试
 - 使用`python -m pytest`来运行所有单元测试，确保所有单测都是通过的

之后即可提交PR。


# Related Projects

- 汉字转拼音：[pypinyin](https://github.com/mozillazg/python-pinyin)
- 拼音转汉字：[Pinyin2Hanzi](https://github.com/letiantian/Pinyin2Hanzi)