def test(a,b,c,*d,**e): #** vadi argument mate hamesha dictionary bani jase
    print("A:",a,'B:',b,'C;',c,'D:',d,'E:',e)

test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)#4 pa6i ni badhi argument mate tuple banai lese
#dynamic tuple argument is known as arbitrary argument
#arbitrary argument hamesha last ma j thay
#** pan j arbitrary argument j 6
#** last ma aavse and *eni pehla aave