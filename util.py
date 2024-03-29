#!/usr/bin/python
# encoding: utf-8
# 实现文本块生成器把纯文本分成一个一个的文本块，以便接下来对每一个文本块进行解析

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'


def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []