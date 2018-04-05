import datetime
kalender = [('nulmaand', range(1,1)),
            ('Januari', range(1, 31 + 1)),
            ('Februari', range(1, 28 + 1)),
            ('Maart', range(1, 31 + 1)),
            ('April', range(1, 30 + 1)),
            ('Mei', range(1, 31 + 1)),
            ('Juni', range(1, 30 + 1)),
            ('Juli', range(1, 31 + 1)),
            ('Augustus', range(1, 31 + 1)),
            ('September', range(1, 30 + 1)),
            ('Oktober', range(1, 31 + 1)),
            ('November', range(1, 30 + 1)),
            ('December', range(1, 31 + 1))]

kwartaal = [range(1,3+1),range(4,6+1), range(7,9+1), range(10,12+1)]

def maandVersieren(jaar, maand):
    daglijst = []
    maandoverzicht = []
     
    if is_schrikkel(jaar):
      kalender[2] = ('Februari', range(1, 29 + 1))

    dt =  datetime.date(jaar, maand, 1)
    index_start = dt.isoweekday()
    
    dt1 = datetime.date(jaar,maand,max(kalender[maand][1]))
    dow = dt1.isoweekday()
        
    for i in range (0, index_start-1):
         daglijst.append(' ')
         
    for i in kalender[maand][1]:
        daglijst.append(i)

    for i in range(0, 7-dow):
        daglijst.append(' ')
  
    aantal_weken = len(daglijst)//7
    daglijst.insert(0,dt.isocalendar()[1])
    for i in range(8, aantal_weken*7, 8):
        dt = datetime.date(jaar,maand,daglijst[i])
        daglijst.insert(i,dt.isocalendar()[1])

    aantal = 6*8 - len(daglijst)
    for i in range(0,aantal):
       daglijst.append(' ')
         
    return daglijst    
   
def kwartaalRegel(jaar,maand,regelnr):
    regel = []
    start =0
    eind = 8
    if regelnr > 0:
      start = regelnr * 8
      eind = (regelnr + 1) * 8 
           
    for mnd in kwartaal[maand-1]:
       maand = maandVersieren(jaar,mnd)
       regel = regel + maand[start:eind]
        
    return regel   

def kwartaalRegels(jaar,maand):
   
    matrix = [[0 for x in range(24)] for y in range(6)]
    
    for index in range(0,6):
       regel = kwartaalRegel(jaar,maand, index)
       matrix[index] = regel
    
    return matrix
 
def kwartaalAfdrukken(jaar,index, matrix):
    weekkop = ['wk', 'Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']
       
    for i in kwartaal[index-1]:
        print('{0:<24}'.format(kalender[i][0]+ " " + str(jaar)), end='')
    print()    
    
    for i in range(0,3):
        for dag in weekkop:
            print('{0:<3}'.format(dag), end='')
    print()
  
    for row in range(0, 6):
        for kol in range(0,24):
          print('{0:<3}'.format(matrix[row][kol]), end='')
        print()
  
def is_schrikkel(jaar):
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            if jaar % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

jaar = 2015
m1 = kwartaalRegels(jaar, 1)
kwartaalAfdrukken(jaar,1,m1)

m2 = kwartaalRegels(jaar, 2)
kwartaalAfdrukken(jaar,2,m2)
m3 = kwartaalRegels(jaar, 3)
kwartaalAfdrukken(jaar,3,m3)

m4 = kwartaalRegels(jaar, 4)
kwartaalAfdrukken(jaar,4,m4)


