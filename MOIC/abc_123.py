alph = "abcdefghijklmnop"
st = input("ВВЕДИ СТРОКУ: ")
for i in alph:
    st = st.replace(i, str(alph.index(i) + 1))
st = st.replace('(', '{')
st = st.replace(')', '}')

print(st)


# {(a,b),(a,c),(b,c),(c,d),(c,g),(d,g),(d,e),(d,f),(g,h),(g,i),(f,e),(h,i)}
# (a,b),(a,c),(b,c),(c,d),(d,e),(e,f)
