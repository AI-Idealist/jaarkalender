import datetime
calender = [('nulmaand', range(1,1)),
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

def maak_maand(jaar, maand):
   
    daglijst = []
     
    if is_leap(jaar):
        calender[2] = ('Februari', range(1, 29 + 1))

    dt =  datetime.date(jaar, maand, 1)
        
    index_start = dt.isoweekday()
    
    dt1 = datetime.date(jaar,maand,max(calender[maand][1]))
    dow = dt1.isoweekday()
        
    for i in range (0, index_start-1):
         daglijst.append(' ')
         
    for i in calender[maand][1]:
        daglijst.append(i)

    for i in range(0, 7-dow):
        daglijst.append(' ')

    aantal_weken = len(daglijst)//7
    for i in range(1, aantal_weken*7, 8):
        if daglijst[i] == ' ': 
            j = 0
            while daglijst[i+j-1] == ' ': #iterate over first zeros of the month to get first real date
               j += 1
            dt = datetime.date(jaar,maand,daglijst[i+j-1])   
        else:
            dt = datetime.date(jaar,maand,daglijst[i])
        dow = dt.isocalendar()[1]
        daglijst.insert(i-1,dow)
    
    
    return daglijst
    
def print_kwartaal(daglijsten,jaar,index):

    if index == 1:
       start = 1
       eind = 4
    elif index == 2:
       start = 4
       eind = 7
    elif index == 3:
       start = 7
       eind = 10   
    elif index == 4:
       start = 10
       eind = 13   
    
    spatie = " "
    for i in range(start,eind):
        print('{0:<25}'.format(calender[i][0]+ " " + str(jaar)), end='')
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
     
         
def print_week(daglijst, weekregel):
   start = 0
   eind = 8
   
   if weekregel == 1:
      start = 8
      eind = 16
   elif weekregel == 2:
      start = 16
      eind =24
   elif weekregel == 3:
      start = 24
      eind =32
   elif weekregel == 4:
      start = 32
      eind =40
   elif weekregel == 5:
      start = 40
      eind =48  
   
   for i in range(start,eind):
      print('{0:<3}'.format(daglijst[i]), end='')

        
def is_leap(jaar):
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


def maak_kwartaal(jaar,start, eind):
   daglijsten = []
   for i in range(start,eind):
       
       daglijst = maak_maand(jaar,i)
       daglijsten.append(daglijst)
   return daglijsten   

daglijsten = []
jaar=int(input('Enter Year'))

dl = maak_kwartaal(jaar,1,4)
print_kwartaal(dl,jaar,1)

dl = maak_kwartaal(jaar,4,7)
print_kwartaal(dl,jaar,2)

dl = maak_kwartaal(jaar,7,10)
print_kwartaal(dl,jaar,3)

dl = maak_kwartaal(jaar,10,13)
print_kwartaal(dl,jaar,4)


