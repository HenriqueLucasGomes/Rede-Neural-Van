#coding: utf-8
#author Henrique Lucas Gomes Rezende
import kivy
kivy.require("1.9.1")
from kivy.app import App
import sqlite3
from random import uniform,randint

#conn=sqlite3.connect(r"/storage/emulated/0/kivy/RN Van-Meu-Jeito/pesos.db")
#conn=sqlite3.connect(r"C:\dev\eXcript\kivy\source\projetos\RN Van-Meu-Jeito\pesos.db")
conn=sqlite3.connect(r"/home/henrique/projetos/RN Van-Meu-Jeito/Rede-Neural-Van/pesos.db")

cursor = conn.execute("select GE from PESOS")
ge=cursor.fetchall()
if(ge==[]):
    ge=1
else:
    ge=int(ge[0][0])

#qtd=int(input("Quanridade de pesoas:"))
qtd=5
class Neuronio():
    def __init__(self,tipo,rede,ide):
        cursor = conn.execute("select ID from PESOS where ID="+str(ide))
        rows = cursor.fetchall()
        self.ide = ide
        if(rows==[]):
            conn.execute("insert into PESOS(GE,TI,RE,BI,P1,P2,P3,P4) values('" + str(ge) + "','" + str(tipo) + "','" + str(rede) + "'," + str(uniform(1, 0)) +","+ str(uniform(1, 0)) +","+ str(uniform(1, 0))+","+ str(uniform(1, 0))+","+ str(uniform(1, 0))+")")
            conn.commit()
            # if(tipo>1 or ide==(((r-1)*50)+1)):
            #     if(tipo==2):
            #         conn.execute("update PESOS set P3="+str(uniform(1,0))+" where ID="+str(self.ide))
            #         conn.commit()
            #     else:
            #         conn.execute("update PESOS set P3=" + str(uniform(1,0)) +",P4="+str(uniform(1,0))+" where ID=" + str(self.ide))
            #         conn.commit()
    def processamento(self,*args):
        c=0
        cursor = conn.execute("select BI from PESOS where ID=" + str(self.ide))
        rows = cursor.fetchall()
        print("ID: "+str(self.ide))
        res=-0.5*rows[0][0]
        print("Bias:"+str(res))
        for i in args:
            c+=1
            cursor=conn.execute("select P"+str(c)+" from PESOS where ID="+str(self.ide))
            rows = cursor.fetchall()
            print("P"+str(c)+":" + str(rows[0][0]))
            res+=(i*rows[0][0])
            #print(res)
        print(res)
        if(res>=0):
            if(res>1):
                return (1,1)
            else:
                return (1,res)
        elif(res<0):
            return (0,0)

def entrada(t,r,v1,v2):
    a1=Neuronio(t,r,(((r-1)*50)+1))
    a2=Neuronio(t,r,(((r-1)*50)+2))
    r1=a1.processamento(v1,v2)[1]
    r2=a2.processamento(v1,v2)[1]
    a3=Neuronio(t,r,(((r-1)*50)+3))
    a4=Neuronio(t,r,(((r-1)*50)+4))
    r3=a3.processamento(r1,r2)[1]
    r4=a4.processamento(r1,r2)[1]
    a5=Neuronio(t,r,(((r-1)*50)+5))
    r=a5.processamento(r3,r4)[1]
    #print(r)
    return r

def frente(t,r,v1,v2):
    a1 = Neuronio(t, r,(((r-1)*50)+6))
    a2 = Neuronio(t, r,(((r-1)*50)+7))
    r1 = a1.processamento(v1, v2)[1]
    r2 = a2.processamento(v1, v2)[1]
    a3 = Neuronio(t, r,(((r-1)*50)+8))
    a4 = Neuronio(t, r,(((r-1)*50)+9))
    r3 = a3.processamento(r1, r2)[1]
    r4 = a4.processamento(r1, r2)[1]
    a5 = Neuronio(t, r,(((r-1)*50)+10))
    r = a5.processamento(r3, r4)[1]
    #print(r)
    return r

