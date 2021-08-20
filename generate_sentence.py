from icecream import ic
import random

grammar_rule = """
复合句子 = 句子 连词 复合句子 | 句子 
句子 = 主语s 谓语 宾语s
谓语 = 喜欢 | 讨厌 | 吃掉 | 玩 | 跑
主语s = 主语 和 主语 | 主语
宾语s = 宾语 和 宾语 | 宾语
主语 = 冠词 定语 代号
宾语 = 冠词 定语 代号
代号 = 名词 | 代词
名词 = 苹果 | 鸭梨 | 西瓜 | 小狗 | 小猫 | 滑板 | 老张 | 老王
代词 = 你 | 我 | 他 | 他们 | 你们 | 我们 | 它
定语 = 漂亮的 | 今天的 | 不知名的 | 神秘的 | 奇奇怪怪的
冠词 = 一个 | 一只 | 这个 | 那个
连词 = 但是 | 而且 | 不过
"""

def parse_grammar(rule):
    grammar = dict()
    for line in rule.split('\n'):
        if not line.strip():continue#strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        # print(line)
        target,expand = line.split('=')
        expands = expand.split('|')
        # ic(target,expand)#用来替代print做调试
        # ic(expands)

        grammar[target.strip()] = [e.strip() for e in expands]
        # ic(grammar)
    return grammar

def get_expand(target,grammar):
    if target not in grammar:return target#字典里没有的也让显示出来,比如：‘和’
    # print(target,grammar[target])         #用来查看过程挺高的***********
    expand = random.choice(grammar[target])#在符合的条件中随机选择一个
    return ''.join(get_expand(e,grammar) for e in expand.split())

if __name__ == '__main__':
    another_rule = """
        expression = ( math ) op ( expression ) | math 
        math = num op num
        num = sing_num num | sing_num
        sing_num = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
        op = + | - | * | / | ^ | ->
        """
    # ic(get_expand('复合句子',parse_grammar(grammar_rule)))
    for i in range(10):
        ic(get_expand('expression',parse_grammar(another_rule)))

