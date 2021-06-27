def maior(a):
    if len(a) <= 1:
        m = a[0]
    else:
        m = a[0]
        for i in range(1,len(a)):
            if a[i]>m:
                m = a[i]

    return m