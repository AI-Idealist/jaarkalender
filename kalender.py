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

week = ['wk', 'Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']
kwartaal = [range(1,4),range(4,7), range(7,10), range(10,13)]

def maand_versieren(jaar, maand):
   
    daglijst = []
     
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
    
    return daglijst


def kwartaal_versieren(jaar,start, eind):
   daglijsten = []
   for i in range(start,eind):
       
       daglijst = maand_versieren(jaar,i)
       daglijsten.append(daglijst)
   return daglijsten   

    
def print_kwartaal(daglijsten,jaar,index):
 
    spatie = " "
    for i in kwartaal[index-1]:
        print('{0:<25}'.format(kalender[i][0]+ " " + str(jaar)), end='')
    print()    
    
    for i in range(0,3):
        for dag in week:
            print('{0:<3}'.format(dag), end='')
        print(spatie, end='')
    
    print()

    
    for weekregel in range (0,8):
      for maand in range(0,3):
          if weekregel*8 < len(daglijsten[maand]): 
             print_week(daglijsten[maand],weekregel)
             print(spatie, end='')
          else:
             print('{0:<24}'.format(' '), end='') 
             print(spatie, end='')
      print()     
     
         
def print_week(daglijst, index):
   weekregel = [range(0,8), range(8,16),range(16,24), range(24,32), range(32,40),range(40,48)]
     
  
   for i in weekregel[index]:
      print('{0:<3}'.format(daglijst[i]), end='')

        
def is_schrikkel(jaar):
    """Checks if year is a leap year"""
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


daglijsten = []
jaar=int(input('Enter Year'))

dl = kwartaal_versieren(jaar,1,4)
print_kwartaal(dl,jaar,1)

dl = kwartaal_versieren(jaar,4,7)
print_kwartaal(dl,jaar,2)

dl = kwartaal_versieren(jaar,7,10)
print_kwartaal(dl,jaar,3)

dl = kwartaal_versieren(jaar,10,13)
print_kwartaal(dl,jaar,4)


