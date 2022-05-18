#!/usr/bin/python
# -*- coding: UTF-8 -*-


def stat_ttest(group1, group2):
    from scipy.stats import ttest_ind
    import scipy.stats as stats
    import numpy as np
    group1 = np.array(group1, dtype='float')
    group2 = np.array(group2, dtype='float')

    if stats.levene(group1, group2)[1] > 0.05:
        t_statistic, pVal = ttest_ind(group1, group2, equal_var=True)
    else:
        t_statistic, pVal = ttest_ind(group1, group2, equal_var=False)
    re_str = ''
    if pVal > 0.05:
        re_str = 'ns'
    elif 0.05 >= pVal > 0.01:
        re_str = '*'
    elif 0.01 >= pVal > 0.001:
        re_str = '**'
    elif 0.001 >= pVal:
        re_str = '***'
    else:
        print(pVal)
    return re_str, pVal


if __name__ == "__main__":
    dig = [[102, 100, 98], [205, 208, 202], [123, 120, 131], [95, 98, 103], [263, 259, 258]]
    name = ['WT', 'Mut_1', 'Mut_2', 'Mut_3', 'Mut_4']
    wt_dig, wt_name = dig[0], name[0]
    mut_dig_list, mut_name_list = dig[1:], name[1:]
    for mut_dig, mut_name in zip(mut_dig_list, mut_name_list):
        print(f"{mut_name} <==> {wt_name}\n{stat_ttest(wt_dig, mut_dig)}\n")