def resolucaoAt(t,re,*l):
    # a1 = Neuronio(t+1, re,(((re-1)*50)+54))#retirar
    # a2 = Neuronio(t+1, re,(((re-1)*50)+55))#retirar
    # a3 = Neuronio(t+1, re,(((re-1)*50)+56))#retirar
    # a4 = Neuronio(t+1, re,(((re-1)*50)+57))#retirar
    # r1 = a1.processamento(l[0], l[1], l[2],l[3])[1]#retirar
    # r2 = a2.processamento(l[0], l[1], l[2],l[3])[1]#retirar
    # r3 = a3.processamento(l[0], l[1], l[2],l[3])[1]#retirar
    # r4 = a4.processamento(l[0], l[1], l[2],l[3])[1]#retirar
    a1 = Neuronio(t+1, re,(((re-1)*50)+41))
    a2 = Neuronio(t+1, re,(((re-1)*50)+42))
    a3 = Neuronio(t+1, re,(((re-1)*50)+43))
    a4 = Neuronio(t+1, re,(((re-1)*50)+44))
    r1 = a1.processamento(l[0], l[1], l[2],l[3])[1]
    r2 = a2.processamento(l[0], l[1], l[2],l[3])[1]
    r3 = a3.processamento(l[0], l[1], l[2],l[3])[1]
    r4 = a4.processamento(l[0], l[1], l[2],l[3])[1]
    a5 = Neuronio(t+1, re,(((re-1)*50)+45))
    a6 = Neuronio(t+1, re,(((re-1)*50)+46))
    a7 = Neuronio(t+1, re,(((re-1)*50)+47))
    r5 = a5.processamento(r1, r2, r3, r4)[1]
    r6 = a6.processamento(r1, r2, r3, r4)[1]
    r7 = a7.processamento(r1, r2, r3, r4)[1]
    a8 = Neuronio(t, re,(((re-1)*50)+48))
    a9 = Neuronio(t, re,(((re-1)*50)+49))
    r8 = a8.processamento(r5, r6, r7)[1]
    r9 = a9.processamento(r5, r6, r7)[1]
    a10 = Neuronio(t-1, re,(((re-1)*50)+50))
    r = a10.processamento(r8, r9)[1]
    return r


