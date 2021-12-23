# -- coding: utf-8 --
# @Author   : Li
# @Time    : 2021/12/23 16:07

"""感受野计算程序"""

K = [4, 4, 4, 4, 4]  # 卷积核尺寸
S = [2, 2, 2, 1, 1]  # 步幅


def show_rf(K, S):
    assert (len(K) == len(S))

    def receptive_field(i):
        RF = 1
        for j in range(i, 0, -1):
            RF = (RF-1) * S[j-1] + K[j-1]
        return RF

    for i in range(1, len(K) + 1):
        print('第%d层感受野：' % i, receptive_field(i))  # output=11


show_rf(K, S)
print()

