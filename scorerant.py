# [分數]由以下轉成[等第分數] 
#     分數      等第分數
#    90-100       4.3
#    85-89        4.0
#    80-84        3.7
#    77-79        3.3
#    73-76        3.0
#    70-72        2.7
#    67-69        2.3
#    63-66        2.0
#    60-62        1.7
#    0-59         0

# 等第總分 = 各科分數轉成[等第分數]後的加總.
# 例如, 有人考了95, 85, 75, 65, 55
# 其[等第總分] = 4.3 + 4.0 + 3.0 + 2.0 + 0 = 13.3


#coding=utf-8
import m01

#--------------------------------------------------------------------
# 序號, 姓名, 第1次分數, 第2次分數, 第3次分數, 第4次分數, 第5次分數
#--------------------------------------------------------------------
for no, name, exam1, exam2, exam3, exam4, exam5 in [('120001','蔡家雅',80,75,65,86,76), ('120002','張怡宇',56,76,80,90,66), ('120003','王庭棋',90,93,95,100,95), ('120004','黃和夫',34,43,50,44,33), ('120005','林于文',75,64,80,90,94), ('120006','唐馨馨',90,43,95,30,63), ('120007','張韻庭',90,50,60,77,75), ('120008','應立煌',85,43,37,65,82), ('120009','賀家政',95,63,79,81,78), ('120010','游惠嘉',57,64,68,71,51), ('120011','林佑倫',73,87,89,91,92), ('120012','孫宥葳',61,63,65,67,81), ('120013','黃岑秀',76,56,54,67,57), ('120014','楊雅柔',90,93,95,96,78), ('120015','李至君',87,89,81,92,92)]:
    # 呼叫模組中的函式
    tot = m01.score(exam1, exam2, exam3, exam4, exam5)

    # 印出結果
    print('序號:{}, 姓名：{},等地總分：{}'.format(no,name,tot))