def atras(t,re,*l):
    lisRes=[]
    c=0
    while(c<9):
        # a1 = Neuronio(t,re,(((re-1)*50)+11+(10*c/3)))#retirar
        # a2 = Neuronio(t,re,(((re-1)*50)+12+(10*c/3)))#retirar
        # a3 = Neuronio(t,re,(((re-1)*50)+13+(10*c/3)))#retirar
        # r1 = a1.processamento(l[c],l[c+1],l[c+2])[1]#retirar
        # r2 = a2.processamento(l[c],l[c+1],l[c+2])[1]#retirar
        # r3 = a3.processamento(l[c],l[c+1],l[c+2])[1]#retirar
        a1 = Neuronio(t,re,(((re-1)*50)+11+(7*c/3)))
        a2 = Neuronio(t,re,(((re-1)*50)+12+(7*c/3)))
        a3 = Neuronio(t,re,(((re-1)*50)+13+(7*c/3)))
        r1 = a1.processamento(l[c],l[c+1],l[c+2])[1]
        r2 = a2.processamento(l[c],l[c+1],l[c+2])[1]
        r3 = a3.processamento(l[c],l[c+1],l[c+2])[1]
        a4 = Neuronio(t,re,(((re-1)*50)+14+(7*c/3)))
        a5 = Neuronio(t,re,(((re-1)*50)+15+(7*c/3)))
        a6 = Neuronio(t,re,(((re-1)*50)+16+(7*c/3)))
        r4 = a4.processamento(r1, r2, r3)[1]
        r5 = a5.processamento(r1, r2, r3)[1]
        r6 = a6.processamento(r1, r2, r3)[1]
        a7 = Neuronio(t,re,(((re-1)*50)+17+(7*c/3)))
        r = a7.processamento(r4, r5, r6)[1]
        lisRes+=[r]
        #print(r)
        c+=3
    # a1 = Neuronio(t, re,(((re-1)*50)+41))#retirar
    # a2 = Neuronio(t, re,(((re-1)*50)+42))#retirar
    # a3 = Neuronio(t, re,(((re-1)*50)+43))#retirar
    # a4 = Neuronio(t, re,(((re-1)*50)+44))#retirar
    # r1 = a1.processamento(l[9], l[10], l[11])[1]#retirar
    # r2 = a2.processamento(l[9], l[10], l[11])[1]#retirar
    # r3 = a3.processamento(l[9], l[10], l[11])[1]#retirar
    # r4 = a4.processamento(l[9], l[10], l[11])[1]#retirar
    a1 = Neuronio(t+1, re,(((re-1)*50)+32))
    a2 = Neuronio(t+1, re,(((re-1)*50)+33))
    a3 = Neuronio(t+1, re,(((re-1)*50)+34))
    a4 = Neuronio(t+1, re,(((re-1)*50)+35))
    r1 = a1.processamento(l[9], l[10], l[11])[1]
    r2 = a2.processamento(l[9], l[10], l[11])[1]
    r3 = a3.processamento(l[9], l[10], l[11])[1]
    r4 = a4.processamento(l[9], l[10], l[11])[1]
    a5 = Neuronio(t+1, re,(((re-1)*50)+36))
    a6 = Neuronio(t+1, re,(((re-1)*50)+37))
    a7 = Neuronio(t+1, re,(((re-1)*50)+38))
    a8 = Neuronio(t+1, re,(((re-1)*50)+39))
    r5 = a5.processamento(r1, r2, r3,r4)[1]
    r6 = a6.processamento(r1, r2, r3,r4)[1]
    r7 = a7.processamento(r1, r2, r3,r4)[1]
    r8 = a8.processamento(r1, r2, r3,r4)[1]
    a13 = Neuronio(t+1, re,(((re-1)*50)+40))
    r = a13.processamento(r5, r6, r7,r8)[1]
    lisRes+=[r]
    r=resolucaoAt(t,re,*lisRes)
    return r

#l=[[0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0,0]]


def redes():
    global lc
    global dicRes
    lc = [[0.5, 0.5], [1, 0.5, 0.5], [1, 0.5, 0.5], [1, 0.5, 0.5], [1, 0.5, 0.5,1]]
    dicRes = {}
    pri = 0
    r = 0
    while(pri<12):
        c = 0
        dicRes[pri] = [[0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]]
        r+=1
        while(c<qtd):
            ent=entrada(1,r,0.5,0.5)
            fre=frente(1,r,dicRes[pri][0][0],dicRes[pri][0][1],)
            #at = atras(2, r, 0, 0, 0,   0, 0, 0,   0, 0, 0,   0, 0, 0, 0)
            at = atras(2, r, dicRes[pri][1][0],dicRes[pri][1][1],dicRes[pri][1][2],
                       dicRes[pri][2][0],dicRes[pri][2][1],dicRes[pri][2][2],
                       dicRes[pri][3][0],dicRes[pri][3][1],dicRes[pri][3][2],
                       dicRes[pri][4][0],dicRes[pri][4][1],dicRes[pri][4][2],dicRes[pri][4][3])
            #print(dicRes[pri])
            print("Entrada:"+str(ent))
            print("Fente:"+str(fre))
            print("Atras:"+str(at))
            if(ent>0.5):
                print("vai na frente")
                if(fre>0.5):
                    print("primeiro")
                    dicRes[pri][0][0]=1
                else:
                    print("segundo")
                    dicRes[pri][0][1]=1
            else:
                print("vai atras")
                if(at<0.25):
                    print("primeira fileira")
                    cursor = conn.execute("select P3 from PESOS where ID=" + str((((r - 1) * 50) + 1)))
                    rows = cursor.fetchall()
                    at *= rows[0][0]
                    if(at<1/3):
                        print("primeiro lugar")
                        dicRes[pri][1][0] = 1
                    elif(at<2/3):
                        print("segundo lugar")
                        dicRes[pri][1][1] = 1
                    else:
                        print("terceiro lugar")
                        dicRes[pri][1][2] = 1
                elif(at<0.5):
                    print("segunda fileira")
                    cursor = conn.execute("select P3 from PESOS where ID=" + str((((r - 1) * 50) + 1)))
                    rows = cursor.fetchall()
                    at *= rows[0][0]
                    if (at < 1 / 3):
                        print("primeiro lugar")
                        dicRes[pri][2][0] = 1
                    elif (at < 2 / 3):
                        print("segundo lugar")
                        dicRes[pri][2][1] = 1
                    else:
                        print("terceiro lugar")
                        dicRes[pri][2][2] = 1
                elif(at<0.75):
                    print("terceira fileira")
                    cursor = conn.execute("select P3 from PESOS where ID=" + str((((r - 1) * 50) + 1)))
                    rows = cursor.fetchall()
                    at *= rows[0][0]
                    if (at < 1 / 3):
                        print("primeiro lugar")
                        dicRes[pri][3][0] = 1
                    elif (at < 2 / 3):
                        print("segundo lugar")
                        dicRes[pri][3][1] = 1
                    else:
                        print("terceiro lugar")
                        dicRes[pri][3][2] = 1
                else:
                    print("quarta fileira")
                    cursor = conn.execute("select P3 from PESOS where ID=" + str((((r-1)*50)+1)))
                    rows = cursor.fetchall()
                    at*=rows[0][0]
                    if (at < 0.25):
                        print("primeiro lugar")
                        dicRes[pri][4][0] = 1
                    elif (at <0.5):
                        print("segundo lugar")
                        dicRes[pri][4][1] = 1
                    elif (at <0.75):
                        print("terceiro lugar")
                        dicRes[pri][4][2] = 1
                    else:
                        print("quarto lugar")
                        dicRes[pri][4][3] = 1
            print(dicRes[pri])
            c+=1
        pri+=1

