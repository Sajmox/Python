import os
clear = lambda: os.system("cls")
dostepne_sniadania = []
dostepne_obiady = []

############# Lista składników na śniadania:
skladniki_sniadanie = ["jajko","pomidor","cebula","czosnek","płatki owsiane","jogurt naturalny","płatki",
                       "mleko","pieczywo","mąka","dżem","biała fasola","seler","grzyby","musztarda","majeranek",
                      "oliwa","ocet balsamiczny","rzodkiewka","szczypiorek","śmietana 18%","olej",
                      "proszek do pieczenia","ser","bułka tarta","nutella"]
skladniki_obiad = ["szpinak","makaron","cebula","czosnek","śmietana 18%","śmietanka 30","cytryna","parmezan",
                   "gałka muszkatałowa","tofu","pomidor","cukinia","bakłażan","ser pleśniowy","ser gorgonzola","ser rokpol",
                   "ser żółty","ser wędzony","jajko","mąka","ser mozarella","ser feta","twaróg","makaron ryżowy","ryż",
                   "kiełki fasoli mung","szczypiorek","orzeszki ziemne","chilli","sos pad thai","oliwa","sałata","wege burger",
                   "naleśnik wrap","pieczywo","warzywa","marchewka","pietruszka","seler","sos sojowy","por","natka pietruszki",
                   "papryka","mleko","pieczarki","masło orzechowe","imbir","ziemniak","bulion","makaron lazania","soczewica"]

############# Lista obiadów:
makaron_ze_szpinakiem = ["makaron ze szpinakiem","makaron","szpinak","cebula","czosnek","cytryna","śmietanka 30","parmezan"]
makaron_pomidory_tofu_warzywa = ["makaron w pomidorach, z tofu i warzywami","warzywa","pomidor","tofu","makaron"]
pad_thai = ["pad thai","makaron ryżowy","czosnek","tofu","jajko","kiełki fasoli mung","szczypiorek","orzeszki ziemne","sos pad thai"]
aglio_e_olio = ["aglio e olio","makaron","oliwa","czosnek","chilli","natka pietruszki","jajko","parmezan"]
nalesniki_ze_szpinakiem = ["naleśniki ze szpinakiem","mleko","mąka","jajko","szpinak","smietanka 30","czosnek"]
veggie_burger = ["veggie burgery","wege burger","ser żółty","pomidor","cebula","sałata"]
tortilla = ["tortilla","naleśnik wrap","warzywa","tofu"]
zapiekanka = ["zapiekanka","pieczywo","ser żólty","pieczarki"]
rosol = ["rosół","sos sojowy","cebula","marchewka","pietruszka","seler","por","natka pietruszki","makaron"]
wege_ramen = ["wege ramen","sos sojowy","cebula","marchewka","pietruszka","seler","por","natka pietruszki","masło orzechowe","szczypiorek","jajko","czosnek","makaron"]
krem_zbialych_warzyw = ["krem z białych warzyw","kalafior","por","cebula","ziemniak","seler","pietruszka","czosnek","bulion","śmietana 18%"]
krem_zpomidorow = ["krem z pomidorów","pomidor","cebula","czosnek","bulion"]
kalafior_pod_beszamelem = ["kalafior pod beszamelem","kalafior","mąka","mleko","ser żółty"]
kopytka = ["kopytka","ziemniak","mąka","jajko"]
wege_lazania = ["wege lazania","makaron lazania"]

############# Lista śniadań:
szakszuka = ["szakszuka","jajko","pomidor","cebula","czosnek"]
owsianka = ["owsianka","płatki owsiane","jogurt naturalny"]
platki = ["płatki na mleku","płatki","mleko"]
jajko_sadzone = ["jajko sadzone","jajko"]
jajko_namiekko = ["jajko na miekko","jajko","pieczywo"]
jajecznica = ["jajecznica","jajko","pieczywo"]
nalesniki_zdzemem = ["naleśniki z dźemem","mleko","mąka","jajko","dżem"]
pasztet_zfasoli = ["pasztet z fasoli","biała fasola","seler","grzyby","cebula","czosnek","jajko","musztarda","majeranek"]
kanapki = ["kanapki","pieczywo"]
omlet_slodki = ["omlet słodki","jajko","mąka","jogurt naturalny"]
caprese = ["caprese","pomidor","oliwa","ocet balsamiczny"]
twarozek = ["twarożek","twaróg","rzodkiewka","szczypiorek","śmietana 18%"]
gofry = ["gofry","mleko","olej","jajko","mąka","proszek do pieczenia"]
tosty_francuskie = ["tosty_francuskie","ser","pieczywo","jajko"]
chleb_wjajku = ["chleb w jajku","pieczywo","jajko"]
chleb_wjajku_zbulka = ["chleb w jajku z serem","bulka tarta","pieczywo","jajko","ser"]
nalesniki_zserem = ["naleśniki z serem","mleko","mąka","jajko","śmietana 18%","twaróg"]
nalesniki_znutella = ["naleśniki z nutellą","mleko","mąka","jajko","nutella"]

