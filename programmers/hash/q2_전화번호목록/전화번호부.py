#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(pb):
    answer = True
    pb.sort()
    
    for i in range(len(pb)):
        breaker = False
        for j in range(i+1, len(pb)):
            if pb[i] == pb[j][:len(pb[i])]:
                
                answer = False
                breaker = True
                break
        if breaker:
            break
            
    return answer

