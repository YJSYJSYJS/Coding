# 시간제한: 2초
# 메모리제한: 128mb
N = int(input())
min_sec = [i for i in range(60) if '3' in str(i)]
ms_num = len(min_sec)
h_num = 0 
if N<3:
    h_num = 0 
elif N<13:
    h_num = 1
elif N<23:
    h_num = 2
else:
    h_num = 3 

h_case = h_num*60*60
m_case = (N-h_num+1)*ms_num*60
s_case = (N-h_num+1)*(60-ms_num)*ms_num
print(h_case+m_case+s_case)