sniadania = [szakszuka,owsianka,platki,jajko_sadzone,jajko_namiekko,jajecznica,nalesniki_zserem,
             pasztet_zfasoli,kanapki,omlet_slodki,caprese,twarozek,gofry,tosty_francuskie,chleb_wjajku,
             chleb_wjajku_zbulka,nalesniki_znutella]


############# Zczytywanie listy śniadań i kolacji z pliku i generowanie
def wyswietl_sniadania():
    sniadania = open("lista sniadan i kolacji.txt", "r")
    sniadania_tekst = sniadania.readlines()
    for i in range(len(sniadania_tekst)):
        yield sniadania_tekst[i]

############# Lista składników danych śniadań
def jakie_skladniki_sniadanie(jakie_skladniki):
    if jakie_skladniki == 1: #szakszuka
        tekst ="Główne składniki na szakszuke to: \n -jajka \n -pomidory \n -masło klarowane lub oliwa \n -cebula" \
               " \n -2 ząbki czosnku \n\nDodatkowe ewentualne składniki: \n -słodka papryka \n -pieprz cayenne " \
               "\n -gałka muszkatałowa \n -kumin \n -swieża kolendra \n -szczypior"

    if jakie_skladniki == 2:  #owsianka
        tekst ="Główne składniki na owsianke to: \n -płatki owsiane \n -jogurt naturalny \n\n" \
               "Dodatkowe ewentualne składniki: \n -owoce \n -rodzynki \n -miód"

    if jakie_skladniki == 3: # platki na mleku
        tekst ="Główne składniki w płatkach na mleku to: \n -płatki \n -mleko"

    if jakie_skladniki == 4: #jajko sadzone
        tekst = "Główne składniki na jajko sadzone to: \n -jajko \n -maslo klarowane lub olej \n -sól i pieprz\n\n" \
                "Dodatkowe ewentualne składniki: \n -ziemniaki \n -maślanka \n -grzanki \n -sałata w śmietanie"

    if jakie_skladniki == 5: #jajko na miekko
        tekst = "Główne składniki na jajko na miękko to: \n -jajko\n\nDodatkowe ewentualne składniki: \n -grzanki"

    if jakie_skladniki == 6: #jajecznica
        tekst = "Główne składniki na jajecznice to: \n -jajka \n -maslo klarowane \n -sól i pieprz\n\n" \
                "Dodatkowe ewentualne składniki: \n -szczypiorek \n -cebula \n -papryczki ostre"

    if jakie_skladniki == 7: #nalesniki z dzemem
        tekst = "Główne składniki na naleśniki z dżemem to: \n -mleko \n -mąka \n -jajka \n -sól \n " \
                "-olej lub masło klarowane \n -dżem\n\n"

    if jakie_skladniki == 8: #pasztet z fasoli
        tekst = "Główne składniki na pasztet z fasoli to: \n -biała fasola 400g \n -seler 100g \n -suszone grzyby \n " \
                "-2 średnie cebule \n -2 ząbki czosnku \n -3 jajka \n -jabłko \n -musztarda \n -majeranek \n -olej \n " \
                "-sól i pieprz\n\nDodatkowe ewentualne składniki: \n -dowolne przyprawy"

    if jakie_skladniki == 9: #kanapki
        tekst = "Główne składniki na kanapki to: \n -pieczywo \n -masło\n\n" \
                "Dodatkowe ewentualne składniki: \n -dowolne warzywa, sery, jajka"

    if jakie_skladniki == 10: #omlet na słodko
        tekst = "Główne składniki na omlet na słodko to: \n -jajka \n -mąka \n -cukier \n jogurt naturalny\n\n" \
                "Dodatkowe ewentualne składniki: \n -owoce na słodko \n -warzywa"

    if jakie_skladniki == 11: #caprese
        tekst = "Główne składniki na caprese to: \n -pomidory \n -oliwa \n -ocet balsamiczny \n -mozarella \n -sól i pieprz\n\n" \
                "Dodatkowe ewentualne składniki: \n -ulubione przyprawy"

    if jakie_skladniki == 12: #twarozek z rzodkiewka i szczypiorkiem
        tekst = "Główne składniki na twarozek to: \n -twaróg \n -rzodiewka \n -szczypiorek \n -sól i pieprz \n -śmietana 18%\n\n" \
                "Dodatkowe ewentualne składniki: \n"

    if jakie_skladniki == 13: #gofry
        tekst = "Główne składniki na gofry to: \n -mleko \n -olej \n -jajka \n -mąka \n -proszek do pieczenia \n -cukier \n -sól\n\n" \
                "Dodatkowe ewentualne składniki: \n -owoce \n -cukier puder \n -bita śmietana"

    if jakie_skladniki == 14: #tosty francuskie
        tekst = "Główne składniki na tosty francuskie to: \n -papryka \n -ser \n -szczypiorek \n -cebula \n -pomidor \n -jajko\n\n" \
                "Dodatkowe ewentualne składniki: \n -oliwki lub inne dowolne dodatki"
    if jakie_skladniki == 15: #chleb w jajku
        tekst = "Główne składniki na chleb w jajku to: \n -chleb \n -jajko \n -masło klarowane \n - sól i pieprz\n\n" \
                "Dodatkowe ewentualne składniki: \n "
    if jakie_skladniki == 16: #chleb w jajku z bulka tarta i serem
        tekst = "Główne składniki na chleb w jajku z serem to: \n -chleb \n -jajko \n -masło klarowane \n " \
                "-sól i pieprz \n -ser liliput \n -bułka tarta\n\nDodatkowe ewentualne składniki: \n -keczup \n -majonez \n -sosy ostre"
    if jakie_skladniki == 17: #nalesniki z serem
        tekst = "Główne składniki na naleśniki z dżemem to: \n -mleko \n -mąka \n -jajka \n -sól \n " \
                "-olej lub masło klarowane \n -śmietana 18%\n -twaróg\n\n"
    if jakie_skladniki == 18: #nalesniki z nutellą
        tekst = "Główne składniki na naleśniki z dżemem to: \n -mleko \n -mąka \n -jajka \n -sól \n " \
                "-olej lub masło klarowane \n -nutella\n\n"
    return tekst

