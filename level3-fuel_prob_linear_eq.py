def sign(x):
    if x >= 0:
        return 1
    return -1

def mcommon(num1, num2):
    if num1 == 0 or num2 == 0:
        return 1
    m = max(num1, num2)
    n = min(num1, num2)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

def lcommon(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def minus_fac(a, b):
    if is_zero_fac(a):
        return reverse_fac(b)
    elif is_zero_fac(a):
        return a
    a_f, a_1, a_2 = a
    b_f, b_1, b_2 = b
    r_1 = a_f * a_1 * b_2 - b_f * a_2 * b_1
    r_2 = a_2 * b_2
    rcommon = mcommon(r_1, r_2)
    if r_1 == 0:
        return (1, 0, 1)
    return (sign(r_1), abs(int(r_1/rcommon)), abs(int(r_2/rcommon)))


def mul_fac(a, b):
    if is_zero_fac(a):
        return (1, 0, 1)
    elif is_zero_fac(b):
        return (1, 0, 1)
    a_f, a_1, a_2 = a
    b_f, b_1, b_2 = b
    r_f = a_f * b_f
    r_1 = a_1 * b_1
    r_2 = a_2 * b_2
    rcommon = mcommon(r_1, r_2)
    return (r_f, abs(int(r_1/rcommon)), abs(int(r_2/rcommon)))

def div_fac(a, b):
    if is_zero_fac(a):
        return (1, 0, 1)
    a_f, a_1, a_2 = a
    b_f, b_2, b_1 = b
    r_f = a_f * b_f
    r_1 = a_1 * b_1
    r_2 = a_2 * b_2
    rcommon = mcommon(r_1, r_2)
    return (r_f, abs(int(r_1/rcommon)), abs(int(r_2/rcommon)))

def is_zero_fac(a):
    a_f, a_1, a_2 = a
    return a_1 == 0

def reverse_fac(a):
    a_f, a_1, a_2 = a
    if a_1 == 0:
        return (1,0,1)
    return (-a_f, a_1, a_2)

def answer(m):
    points_num = len(m)
    points_static_out = []
    terminals = 0
    #preprocess m
    terminal_lines = []
    non_terminal_lines = []
    for m_i in range(points_num):
        if sum(m[m_i]) == 0:
            terminal_lines.append(m_i)
        else:
            non_terminal_lines.append(m_i)
    sequences = non_terminal_lines + terminal_lines
    collector = []
    terminal_collector = []
    for matrix in m:
        if sum(matrix) == 0:
            terminal_collector.append(matrix)
        else:
            collector.append(matrix)
    m = collector + terminal_collector
    copy_m = []
    for i in range(points_num):
        temp = list()
        for j in range(points_num):
            temp.append(m[i][j])
        copy_m.append(temp)
    j_index = 0
    for i in range(points_num):
        j_index = 0
        for j in sequences:
            m[i][j_index] = copy_m[i][j]
            j_index += 1
    # init above state
    for i in range(points_num):
        sum_total = sum(m[i])
        temp = list()
        if sum_total != 0:
            for j in range(points_num):
                if j != i:
                    if m[i][j] == 0:
                        temp.append((1, 0, 1))
                    else:
                        temp.append((1, m[i][j], sum_total))
                else:
                    temp.append(minus_fac((1, m[i][j], sum_total), (1, 1, 1)))
            points_static_out.append(temp)
        else:
            terminals += 1
    arr_num = len(points_static_out)
    if arr_num == 0:
        return [1, 1]
    arr_len = len(points_static_out[0])
    for rd in range(arr_num):
        for below in range(rd + 1, arr_num):
            div_factor = div_fac(points_static_out[below][rd], points_static_out[rd][rd])
            for i in range(arr_len):
                points_static_out[below][i] = minus_fac(points_static_out[below][i], mul_fac(div_factor, points_static_out[rd][i]))
    for clr in range(1, arr_num):
        div_factor = div_fac(points_static_out[0][clr], points_static_out[clr][clr])
        for i in range(arr_len):
            points_static_out[0][i] = minus_fac(points_static_out[0][i], mul_fac(div_factor, points_static_out[clr][i]))
    lcom = 1
    result = []
    for ter_index in range(arr_len - terminals, arr_len):
        if not is_zero_fac(points_static_out[0][ter_index]):
            _, a, b = div_fac(points_static_out[0][ter_index], reverse_fac(points_static_out[0][0]))
            result.append((a, b))
            lcom = lcommon(lcom, b)
        else:
            result.append((0, 1))
    result.append((lcom,lcom))
    return list(map(lambda (a, b): int(a * lcom/b), result))
