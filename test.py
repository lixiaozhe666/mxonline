# _*_ encoding:utf-8 _*_
class Word(str):


    def __new__(cls, word):
        # 注意，我们只能使用 __new__ ，因为str是不可变类型
        # 所以我们必须提前初始化它（在实例创建时）
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')]
            # Word现在包含第一个空格前的所有字母
        return str.__new__(cls, word)#返回的是一个实例，这个word是实例的名称

    def __init__(self,word):#而这个word是实例的一个属性，即（实例）word.word（属性）的值
        self.word =word

temp = Word("1222 333")
print temp
print(temp.word)