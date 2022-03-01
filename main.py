from random import randint
import os
clear = lambda: os.system("cls")
Afryka_Kraje = ["ALGIERA", "ANGOLA", "BENIN", "BOTSWANA", "BURKINA FASO", "BURUNDI", "CZAD",
                "DEMOKRATYCZNA REPUBLIKA KONGA", "DŻIBUTI",
                "ERYTREA", "ESWATINI", "ETIOPIA", "GABON", "GAMBIA", "GHANA", "GWINEA", "KAMERUN", "KENIA", "KOMORY",
                "KONGO", "LESOTHO",
                "LIBERIA", "LIBIA", "MADAGASKAR", "MALAWI", "MALI", "MAROKO", "MAURETANIA", "MAURITIUS", "MOZAMBIK",
                "NAMIBIA", "NIGER",
                "NIGERIA", "POŁUDNIOWA AFRYKA", "REPUBLIKA ŚRODKOWOAFRYKAŃSKA", "REPUBLIKA ZIELONEGO PRZYLĄDKA",
                "RWANDA", "SENEGAL",
                "SESZELE", "SIERRA LEONE", "SOMALIA", "SUDAN", "TANZANIA", "TOGO", "TUNEZJA", "UGANDA",
                "WYBRZEŻE KOŚCI SŁONIOWEJ",
                "ZAMBIA", "ZIMBABWE", "EGIPT"]
Afryka_Stolice = ["ALGIER", "LUANDA", "PORTO NOVO", "GABORONE", "WAGADUGU", "GITEGA", "NDŻAMENA", "KINSZASA", "DŻIBUTI",
                  "ASMARA",
                  "MBABANE", "ADDIS ABEBA", "LIBREVILLE", "BANDŻUL", "AKRA", "KONAKRY", "JUANDE", "NAIROBI", "MORONI",
                  "BRAZZAVILLE",
                  "MASERU", "MONROVIA", "TRYPOLIS", "ANTANANARYWA", "LILONGWE", "BAMAKO", "RABAT", "NAWAKSZUT",
                  "PORT LOUIS",
                  "MAPUTO", "WINDHUK", "NIAMEY", "ABUDŻA", "PRETORIA", "BANGI", "PRAIA", "KIGALI", "DAKAR", "VICTORIA",
                  "FREETOWN",
                  "MOGADISZU", "CHARTUM", "DODOMA", "LOME", "TUNIS", "KAMPALA", "JAMUSUKRO", "LUSAKA", "HARARE", "KAIR"]

Ameryka_Poludniowa_Kraje = ["ARGENTYNA","BOLIWIA","BRAZYLIA","CHILE","EKWADOR","GUJANA","KOLUMBIA","PARAGWAJ","PERU",
                            "SURINAM","TRYNIDAD I TOBAGO","URUGWAJ","WENEZUELA"]

Ameryka_Poludniowa_Stolice = ["BUENOS AIRES","SUCRE","BRASILIA","SANTIAGO","QUITO","GEORGETOWN","BOGOTA","ASUNCION",
                              "LIMA","PARAMARIBO","PORT OF SPAIN","MONTEVIDEO","CARACAS"]

Ameryka_Polnocna_Kraje = ["ANTIGUA I BARBUDA","BAHAMY","BARBADOS","BELIZE","DOMINIKA","DOMINIKANA","GRENADA","GWATEMALA",
                          "HAITI","HONDURAS","JAMAJKA","KANADA","KOSTARYKA","KUBA","MEKSYK","NIKARAGUA","PANAMA",
                          "SAINT KITTS I NEVIS","SAINT LUCIA","SAINT VINCENT I GRENADYNY","SALWADOR","STANY ZJEDNOCZONE"]

Ameryka_Polnocna_Stolice = ["SAINT JOHNS","NASSAU","BRIDGETOWN","BELMOPAN","ROSEAU","SANTO DOMINGO","SAINT GEORGES",
                            "GWATEMALA","PORT AU PRINCE","TEGUCIGALPA","KINGSTON","OTTAWA","SAN JOSE","HAWANA","MEKSYK",
                            "MANAGUA","PANAMA","BASSETERRE","CASTRIES","KINGSTOWN","SAN SALWADOR","WASZYNGTGON"]

