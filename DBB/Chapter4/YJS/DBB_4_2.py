# 시간제한: 2초
# 메모리제한: 128mb
N = int(input())
s = [i for i in range(60) if '3' in str(i)]
m = [i for i in range(60) if '3' in str(i)]
h = [i for i in range(N) if '3' in str(i)]
s_num = len(s)
m_num = len(m)
h_num = len(h)
a = s_num*60*(N+1)
b = (60-s_num)*m_num*(N+1)
c = (60-s_num)*(60-m_num)*h_num
print(a+b+c)