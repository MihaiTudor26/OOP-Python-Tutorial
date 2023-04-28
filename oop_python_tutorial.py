#|------------------------------Object-Oriented Programming--------------------



#1.Notiuni de baza:

"""
-problema pricipala in cazul programarii clasice este faptul ca
o modificare a unei parti din program,se resfrange si in alte locuri din program.
-progrmarea orientata pe obiecte are marele avantaj oferit de mecanismul de
incapsulare care presupune spargerea programului in mai multe piese,iar fiecare piesa opereaza i
ndependent de celelate.
-piesele interactioneaza intre ele insa fara a fi nevoie sa stie cum isi realizeaza celelalte task-urile
-python este un limbaj de programare orientat pe obiecte
-notiunea de baza este cea de OBIECT 
-vom numi obiectele si instante
-orice obiect poate contine atribute si metode
-functiile din interiourul clasei le numim metode
"""

#2.Crearea unei clase

"""
Ex: Cream clasa student"""

class Student:
    pass
x=Student()#obiect
y=Student()#obiect
z=x#z este o referinta(alias) pentru x
print(x==y)#afiseaza False deoarece x,y fiind obiecte diferite
print(x==z)#afiseaza True dearece z,x sunt unul si acelasi obiect

#3.Atribute ale clasei

"""
-vom putea adauga obiectelor create atributul (proprietatea) 'nume'
-atributele pot fi create atat in interiorul unei clase
cat si dinamic asa cum vom proceda in exemplul urmator"""

x.nume="ana"#nume este un atribut pentru obiectul x
y.nume="mircea"#nume este un atribut pentru obiectul y
print("Nume: ",x.nume)
print("Nume: ",y.nume)

#-determinarea atributelor si valorilor unui anumit obiect

"""
-pentru a detrmina atributele precum si valorile unui anumit obiect
putem folosi o metoda speciala __dict__"""

print("Dictionarul cu atributele obiectului x: ",x.__dict__)

#-legarea atributelor unei clase de functiile din afara clasei

"""
-obiectele unei clase pot fi legate si de functiile din afara clasei
-in acest sens consideram exemplul urmator"""

def salut(x):
    print("Salut, eu sunt ",x.nume)
salut(x)    

"""
-recomandat este ca functiile sa fie definite in interirorul clasei
numindu-le metode
-primul argument al fiecarei metode din clasa este o variabila
speciala numita "self"
-de fiecare data cand ne referim la o metoda sau o variabila a clasei
acesta trebuie sa aiba in fata sa "self."
-"self" are rolul de a distinge variabilele si metodele clasei de celelate
variabile si metode din program"""

#-Atribute publice, private, protejate

"""
In OOP exista trei tipuri de atribute:
-atribute private=pot fi folosite doar in interiorul clasei de definitie
-atribute protejate=pot fi folosite doar in subclase ale clasei de definitie
-atribute publice=pot fi utilizate fara nicio restrictie atat in interiorul clasei cat si in afara ei

Mod de definire:
         _NumeAtribut=atribut protejat
        __NumeAtribut=atribut privat
"""

#-metoda __init__

"""
-__init__ este o metoda speciala(avand __)numita constructor sau magic method
-aceasta este automat apelata cand se creaza un obiect
-constructorul este folosit pentru a seta variabilele clasei
"""

#Ex1. Implementarea clasei 'Curs'
class Curs:
    def __init__(self,id_curs=None):
        self.id_curs=id_curs
    def selectie_grupa(self):
        if self.id_curs=='#113':
            print("Sunteti repartizati in grupa 1")
        else:
            print("Sunteti repartizati in grupa 2")
student=Curs()
student.id_curs="#113"
student.selectie_grupa()
        
#Ex2. Implementarea clasei 'Fractie'-contine metode pentru adunarea si inmultirea fractilor
class Fractie:
    def __init__(self,numitor=None,numarator=None):
        self.numitor=numitor
        self.numarator=numarator
    def show(self):
        if self.numitor!=0:
            print("Numitorul fractiei este: ",self.numitor)
        else:
            print("Valoare invalida")
        if self.numarator:
            print("Numaatorul fractiei este: ",self.numarator)
        else:
            print("Valoare invalida")
    def adunare(self,a):
        if self.numitor==a.numitor:
            return (self.numarator+a.numarator)/a.numitor
        else:
            return (self.numarator*a.numitor+a.numarator*self.numitor)/(a.numitor*self.numitor)
    def inmultire(self,a):
        return (self.numarator*a.numarator)/(self.numitor*a.numitor)

o1=Fractie(2,3)
o2=Fractie(7,5)
print("Suna celor doua fractii este: ",o1.adunare(o2))
print("Produsul celor doua fractii este: ",o1.inmultire(o2))
print(o1.__dict__)#dictionar cu atribute si valori pentru primul obiect
print(o2.__dict__)#dictionar cu atribute si valori pentru al doilea obiect

#-metoda  __str__

"""
-metoda speciala folosita in afisaj"""

#Ex. Vom crea o clasa numita 'Invest'. 
"""
Constructorul va contine doua campuri:
-investitie
-rata anuala
Va exista o metoda ce va calcula suma avuta dupa n ani.
Va exista si o metoda de afisare."""

class Invest:
    def __init__(self,investitie,rata):
        self.investitie=investitie
        self.rata=rata
    def suma(self,ani):
        return self.investitie*((1+self.rata/100)**ani)
    def __str__(self):
        return "Suma investita este de "+str(self.investitie)+"$"+" cu o dobanada anuala egala cu "+str(self.rata)+"%"

inv=Invest(1000,10)
print(str(inv))
print(inv.suma(3))

#-metoda __del__

"""
-un obiect/instanta creata poata fi stearsa folosind metoda __del__
-pentru a fi sters, obiectul trebuie sa apeleze explicit aceasta metoda """

class Destructor:
    def __init__(self,grupa,medie):
        self.grupa=grupa
        self.medie=medie
    def __str__(self):
        return "Studentul este in grupa "+str(self.grupa)+" avand media "+str(self.medie)
    def __del__(self):
        print("Ati sters obiectul folosit")
g=Destructor(2,9.78)
print(str(g))
del g
#print(str(g))#vom primi o eroare, obiectul g fiind deja sters   


#4.Inheritance
"""
-ne permite sa cream clase care 'mostenesc' toate functiile si atributele unei clase construite inainte
"""

#Ex:

class Masina:#-clasa 'parinte'
    def __init__(self,nume,pret):
        self.nume=nume
        self.pret=pret
    def f1(self):
        print("Ati achitionat autoturismul ",self.nume," la pretul ",self.pret,"$.")
auto=Masina("Dacia Logan",7350)
auto.f1()

class Fabricatie(Masina):#-'child class'
    def __init__(self,nume,pret,an):
        super().__init__(nume,pret)
        self.an=an
    def f2(self):
        print("Anul de fabricatie pentru autoturismul achizitionat:",self.an)    
auto1=Fabricatie("Dacia Duster",9500,2015)
auto1.f1()
auto1.f2()

"""
-in 'child class' se pot adauga noi functii
-pentru a adauga noi atribute in 'child class' utilizam constructorul  __init__
rescriind proprietatile din 'parent class' la care adaugam noile atribute
-super() ne permite sa pastram in constructorul din 'child class', proprietatile din 'parent class'
"""

#|--------------------------------------------------------------------------------------------------------------