Australia_I_Oceania_Kraje = ["AUSTRALIA","FIDŻI","KIRIBATI","MIKRONEZJA","NAURU","NOWA ZELANDIA","PALAU","PAPUA NOWA GWINEA",
                             "SAMOA","TONGA","TUVALU","VANUATU","WYSPY MARSHALLA","WYSPY SALOMONA"]

Australia_I_Oceania_Stolice = ["CAMBERRA","SUVA","BAIRIKI","PALIKIR","YAREN","WELLINGTON","NGERULMUD","PORT MORESBY",
                               "APIA","NUKU ALOFA","VAIAKU","PORT VILA","MAJURO","HONIARA"]

Azja_Kraje = ["AFGANISTAN","ARABIA SAUDYJSKA","ARMENIA","AZERBEJDŻAN","BAHRAJN","BANGLADESZ","BHUTAN","BRUNEI","CHINY",
              "CYPR","FILIPINY","INDIE","INDONEZJA","IRAK","IRAN","IZRAEL","JAPONIA","JEMEN","JORDANIA","KAMBODŻA","KATAR",
              "KIRGISTAN","KOREA POŁUDNIOWA","KOREA PÓŁNOCNA","KUWEJT","LAOS","LIBAN","MALEDIWY","MALEZJA","MJANMA",
              "MONGOLIA","NEPAL","OMAN","PAKISTAN","SINGAPUR","SRILANKA","SYRIA","TADŻYKISTAN","TAJLANDIA","TIMOR WSCHODNI",
              "TURKMENISTAN","UZBEKISTAN","WIETNAM","ZJEDNOCZONE EMIRATY ARABSKIE","KAZACHSTAN","ROSJA","TURCJA"]

Azja_Stolice = ["KABUL","RIJAD","ERYWAN","BAKU","MANAMA","DHAKA","THIMPHU","BANDAR SERI BEGAWAN","PEKIN","NIKOZJA","MANILA",
                "NOWE DELHI","DŻAKARTA","BAGDAD","TEHERAN","JEROZOLIMA","TOKIO","SANA","AMMAN","PHNOM PENH","DOHA","BISZKEK",
                "SEUL","PGJONGJANG","KUWEJT","WIENTIAN","BEJRUT","MALE","KUALA LUMPUR","NAYPYIDAW","UŁAN BATOR","KATMANDU",
                "MASKAT","ISLAMABAD","SINGAPUR","SRI DZAJAWARDANAPURA KOTTE","DAMASZEK","DUSZANBE","BANGKOK","DILI","ASZCHABAD",
                "TASZKENT","HANOI","ABU ZABI","NUR SUŁTAN","MOSKWA","ANKARA"]

Europa_Kraje = ["KAZACHSTAN","ROSJA","TURCJA","ALBANIA","ANDORA","AUSTRIA","BELGIA","BIAŁORUŚ","BOŚNIA I HERCEGOWINA",
                "BUŁGARIA","CHORWACJA","CZARNOGÓRA","CZECHY","DANIA","ESTONIA","FINLANDIA","FRANCJA","GRECJA","HISZPANIA",
                "HOLANDIA","IRLANDIA","ISLANDIA","LIECHTENSTEIN","LITWA","LUKSEMBURG","ŁOTWA","MACEDONIA PÓŁNOCNA","MALTA",
                "MOŁDAWIA","MONAKO","NIEMCY","NORWEGIA","POLSKA","PORTUGALIA","RUMUNIA","SAN MARINO","SERBIA","SŁOWACJA",
                "SŁOWENIA","SZWAJCARIA","SZWECJA","UKRAINA","WATYKAN","WĘGRY","WIELKA BRYTANIA","WŁOCHY","GRUZJA"]

Europa_Stolice = ["NUR SUŁTAN","MOSKWA","ANKARA","TIRANA","ANDORA","WIEDEŃ","BRUKSELA","MIŃSK","SARAJEWO","SOFIA","ZAGRZEB",
                  "PODGORICA","PRAGA","KOPENHAGA","TALLINN","HELSINKI","PARYŻ","ATENY","MADRYT","AMSTERDAM","DUBLIN","REYKJAVIK",
                  "VADUZ","WILNO","LUKSEMBURG","RYGA","SKOPJE","VALETTA","KISZYNIÓW","MONAKO","BERLIN","OSLO","WARSZAWA",
                  "LIZBONA","BUKARESZT","SAN MARINO","BELGRAD","BRATYSŁAWA","LUBLANA","BERNO","SZTOKHOLM","KIJÓW","WATYKAN",
                  "BUDAPESZT","LONDYN","RZYM","TBILISI",]


