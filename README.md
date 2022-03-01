# Dokomentácia k študentskému projektu

### Realizácia
Moja realizácia je dostupná na [GitHub](https://github.com/Chalupa99/SIP-Proxy "Moja práca")

### Knižnice
Použité knižnice:
- verejne dostupná knižnica sipfullproxy, ktorá je dostupná na [GitHub](https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py "SIP Proxy") 
- logging
- time
- socketserver
- socket


### Programovací jazyk
Celé riešienie je v jazyku **Python 3.8.**

### Funkcionality
Implementoval som:
- Registráciu účastníka bez autentifikácie
- Vytočenie hovoru a zvonenie na druhej strane
- Prijatie hovoru druhou stranou a fungujúci hlasový hovor
- Ukončenie hlasového hovoru (prijatého aj neprijatého)
- Úpravu SIP stavových kódov v zdrojovom kóde proxy, konkrétne

### Návod na spustenie
Program sa spúšťa cez súbor `main.py`, v ktorom sa po spustení nastaví SIP ústredňa.

### Navigácia / User guide
Počas celého bežania SIP ústredne sa zhotovuje záznam aktivít v momentálnej relácia v súbore `proxy.log`.

