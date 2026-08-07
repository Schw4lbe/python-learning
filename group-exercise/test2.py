# default class inheritance example with method overwrite


class MyList(list):

    # overwrite pop method with default index 0 instead of -1
    def pop(self, index=0):
        # crawls up to parent class
        return super().pop(index)


x = MyList(["a", "b", "c"])

# looking for pop in class, sees overwrite and calls parent method by handing over new default index
print(x.pop())

# MRO = Method Resolution Order
# source: https://docs.python.org/3/reference/datamodel.html#type.__mro__
# returns resolution order
# mro() method is part of the object class
print(MyList.mro())

# output:
# [
#     <class '__main__.MyList'>,
#     <class 'list'>,
#     <class 'object'>
# ]


for cls in object.__subclasses__():
    # print out all object subclasses with the dunder attribute __mro__
    # mro() cant be called because the return for some classes like type needs a param
    print(cls.__mro__)