print("Wybierz kontynent:\n")

print("1. Afryka")
print("2. Ameryka Południowa")
print("3. Ameryka Północna")
print("4. Australia i Oceania")
print("5. Azja")
print("6. Europa")

wybor1 = int(input())

clear()

print("Którą opcję wybierasz?\n")
print("1. Bez podpowiedzi")
print("2. Z podpowiedziami")

wybor2 = int(input())

def gra(kraj,stolica):
    j = len(kraj) - 1
    while j != 0:
        clear()
        litery = []
        index = randint(0, j)
        print(kraj[index], "                              Pozostało ", j, " krajów")
        dl_wyrazu = len(stolica[index])
        stolica2 = stolica[index]
        zgadywanka = []
        for i in range (dl_wyrazu):
            zgadywanka.append("_")
        while "_" in zgadywanka:
            clear()
            print("Wprowadź literę:")
            print(" ".join(zgadywanka))
            print("")
            print("Użyte litery: ",", ".join(litery))
            litera = str(input())
            litera = litera.upper()
            if not litera in litery:
                litery.append(litera)
            if len(litera) == 1:
                for j in range (dl_wyrazu):
                    if litera == stolica2[j]:
                        zgadywanka[j] = litera
        odpowiedz = input()
        faktyczna_odpowiedz = stolica[index]
        if len(odpowiedz) == len(faktyczna_odpowiedz):
            punkt = 0
            odpowiedz = odpowiedz.upper()
            for i in range(len(odpowiedz)):
                if odpowiedz[i] == faktyczna_odpowiedz[i]:
                    punkt += 1
            if punkt >= (len(odpowiedz) - 2):
                kraj.pop(index)
                stolica.pop(index)
                j -= 1
    clear()
    print("Gratulacje! Quiz zakończony powodzeniem.")

def sprawdzanie(kraj,stolica):
    j = len(kraj) - 1
    while j != 0:
        clear()
        index = randint(0, j)
        print(kraj[index], "                              Pozostało ", j, " krajów")
        odpowiedz = input()
        faktyczna_odpowiedz = stolica[index]
        if len(odpowiedz) == len(faktyczna_odpowiedz):
            punkt = 0
            odpowiedz = odpowiedz.upper()
            for i in range(len(odpowiedz)):
                if odpowiedz[i] == faktyczna_odpowiedz[i]:
                    punkt += 1
            if punkt >= (len(odpowiedz) - 2):
                kraj.pop(index)
                stolica.pop(index)
                j -= 1
    clear()
    print("Gratulacje! Quiz zakończony powodzeniem.")


if wybor1 == 1:
    if wybor2 == 1:
        sprawdzanie(Afryka_Kraje,Afryka_Stolice)
    if wybor2 == 2:
        gra(Afryka_Kraje,Afryka_Stolice)

if wybor1 == 2:
    if wybor2 == 1:
        sprawdzanie(Ameryka_Poludniowa_Kraje,Ameryka_Poludniowa_Stolice)
    if wybor2 == 2:
        gra(Ameryka_Poludniowa_Kraje,Ameryka_Poludniowa_Stolice)

if wybor1 == 3:
    if wybor2 == 1:
        sprawdzanie(Ameryka_Polnocna_Kraje,Ameryka_Polnocna_Stolice)
    if wybor2 == 2:
        gra(Ameryka_Polnocna_Kraje,Ameryka_Polnocna_Stolice)

if wybor1 == 4:
    if wybor2 == 1:
        sprawdzanie(Australia_I_Oceania_Kraje,Australia_I_Oceania_Stolice)
    if wybor2 == 2:
        gra(Australia_I_Oceania_Kraje,Australia_I_Oceania_Stolice)

if wybor1 == 5:
    if wybor2 == 1:
        sprawdzanie(Azja_Kraje,Azja_Stolice)
    if wybor2 == 2:
        gra(Azja_Kraje,Azja_Stolice)

if wybor1 == 6:
    if wybor2 == 1:
        sprawdzanie(Europa_Kraje,Europa_Stolice)
    if wybor2 == 2:
        gra(Europa_Kraje,Europa_Stolice)
