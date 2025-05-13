def solution(s):
    answer = -1

    st = []

    for i in s:
        if len(st) and st[-1] == i:
            st.pop()
            continue
        st.append(i)

    if len(st) == 0:
        return 1
    else:
        return 0