def registra(i,c,f,mp,g,taxa):
    # if(raz):
    #     raz=uniform(1,0)
    # else:
    #     raz=0
    if (taxa>0 and taxa<0.01):# des==0.5/des>0.5
        conn.execute("update PESOS set " + str(i) + "=" + str(uniform(1, 0)) + " , GE=" + str((g)) + " where ID=" + str((50 * c) + f + 1))
        conn.commit()#mutação
        # conn.execute("update PESOS set GE='" + str((g)) + "' where ID=" + str((50 * c) + f + 1))
        # conn.commit()
        print("ISSO:" + str((50 * c) + f + 1))
    else:
        conn.execute("update PESOS set " + str(i) + "=" + str(mp[i][f][0]) +" , GE=" + str((g)) + " where ID=" + str((50 * c) + f + 1))
        conn.commit()
        # conn.execute("update PESOS set GE='" + str((g)) + "' where ID=" + str((50 * c) + f + 1))
        # conn.commit()
        print("ISSO:" + str((50 * c) + f + 1))

def crossing(pai,mae,dic):
    g=int(ge)
    g = g+1
    p = {}
    m = {}
    cursor = conn.execute("select BI from PESOS")
    p['bi'] = cursor.fetchall()[((pai * 50)):((pai * 50) + 50)]
    cursor = conn.execute("select BI from PESOS")
    m['bi'] = cursor.fetchall()[((mae * 50)):((mae * 50) + 50)]
    cursor = conn.execute("select P1 from PESOS")
    p['p1'] = cursor.fetchall()[((pai * 50)):((pai * 50) + 50)]
    cursor = conn.execute("select P1 from PESOS")
    m['p1'] = cursor.fetchall()[((mae * 50)):((mae * 50) + 50)]
    cursor = conn.execute("select P2 from PESOS")
    p['p2'] = cursor.fetchall()[((pai * 50)):((pai * 50) + 50)]
    cursor = conn.execute("select P2 from PESOS")
    m['p2'] = cursor.fetchall()[((mae * 50)):((mae * 50) + 50)]
    cursor = conn.execute("select P3 from PESOS")
    p['p3'] = cursor.fetchall()[((pai * 50)):((pai * 50) + 50)]
    cursor = conn.execute("select P3 from PESOS")
    m['p3'] = cursor.fetchall()[((mae * 50)):((mae * 50) + 50)]
    cursor = conn.execute("select P4 from PESOS")
    p['p4'] = cursor.fetchall()[((pai * 50)):((pai * 50) + 50)]
    cursor = conn.execute("select P4 from PESOS")
    m['p4'] = cursor.fetchall()[((mae * 50)):((mae * 50) + 50)]

    c = 0
    a1=p['p1'][4][0] * m['p1'][4][0]

    while (c < 12):
        print("OLHA:"+str(c))
        f = 0#TEMOS ALGUNS PROBLEMAS COM ISSO AQUI!!!!->ele não ta aprendendo direito
        if(randint(0,1)>0.5):#vai mutar
            raz=True
        while (f < 50):
            for i, k in m.items():
                if ( a1> 0.5):
                    registra(i, c, f, p, g,uniform(1,0))
                    # if (int(dic[pai])>=2000):#int(dic[pai])==1000
                    #     registra(i,c,f,p,g,raz)# randint(0, 1)/uniform(1,0)
                    # else:
                    #     if(randint(0,1)==0):
                    #         registra(i,c,f,p,g,raz)
                    #     else:
                    #         registra(i,c,f,p,g,raz)
                else:
                    registra(i, c, f, m, g, uniform(1, 0))
                    # if (int(dic[mae])>=2000):
                    #     registra(i,c,f,p,g,raz)# randint(0, 1)
                    # else:
                    #     if(randint(0,1)==0):
                    #         registra(i,c,f,m,g,raz)#0.6
                    #     else:
                    #         registra(i,c,f,m,g,raz)#0.4

            f += 1
        c += 1



