#!/usr/bin/env python
# coding: utf-8

# In[2]:


#10818
n = int(input())
lst = list(map(int, input().split()))

print(min(lst), max(lst))


# In[ ]:


#2562
lst = []

for i in range(9):
    lst.append(int(input()))
mx = max(lst)
print(mx)
print(lst.index(mx)+1)


# In[6]:


#2577 컴파일 에러 뜸
A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)

for i in range(1,10):
    print(result.count(str(i)))


# In[3]:


# 3052

lst = []
result = []
for i in range(10):
    lst.append(int(input()))

for i in range(len(lst)):
    result.append(lst[i]%42)

#print(len(set(result)))


# In[5]:


# 1546

N = int(input())
lst = list(map(int, input().split()))
mx = max(lst)
add = 0
for i in range(len(lst)):
    add += (lst[i]/mx)*100

print(add/len(lst))    
    


# In[ ]:


# 8958

N = int(input())
for i in range(N):
    input_str = input()
    point = 0
    total = 0
    for j in range(len(input_str)):
        if input_str[j] == 'O':
            point += 1
            total += point
        else:
            point = 0
    print(total)


# In[5]:


# 4344

C = int(input())
for i in range(C):
    input_lst = list(map(int, input().split()))
    lst = input_lst[1:]
    avg = sum(lst)/input_lst[0]
    n = 0
    for j in range(input_lst[0]):
        if lst[j] > avg:
            n += 1
    print(str("%.3f" %round((n/input_lst[0])*100, 3))+'%')


# In[ ]:


# 15596

def solve(a):
    ans = sum(a)
    return ans


# In[ ]:


# 10828 시간 초과 뜸

N = int(input())
stack = list()
for i in range(N):
    order = input()
    if order.split()[0] == 'push':
        stack.append(int(order.split()[1]))
    elif order == 'pop':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop('-1')
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if not stack:
            print('1')
        else:
            print('0')
    elif order == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
        
    

