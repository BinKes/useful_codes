# -*- coding: UTF-8 -*-
import difflib
from timestamp_log import timestamp_log

@timestamp_log
def inner_compare(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    str1 += '\n'
    str2 += '\n'
    diff_result = difflib.ndiff(str1.splitlines(1), str2.splitlines(1))
    list_diff = list(diff_result)
    diff_result = ''.join(list_diff)
    print(diff_result)

    return diff_result 
a="""all
    dsasd
    sdfsdf
    dsfsd
    ddd
    """
b="""all
    cdsvd
    sdfsdf
    dsfdd
    ddd
    """
inner_compare(a, b)