####################   POCZATEK PROGRAMU      ##################

################## Wybór - śniadania, czy kolacje?
print("Czesc, witaj w kulinarnym programie! Wybierz opcję, która Cię interesuje:\n")
print("1 - Interesują mnie śniadania\n\n2- interesują mnie obiady\n\n")
wybor1 = int(input("Wprowadź odpowiednią cyfrę i zatwierdź enterem.\n\n"))
clear()

################## Wybór - lista śniadań, czy składników?
if wybor1 == 1:
    print("Okej, zatem co dalej?\n")
    print("1 - Chce wyświetlić listę wszystkich dań i wybrać na co mam ochotę.\n\n")
    print("2 - Chce wybrać z listy składniki, które mam w lodówce i dostać pomysł na danie.\n\n")
    wybor2 = int(input("Wprowadź odpowiednią cyfrę i zatwierdź enterem.\n\n"))
    clear()

################## Wyświetla listę śniadań
    if wybor2 == 1:
        n = 1
        for i in wyswietl_sniadania():
            print(n, " - ", i)
            n += 1

################## Wybór śniadania, żeby wyświetlić składniki
        print("\n Wpisz liczbę danej potrawy i zatwierdź ją enterem, żeby zobaczyć składniki:")
        jakie_skladniki = int(input())
        clear()
        print(jakie_skladniki_sniadanie(jakie_skladniki),"\n\n")
        koniec = input("                                       Nacisnij enter, aby zakończyć program.")

################### Jeśli chce podać składniki, które ma w lodówce
    if wybor2 == 2:
        print("1 - Chce wybrac z listy większość składników, które mam w lodówce.\n\n")
        print("2 - Chce wybrać z listy tylko kilka składników, na które mam ochotę i dostać propozycję dania.\n\n")
        wybor3 = int(input())
        clear()

################### Wyświetlanie listy składników:
        if wybor3 == 1:
            for i in range (len(skladniki_sniadanie)):
                print(i, " - ",skladniki_sniadanie[i])
            print("\n")

################### Wczytywanie skladnikow, ktore ma uzytkownik
            moje_skladniki = list(map(int, input("Wprowadź liczby po spacji:").split()))
            clear()

################### Dobieranie dostepnych sniadan
            for i in range (len(sniadania)):
                n = 1
                for j in range(len(moje_skladniki)):
                    if skladniki_sniadanie[moje_skladniki[j]] in sniadania[i]:
                        n += 1
                if n == len(sniadania[i]):
                    dostepne_sniadania.append(sniadania[i][0])
            clear()

################### Wyswietlanie dostepnych sniadan
            print("Dostępne śniadania to:\n\n")
            for i in range (len(dostepne_sniadania)):
                print(i+1," - ",dostepne_sniadania[i])
            koniec = input()

################### Wyswietlanie listy sniadan
        if wybor3 == 2:
            for i in range (len(skladniki_sniadanie)):
                print(i, " - ",skladniki_sniadanie[i])
            print("\n")

################### Wczytywanie skladnikow, ktore ma uzytkownik
            moje_skladniki = list(map(int, input("Wprowadź liczby po spacji:").split()))
            clear()

################### Dobieranie dostepnych sniadan
            for i in range(len(sniadania)):
                for j in range(len(moje_skladniki)):
                    if skladniki_sniadanie[moje_skladniki[j]] in sniadania[i]:
                        dostepne_sniadania.append(sniadania[i][0])
                        break
                        clear()

################### Wyswietlanie dostepnych sniadan
            print("Dostępne śniadania to:\n\n")
            for i in range(len(dostepne_sniadania)):
                print(i + 1, " - ", dostepne_sniadania[i])
            koniec = input("                                       Nacisnij enter, aby zakończyć program.")