def selecao():
    print("--->")
    print(dicRes)
    dic={}
    q=0
    while(q<12):
        ver = 0
        erro = 0
        for i in dicRes[q]:
            for k in i:
                if (k == 1):
                    ver += 1
                    print("--->"+str(ver))
        if(ver!=qtd):
            erro=(qtd-ver)*1000
        else:
            c=0
            f=0
            while(c<len(dicRes[q])):
                while(f<len(dicRes[q][c])):
                    if(dicRes[q][c][f]!=lc[c][f]):
                        #print("ta aqui")
                        erro+=1
                    f+=1
                f=0
                c+=1
        dic[q]=erro
        q+=1
    print("---->")
    print(dic)
    m1=dic[0]
    m2=dic[0]
    v1 = 0
    v2 = 0
    for i, k in dic.items():
        if (m1 > k):
            v1 = i
            m1 = k
    if (v1 == 0):
        m2 = dic[1]
    for i, k in dic.items():
        if (m2 >= k and i != v1):
            v2=i
            m2 = k
    print(str(v1)+" "+str(v2))
    #raz=True
    # if(dic[v1]==dic[v2]):
    #     print("É igual")
    #     crossing(v1,v2,dic,raz)
    # elif(dic[v1]<dic[v2]):
    #     print("Não é igual")
    #     krf=300
    #     crossing(v1,v1,dic,raz)
    # else:
    #     print("Não é igual")
    #     krf=300
    #     crossing(v2,v2,dic,raz)
    #----------------------------
    # if(v1<1000 or v2 <1000):
    #     raz=False
    #     crossing(v1, v2, dic,raz)
    # else:
    #     crossing(v1, v2, dic,raz)
    crossing(v1, v2, dic)

class VanApp(App):
    pass

#r=VanApp()
#r.run()
kfr=0
while(kfr<300):
    redes()
    selecao()
    cursor = conn.execute("select GE from PESOS")
    ge = cursor.fetchall()[0][0]
    kfr+=1


#SÃO 50 REGISTROS FEITOS NA TABELA PARA UMA REDE NEURAL COMPLETA
#print(atras(1,1, 1,1,1 ,1,1,1 ,1,1,1 ,1,1,1,1))

# c=Neuronio()
# c.ide=1
# print(c.processamento(1,1,1,1,1))

conn.close()










