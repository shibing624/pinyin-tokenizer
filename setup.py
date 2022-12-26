# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from setuptools import setup, find_packages

__version__ = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='pinyintokenizer',
    version=__version__,
    description='Pinyin Tokenizer, chinese pinyin tokenizer',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/pinyin-tokenizer',
    license='Apache 2.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='pinyin-tokenizer,pinyin,pinyintokenizer,tokenizer',
    install_requires=[
        "six",
    ],
    packages=find_packages(exclude=['tests']),
    package_dir={'pinyintokenizer': 'pinyintokenizer'},
    package_data={
        'pinyintokenizer': ['*.*', '*.txt'],
    },
)
