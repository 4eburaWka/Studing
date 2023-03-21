alph = "abcdefghijklmnop"
st = input("ВВЕДИ СТРОКУ: ")
for i in alph:
    st = st.replace(i, str(alph.index(i) + 1))
st = st.replace('(', '{')
st = st.replace(')', '}')

print(st)



