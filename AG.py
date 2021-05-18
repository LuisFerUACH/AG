import numpy as np

def seleccionar(pobla, let2gen, gen2let):
    ordenada = sorted(pobla.items(), key = lambda x:x[1])
    suma =0
    for edo in ordenada:
        suma = suma + edo[1]
    probas =[]
    for edo in ordenada:
        probas.append(edo[1]/suma)
    cotas =[]
    antes =0.0
    for p in probas:
        cotas.append([antes, antes + p ])
        antes = antes + p
    r1 = np.random.uniform(0 ,1)
    r2 = np.random.uniform(0 ,1)
    indi =0
    for par in cotas:
        if r1 >= par[0] and r1 <= par[1]:
            indi1 = indi
            break
        indi = indi +1
    indi =0
    for par in cotas:
        if r2 >= par[0] and r2 <= par[1]:
            indi2 = indi
            break
        indi = indi +1
    padre = list(pobla)[indi1]
    madre = list(pobla)[indi2]
    padreGen = let2gen [padre]
    madreGen = let2gen [madre]
    return padre, padreGen, madre, madreGen

def formaDic(pobla, fs, let2gen, gen2let ):
    resp ={}
    for edo in pobla:
        resp[edo]= fs[edo]
    return resp

def getMejor(pobla, fs) :
    fmejor =0
    for edo in pobla:
        if fs[edo] > fmejor:
            fmejor = fs[edo]
            mejor = edo
    return mejor

def mutar(edo, let2gen, gen2let):
    gen = let2gen[edo]
    gen2 = list(gen)
    total =len(gen2)
    indi = np.random.randint(0, total)
    if gen2[indi]== '0':
        gen2[indi]= '1'
    else:
        gen2[indi]= '0'
    gen ="".join(gen2)
    letra = gen2let.get(gen)
    if not letra:
        letra ='B'
        gen ='101 '
    return gen , letra

def cruzar(padre, madre, let2gen, gen2let):
    genP = let2gen[padre]
    genM = let2gen[madre]
    genP2 = list(genP)
    genM2 = list(genM)
    total =len(genP2)
    indi = np.random.randint(0, total)
    padre1 = genP2 [: indi ]
    padre2 = genP2 [ indi :]
    madre1 = genM2 [: indi ]
    madre2 = genM2 [: indi ]
    hijo1 = padre1 + madre2
    hijo2 = padre2 + madre1
    genHijo1 ="". join(hijo1)
    genHijo2 ="". join(hijo2)
    letraHijo1 = gen2let.get(genHijo1)
    letraHijo2 = gen2let.get(genHijo2)
    if not letraHijo1:
        letraHijo1 ='B'
        genHijo1 ='101 '
    if not letraHijo2 :
        letraHijo2 ='B'
        genHijo2 ='101 '
    return letraHijo1 , genHijo1 , letraHijo2 , genHijo2

def aGen(ini, proble, fs, let2gen, gen2let):
    mejor = None
    maxItera =50
    itera =0
    pobla = list(fs.keys())
    total =len(pobla)
    while itera <= maxItera:
        nPtotal =0
        nPobla =[]
        while nPtotal < total:
            dicPobla = formaDic(pobla, fs, let2gen, gen2let)
            padre , genPadre , madre , genMadre = seleccionar(dicPobla,let2gen, gen2let)
            hijo1 , genHijo1 , hijo2 , genHijos2 = cruzar(padre, madre, let2gen, gen2let)
            hijo1m , genHijo1m = mutar(hijo1, let2gen, gen2let)
            hijo2m , genHijo12 = mutar(hijo2, let2gen, gen2let)
            nPobla.append(hijo1m)
            nPobla.append(hijo2m)
            nPtotal = nPtotal +2
        itera = itera +1
    mejor = getMejor(pobla,fs)
    return mejor

def main(ini):
    proble ={ 'A':[ 'B','C','D'] ,'B':[ 'A','C','E','F'] ,
              'C':[ 'A','B','D','F','G'] ,'D':[ 'A','C','G','K'] ,
              'E':[ 'B','F','I','H'] ,'F':[ 'B','C','E','I','G'],
              'G':[ 'D','C','F','I','J','K'] ,'H':[ 'E','I','L'] ,
              'I':[ 'E','F','H','L','J'] ,'J':[ 'I','G','M','N','K'] ,
              'K':[ 'D','G','J','N'] ,'L':[ 'I','H','M'] ,
              'M':[ 'L','J','N'] ,'N':[ 'M','J','K']}
 ## La representacion genetica de cada estado
    let2gen = {'A':'0000', 'B':'0001', 'C':'0010',
		   'D':'0011', 'E':'0100', 'F':'0101',
		   'G':'0110', 'H':'0111', 'I':'1000',
		   'J':'1001', 'K':'1010', 'L':'1011',
		   'M':'1100', 'N':'1101'}
    gen2let ={'0000':'A', '0001':'B', '0010':'C',
		   '0011':'D', '0100':'E', '0101':'F',
		   '0110':'G', '0111':'H', '1000':'I',
		   '1001':'J', '1010':'K', '1011':'L',
		   '1100':'M', '1101':'N'}
## La altura de cada estado
    fs ={ 'A':25 , 'B':20, 'C':23 , 'D':18 , 'E':12 , 'F':23, 'G':15, 'H':15, 'I':16, 'J':5, 'K':25, 'L':25, 'M':3, 'N':12}
    mejor = aGen (ini, proble , fs , let2gen , gen2let )
    print ('El mejor estado partiendo de ' + ini + ' es ' + mejor )

if __name__ == '__main__':
    indi = np.random.randint(1, 15)
    nodoInicial = ''
    if indi==1:
        nodoInicial = 'A'
    elif indi==2:
        nodoInicial = 'B'
    elif indi==3:
        nodoInicial = 'C'
    elif indi==4:
        nodoInicial = 'D'
    elif indi==5:
        nodoInicial = 'E'
    elif indi==6:
        nodoInicial = 'F'
    elif indi==7:
        nodoInicial = 'G'
    elif indi==8:
        nodoInicial = 'H'
    elif indi==9:
        nodoInicial = 'I'
    elif indi==10:
        nodoInicial = 'J'
    elif indi==11:
        nodoInicial = 'K'
    elif indi==12:
        nodoInicial = 'L'
    elif indi==13:
        nodoInicial = 'M'
    elif indi==14:
        nodoInicial = 'N'
    main(nodoInicial)