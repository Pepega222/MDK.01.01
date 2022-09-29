def angle(h,m,s):
    return (h%12) * 30 + m * 0.5 + s * 0.0083
print('''угол:''',angle(1,25,0))



