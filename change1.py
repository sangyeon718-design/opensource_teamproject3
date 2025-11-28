t=input("문자열 입력")
type=input("유형(ab=소문자로,AB=대문자로)")
if type=="ab":
    c=""
    for ch in t:
        c+=ch.lower()
    print(c)
elif  type =="AB":
    c=""
    for ch in t:
        c+=ch.upper()
    print(c)