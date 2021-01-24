#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(participant, completion):

    answer = ''
    dic = {}
    for p in participant:
        if p in dic:
            dic[p] +=1
        else: 
            dic[p] = 1
             
    for c in completion:
        dic[c] -= 1
        
        
    for key, values in dic.items():
        if values == 1:
            answer = key

    return answer

