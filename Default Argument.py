def test(a=40,b=30,c=20,d=10): #d=10 is a default argument
    print("A:",a,'B:',b,'C;',c,'D:',d)

test(1,2,3)
test(1,2,3,4) #if I give d = 4 then priority will be given to 4 and not 10(defalut argument)
test(1,2)
test(1) # a ne argument aapvi hoy to b,c,d ne compulsorily defalut argumrnt aapvi padse
test()
test(b=100,d=200) #this is known as keyword argument