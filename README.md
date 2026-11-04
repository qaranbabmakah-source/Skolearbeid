Mandag – bygg organisasjonen i Active Directory

Stage 1

Mål
Jeg skal sjekke at DC01, DNS og Active Directory fungerer. Jeg skal ikke installere noe på nytt.
Dette sjekket jeg på DC01
ipconfig
Jeg sjekket IP-adressen og nettverket.
nslookup dc01.ad.lab.test
Jeg sjekket om DNS finner DC01.
nslookup -type=SRV _ldap._tcp.dc._msdcs.ad.lab.test
Jeg sjekket om DNS finner domenekontrolleren.
 dcdiag
Jeg sjekket om Active Directory har feil.
Resultat
Vi har tidligere jobbet med et domene som heter firma.local. Oppgaven bruker ad.lab.test. Kommandoene må bruke riktig domenenavn for vårt miljø.
I den tidligere gjennomgangen ble det meldt om et problem med DNS SRV-oppslaget. Andre kontroller så ut til å fungere, men resultatene bør bekreftes med utskrift eller skjermbilde fra DC01.
Konklusjon
Helsesjekken er gjennomført, men jeg kan ikke bekrefte at alt fungerer før DNS-feilen er undersøkt. Jeg dokumenterer feilen før jeg endrer noe.

Steg 2 – OU-struktur
Active Directory | DC01
Mål
Målet var å lage en enkel og ryddig OU-struktur i Active Directory. OU-er gjør det lettere å organisere brukere, datamaskiner og grupper.
Plan
Jeg planla denne strukturen før jeg bygde den:
Bedrift
   Brukere
       Administrasjon
       Support
   Datamaskiner
   Grupper
Gjennomføring
Jeg åpnet Active Directory Users and Computers på DC01. Jeg laget OU-en Bedrift. Under Bedrift laget jeg Brukere, Datamaskiner og Grupper. Under Brukere laget jeg Administrasjon og Support.
Hvorfor disse OU-ene?
Bedrift: Samler organisasjonen på ett sted.
Brukere: Samler brukerkontoer.
Administrasjon: For brukere i administrasjonen.
Support: For brukere som jobber med IT-support.
Datamaskiner: Samler datamaskiner.
 Grupper: Samler grupper som brukes til tilgang.
Resultat og konklusjon
Jeg har laget en enkel OU-struktur. Den gjør domenet mer oversiktlig og lettere å administrere. Senere kan vi bruke OU-ene med Group Policy.
Dokumentasjon: Legg inn et skjermbilde fra Active Directory Users and Computers som viser OU-strukturen.

Steg 3 – opprett brukere med en navnestandard

Jeg opprettet seks brukere i Active Directory på DC01.

Administrasjon:

Ola Nordmann
Kari Hansen
Per Olsen
Support:

Ali Hassan
Sara Ahmed
Mohamed Ali
Jeg brukte navnestandarden fornavn.etternavn.

Brukernavnet ola.nordmann var allerede i bruk, så jeg brukte ola.nordmann2.

Jeg kontrollerte Ola Nordmann med PowerShell:

Get-ADUser ola.nordmann2 -Properties DistinguishedName

Resultat:

PowerShell viste at brukeren ligger i riktig OU:

OU=Administrasjon,OU=Brukere,OU=Bedrift,DC=firma,DC=local

Konklusjon:

Jeg har opprettet seks brukere og kontrollert plasseringen til en bruker med PowerShell.




Steg 4 – skill tydelig mellom OU og gruppe
OU (Organisasjonsenhet): Brukes til å organisere og administrere brukere og datamaskiner i Active Directory. Brukere får ikke automatisk tilgangsrettigheter ved å være plassert i en OU.

Gruppe: Brukes til å samle brukere og administrere medlemskap og tilgangsrettigheter.

Utført arbeid

Jeg opprettet to globale sikkerhetsgrupper i Active Directory under firma.local → Bedrift → Grupper.

1. GG-Administrasjon

Ola Nordmann
Kari Hansen
Per Olsen
2. GG-Support

Sara Ahmed
Ali Hassan
Mohamed Ali
Begge gruppene ble opprettet med gruppeomfang Global og gruppetype Sikkerhet.

Kontroll

Jeg åpnet gruppenes egenskaper og kontrollerte fanen Medlemmer for å bekrefte at brukerne var lagt til i riktig gruppe.

Konklusjon

Jeg har lært forskjellen mellom OU og sikkerhetsgrupper, og hvordan brukere legges til i globale sikkerhetsgrupper i Active Directory.

Steg 5 – løft gruppestrukturen ett nivå
Jeg opprettet to domenelokale sikkerhetsgrupper i Active Directory på DC01:

DL-Felles-Administrasjon-RW

DL-Felles-Support-RW

Jeg la GG-Administrasjon inn i DL-Felles-Administrasjon-RW.

Jeg la GG-Suppert inn i DL-Felles-Support-RW.

Jeg kontrollerte at gruppene var lagt til riktig under Medlemmer.

Resultat:

Begge gruppene fungerer som planlagt. Jeg har lært hvordan AGDLP brukes til å organisere grupper og gjøre tilgangsstyring enklere.

Steg 6 – test med PowerShell
Jeg brukte PowerShell til å kontrollere brukere og grupper i Active Directory. Jeg testet kommandoene Get-ADUser, Get-ADGroup og Get-ADGroupMember.

Jeg bekreftet at GG-Support er medlem av DL.Felles-Support-RW. Resultatene stemmer med Active Directory Users and Computers (GUI).

Mandagens grunnoppgave

Jeg har opprettet en ryddig OU-struktur i Active Directory med brukere og grupper.

Jeg har opprettet globale grupper som GG-Support og GG-Administrasjon, og domenelokale grupper for tilgang til fellesressurser.

Jeg har lagt GG-Support inn i DL.Felles-Support-RW og kontrollert gruppemedlemskapet med PowerShell.

Forskjellen mellom OU og gruppe:

En OU brukes til å organisere brukere, datamaskiner og andre objekter i Active Directory. En gruppe brukes til å samle brukere og gi dem tilgang til ressurser.

Hvorfor gir vi rettigheter gjennom grupper?

Det gjør administrasjonen enklere og sikrere. Når en ny bruker trenger tilgang, kan vi legge brukeren til i riktig gruppe i stedet for å gi rettigheter direkte til hver enkelt bruker.


Videre utforskning – mandag

Designutfordring: Ny HR-avdeling

Bedriften skal få en ny HR-avdeling.

Jeg vil opprette en OU som heter HR under Bedrift i Active Directory.

Jeg vil også opprette to sikkerhetsgrupper:

GG-HR – en global gruppe for ansatte i HR.
DL-Felles-HR-RW – en domenelokal gruppe som gir tilgang til HR-mappen.
Jeg vil legge GG-HR inn i DL-Felles-HR-RW.

Dette gjør det enklere å administrere brukere og rettigheter. Bare ansatte som trenger tilgang til HR-mappen, skal få tilgang






