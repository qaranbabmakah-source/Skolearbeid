Jobbklar – Hva jeg har lært om AD DS og LDAP

Denne uken har jeg jobbet praktisk med Active Directory Domain Services (AD DS), LDAP, DNS og Group Policy i Windows Server.

Jeg har lært hvordan jeg kan administrere brukere, grupper og OU-er i et Windows-domene.

Dette har jeg gjort i laben

Jeg har jobbet med domenet firma.local og domenekontrolleren DC01.
Jeg har testet domenepålogging på CLIENT01 med brukeren sara.ahmed.
Jeg har kontrollert gruppemedlemskap med kommandoen whoami /groups.
Jeg har testet tilgang til den delte Support-mappen gjennom sikkerhetsgrupper.
Jeg har opprettet og koblet en GPO til Support-OU-en.
Jeg har brukt gpupdate /force og gpresult /r for å kontrollere at GPO-en ble brukt.
Jeg har feilsøkt DNS og nettverk med ipconfig /all, nslookup og ping.
Jeg har brukt dcdiag /test:dns for å undersøke DNS-feil på domenekontrolleren.
Hva jeg har lært

Jeg har lært forskjellen mellom OU, grupper og GPO.

Jeg forstår bedre hvordan DNS hjelper klienter med å finne domenekontrolleren, hvordan AD DS administrerer brukere og grupper, og hvordan GPO brukes til sentral styring.

Jeg har også lært at LDAP brukes til å søke etter informasjon i Active Directory.

Feilsøking

Jeg har lært å feilsøke systematisk. Jeg kontrollerer først nettverk og IP-adresse, deretter DNS, kontakt med domenekontrolleren, gruppemedlemskap og GPO.

Under arbeidet oppdaget jeg problemer med DNS og kommunikasjonen mellom CLIENT01 og DC01. Jeg brukte kommandoer for å undersøke hvor feilen kunne ligge.

Oppsummering

Denne uken har jeg fått mer praktisk erfaring med administrasjon av Windows-domener.

Jeg kan nå utføre flere grunnleggende oppgaver innen Active Directory, teste brukertilgang, kontrollere gruppepolicyer og undersøke vanlige nettverks- og DNS-problemer.

Dette er nyttige ferdigheter som jeg kan bruke i framtidig arbeid innen IT-drift og brukerstøtte.
du kan 2 av bilde
<img width="1012" height="624" alt="image" src="https://github.com/user-attachments/assets/5433c5eb-1b45-4cf6-94b3-2f96bd70da00" />
<img width="960" height="564" alt="image" src="https://github.com/user-attachments/assets/8f1ab072-a04d-4a39-98db-3c019f8d3b46" />


Ogso Se lenger ned i andre dokumentet for en detaljert oversikt over arbeidet jeg har gjort hver dag fra mandag til fredag. Der har jeg dokumentert oppgavene, testene, resultatene og feilsøkingen gjennom hele uken.



UKEPLAN-AD DS OG LDAP


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

Dette gjør det enklere å administrere brukere og rettigheter. Bare ansatte som trenger tilgang til HR-mappen, skal få tilgang.


Tirsdag – klient, domenepålogging og tilgang
Steg 1 – DNS før domenemedlemskap


Steg 1 – DNS før domenemedlemskap

Utført arbeid:

Kontrollerte nettverksinnstillingene på CLIENT01 med ipconfig /all.
Bekreftet at CLIENT01 har IP-adressen 192.168.1.108 og DNS-server 192.168.1.10 (DC01).
Kontrollerte DNS-tjenesten på DC01 med Get-Service DNS. Status var Running.
Testet DNS på DC01 med nslookup google.com 192.168.1.10. Testen fungerte.
Feil og feilsøking:

CLIENT01 fikk feilmeldingen DNS request timed out ved DNS-oppslag mot DC01.
Ping fra DC01 til CLIENT01 fungerte ikke.
Opprettet en brannmurregel for ICMPv4 på CLIENT01, men problemet vedvarte.
Resultat:
DNS er riktig angitt på CLIENT01, men DNS-kommunikasjonen med DC01 fungerer fortsatt ikke. Oppslagene nslookup ad.lab.test og nslookup dc01.ad.lab.test er ikke dokumentert som testet.

Steg 2 – meld CLIENT01 inn i domenet

Mål

Målet med denne oppgaven er å endre klientens datamaskinnavn til CLIENT01, melde klienten inn i domenet ad.lab.test, og kontrollere domenepålogging.

Arbeid som er utført

Jeg åpnet Systemegenskaper på klientmaskinen.
Jeg gikk til fanen Datamaskinnavn og klikket på Endre.
Jeg endret datamaskinnavnet fra DESKTOP-CS3A0OK til CLIENT01.
Jeg valgte Domene og skrev inn ad.lab.test.
Jeg klikket på OK for å forsøke å melde klienten inn i domenet.
Problem som oppstod

Windows viste følgende feilmelding:

«Kan ikke kontakte Active Directory-domenekontrolleren (AD DC) for domenet ad.lab.test.»

Dette betyr at klienten ikke klarte å kontakte domenekontrolleren.

Feilsøking

Jeg åpnet PowerShell på klientmaskinen og kjørte kommandoen:

nslookup ad.lab.test 192.168.1.10

Resultatet viste:

DNS request timed out
Server: Unknown
Address: 192.168.1.10
Request timed-out
Testen viste at klienten ikke fikk svar fra DNS-serveren på 192.168.1.10.

Tidligere nettverkstester viste også at klienten kunne kontakte 192.168.1.104, men ikke 192.168.1.10.

Status

Steg 2 er påbegynt, men ikke fullført.

Datamaskinnavnet CLIENT01 er skrevet inn, men endringen er ikke bekreftet etter omstart.
Forsøket på å melde klienten inn i ad.lab.test mislyktes.
DNS- og nettverkstilkoblingen til domenekontrolleren må undersøkes.
Domenepålogging og kommandoene whoami og whoami /groups er ikke gjennomført.
Sammenligning med lokal pålogging (.\lokalbruker) gjenstår.

Steg 3 – flytt datamaskinobjektet


Hva jeg gjorde:

Åpnet Active Directory Users and Computers på DC01.
Opprettet datamaskinobjektet CLIENT01 i Bedrift\Datamaskiner.
Endret navnet på den virtuelle maskinen til client01.
Forsøkte å koble CLIENT01 til domenet firma.local.
Kontrollerte DNS, IP-adresse og nettverkskort i Hyper-V.
Problemer:

CLIENT01 klarte ikke å kontakte domenekontrolleren DC01.
nslookup firma.local ga «DNS request timed out».
ping 192.168.1.10 ga «Destination host unreachable».
Domenetilkoblingen mislyktes på grunn av nettverksproblemer.
Hvorfor bruke en egen OU?

En egen OU gjør det enklere å organisere datamaskiner, administrere sikkerhet og bruke Group Policy (GPO).

Steg 4 – gruppebasert tilgang

Steg 4 – Gruppebasert tilgang

Mål: Opprette delte mapper på DC01 og styre tilgangen gjennom sikkerhetsgrupper i Active Directory.

Arbeid utført

Opprettet mappene C:\Felles\Administrasjon og C:\Felles\Support på DC01.
Kontrollerte sikkerhetsgruppene i Active Directory.
Arbeidet med NTFS-tillatelser under Egenskaper → Sikkerhet.
Brukte ressursgrupper for å tildele tilgang i stedet for enkeltbrukere.
Problemer underveis

Vi fikk feilmeldingen «Finner ikke navn» da vi forsøkte å legge til gruppen DL-Felles-Support-RW. Vi kontrollerte gruppenavnene i Active Directory og brukte avansert søk for å finne riktige grupper.

Testing og resultat

Forventet tilgang fra CLIENT01:



Bruker

Mappe

Forventet resultat

Support

Support

Tilgang

Support

Administrasjon

Ingen tilgang

Administrasjon

Administrasjon

Tilgang

Konklusjon: Mappene ble opprettet, og vi arbeidet med gruppebaserte tillatelser. Testresultatene fra CLIENT01 er ikke dokumentert med skjermbilder.



Tirsdagens oppgave – Active Directory og filtilgang

1. Mål

Målet mitt var å koble CLIENT01 til domenet firma.local, teste domenebrukere og kontrollere gruppebasert tilgang til mapper.

2. Domenetilknytning – CLIENT01

Jeg endret datamaskinnavnet til CLIENT01 og forsøkte å melde maskinen inn i domenet firma.local.

Jeg fikk feilmeldingen om at domenekontrolleren ikke kunne kontaktes. Jeg undersøkte problemet med ipconfig, ping og nslookup.

CLIENT01 hadde IP-adressen 192.168.1.108 og DNS-serveren 192.168.1.10.

Jeg klarte ikke å fullføre domenetilknytningen på grunn av nettverks- og DNS-problemer.

3. Gruppebasert tilgang

Jeg opprettet to mapper på DC01:

C:\Felles\Support
C:\Felles\Administrasjon
Jeg kontrollerte sikkerhetsgruppene i Active Directory og arbeidet med å gi gruppene tilgang til riktige mapper.

Jeg fikk problemer med å finne gruppen DL-Felles-Support-RW. Jeg brukte avansert søk for å finne riktig gruppenavn.

4. Testing av domenebrukere

Jeg skulle teste minst to forskjellige domenebrukere og bruke kommandoen whoami /groups for å kontrollere gruppemedlemskap.

Jeg fikk ikke fullført testene fra CLIENT01 fordi domenetilknytningen ikke fungerte.

5. Rettighetsmatrise



Brukergruppe

Support

Administrasjon

GG-Support

Tillatt

Ingen tilgang

GG-Administrasjon

Ingen tilgang

Tillatt

Dette er tilgangene jeg forventet. Jeg fikk ikke bekreftet alle resultatene gjennom testing.

6. NTFS og delingsrettigheter

Jeg undersøkte forskjellen mellom NTFS-rettigheter og delingsrettigheter.

NTFS-rettigheter styrer tilgangen til filer og mapper, mens delingsrettigheter styrer tilgang via nettverket.

Jeg lærte at den mest begrensende effektive tillatelsen gjelder når begge brukes.

7. FILE01 – Videre utforskning

Jeg skulle opprette en Windows Server-VM kalt FILE01, melde den inn i domenet og flytte fildelingen dit.

Jeg har ikke dokumentert denne delen som fullført.

8. Konklusjon

Jeg fikk opprettet mapper og arbeidet med gruppebasert tilgang i Active Directory.

Jeg møtte problemer med DNS, domenetilknytning og søk etter sikkerhetsgrupper. Jeg forsøkte å løse problemene ved å kontrollere nettverksinnstillinger og gruppenavn.

Jeg lærte mer om Active Directory, gruppebaserte rettigheter og feilsøking i Windows Server.

Onsdag – LDAP og katalogsøk

Steg 1 – LDAP og Distinguished Name

Mål

Målet mitt var å forstå hvordan objekter i Active Directory er organisert, og hvordan jeg kan finne plasseringen deres ved hjelp av Distinguished Name (DN).

Hva jeg gjorde

Jeg åpnet Active Directory Users and Computers på DC01.

Jeg gikk til:

firma.local → Bedrift → Brukere → Support

Der fant jeg brukeren Sara Ahmed.

Jeg høyreklikket på brukeren og valgte Egenskaper. Deretter aktiverte jeg avanserte funksjoner og åpnet Redigeringsprogram for attributter.

Jeg fant attributtet distinguishedName og undersøkte verdien.

Resultat

Jeg fant følgende Distinguished Name:

CN=Sara Ahmed,OU=Support,OU=Brukere,OU=Bedrift,DC=firma,DC=local

Dette betyr:

CN=Sara Ahmed: Navnet på brukerobjektet.
OU=Support: Brukeren ligger i organisasjonsenheten Support.
OU=Brukere: Support ligger under Brukere.
OU=Bedrift: Brukere ligger under Bedrift.
DC=firma,DC=local: Domenet heter firma.local.
Hva jeg lærte

Jeg lærte at LDAP er en protokoll som brukes til å søke etter og lese informasjon i katalogtjenester som Active Directory.

Jeg lærte også at Distinguished Name (DN) viser den nøyaktige plasseringen til et objekt i katalogstrukturen.

Konklusjon

Jeg klarte å finne Distinguished Name for brukeren Sara Ahmed og forstå hvordan CN, OU og DC beskriver plasseringen til brukeren i Active Directory.


Steg 2 – hent DN med PowerShell

Jeg brukte PowerShell på DC01 for å finne Distinguished Name (DN) til en bruker og en datamaskin i Active Directory.

Først undersøkte jeg brukeren Sara Ahmed med kommandoen:

Get-ADUser -Filter "Name -eq 'Sara Ahmed'" -Properties DistinguishedName

Jeg fikk følgende resultat:

CN=Sara Ahmed,OU=Support,OU=Brukere,OU=Bedrift,DC=firma,DC=local

Deretter brukte jeg kommandoen:

Get-ADComputer CLIENT01 -Properties DistinguishedName

Resultatet var:

CN=Client01,OU=Datamaskiner,OU=Bedrift,DC=firma,DC=local

Jeg sammenlignet resultatene med plasseringen i Active Directory Users and Computers.

Jeg fant ut at Sara Ahmed ligger under Bedrift → Brukere → Support, mens Client01 ligger under Bedrift → Datamaskiner.

Konklusjon: Jeg lærte hvordan jeg kan bruke PowerShell til å finne Distinguished Name og kontrollere hvor objekter ligger i Active Directory.



Steg 3 – søk i en bestemt del av katalogen

Mål

Målet mitt var å lære hvordan jeg kan søke etter brukere i en bestemt del av Active Directory ved hjelp av PowerShell og LDAP.

Hva jeg gjorde

Jeg åpnet PowerShell på DC01 og forsøkte å søke etter brukerne i Support-OU-en.

Jeg brukte kommandoen:

Get-ADUser -Filter * -SearchBase "OU=Support,OU=Brukere,OU=Bedrift,DC=firma,DC=local"

Jeg brukte domenet firma.local fordi dette er domenet mitt.

Problemer jeg møtte

Da jeg kjørte kommandoen, fikk jeg feilmeldinger.

Først fikk jeg en feil fordi jeg hadde skrevet SearchBase uten bindestrek foran.

Jeg rettet kommandoen og prøvde igjen, men fikk feilmeldingen «Finner ikke mappeobjektet».

Jeg forsøkte også å bruke Get-ADOrganizationalUnit for å finne riktig Distinguished Name, men kommandoen ble skrevet feil og ble derfor ikke gjenkjent av PowerShell.

Jeg fikk ikke fullført søket etter alle brukerne i Support-OU-en.

LDAP-filter

Oppgaven ba meg også prøve et LDAP-filter med sAMAccountName.

Et eksempel tilpasset mitt domene er:

Get-ADUser -LDAPFilter "(sAMAccountName=brukernavn)"

Jeg har ikke testet dette filteret ennå.

Hva jeg lærte

Jeg lærte at -SearchBase brukes til å begrense et søk til en bestemt del av Active Directory.

Jeg lærte også at -LDAPFilter kan brukes til å søke etter objekter basert på attributter, for eksempel sAMAccountName.

Konklusjon

Jeg forsøkte å søke etter brukere i Support-OU-en med PowerShell. Selv om søket ikke ble fullført, fikk jeg erfaring med feilsøking og lærte at Active Directory kan søkes på forskjellige måter.


Steg 4 – koble LDAP tilbake til nettverksuka

Mål

Målet mitt var å undersøke forbindelsen mellom CLIENT01 og domenekontrolleren DC01 ved hjelp av TCP-port 389, som normalt brukes til LDAP.

Hva jeg gjorde

Jeg åpnet Windows PowerShell på CLIENT01 og testet forbindelsen til DC01 med kommandoen:

Test-NetConnection dc01.firma.local -Port 389

Jeg fikk feilmeldingen:

Name resolution of DC01.firma.local failed

Dette viste at CLIENT01 ikke klarte å finne IP-adressen til DC01 gjennom DNS.

Testing med IP-adresser

Jeg forsøkte deretter å koble til DC01 direkte med IP-adressen:

Test-NetConnection 192.168.1.10 -Port 389

Resultatet var:

TcpTestSucceeded : False

Jeg undersøkte nettverksinnstillingene på DC01 med kommandoen ipconfig og fant to IP-adresser:

Ethernet: 192.168.1.10
vEthernet (Hyper-V): 192.168.1.104
Deretter testet jeg den andre IP-adressen fra CLIENT01:

Test-NetConnection 192.168.1.104 -Port 389

Resultatet var:

TcpTestSucceeded : True

Dette viste at CLIENT01 kunne opprette en TCP-forbindelse til port 389 på DC01 via IP-adressen 192.168.1.104.

Sammenhengen mellom DNS, TCP og LDAP

Jeg lærte at disse nettverkstjenestene samarbeider:

DNS oversetter domenenavnet til en IP-adresse.
TCP oppretter en forbindelse til riktig IP-adresse og port.
LDAP brukes til å søke etter og hente informasjon fra Active Directory.
Port 389 brukes normalt til LDAP.

Konklusjon

Jeg klarte å teste forbindelsen mellom CLIENT01 og DC01.

Den første testen med domenenavnet mislyktes på grunn av DNS-navneoppslag. Testen mot 192.168.1.10 mislyktes også.

Da jeg brukte IP-adressen 192.168.1.104, fikk jeg TcpTestSucceeded: True.

Jeg lærte hvordan DNS, IP-adresser, TCP-porter og LDAP henger sammen. Testen bekreftet at TCP-port 389 var tilgjengelig via den andre IP-adressen, men jeg testet ikke et faktisk LDAP-søk fra CLIENT01.



Onsdagens oppgave – LDAP og katalogsøk

Grunnoppgave

Jeg fant brukeren Sara Ahmed og datamaskinen CLIENT01 både i Active Directory Users and Computers og med PowerShell.

Jeg brukte kommandoene:

Get-ADUser -Filter "Name -eq 'Sara Ahmed'" -Properties DistinguishedName

Get-ADComputer CLIENT01 -Properties DistinguishedName

Jeg fant DN til Sara Ahmed:

CN=Sara Ahmed,OU=Support,OU=Brukere,OU=Bedrift,DC=firma,DC=local

CN er objektnavnet, OU viser plasseringen, og DC viser domenet.

Jeg forsøkte å bruke -SearchBase for å søke i Support-OU, men fikk feilmeldinger. Jeg lærte også hvordan LDAP-filter brukes til katalogsøk.

Jeg testet LDAP-port 389 fra CLIENT01:

dc01.firma.local: DNS-oppslag mislyktes.
192.168.1.10: TCP-test mislyktes.
192.168.1.104: TCP-test lyktes.
Videre utforskning

Jeg undersøkte hvordan LDAP-filter kan søke etter brukere basert på attributter som department.

Jeg lærte at ldp.exe er et grafisk verktøy for å undersøke LDAP-katalogen.

Jeg undersøkte også LDAPS. Port 636 brukes normalt til LDAP over TLS, som beskytter kommunikasjonen med kryptering.

Konklusjon

Jeg lærte å finne objekter i Active Directory, forstå Distinguished Name og undersøke LDAP og nettverksforbindelser.


Torsdag - Group Policy og AD-feilsøkingTorsdag - Group Policy og AD-feilsøking

Steg 1 - forstå hva en GPO faktisk gjør

1. Mål

Målet mitt var å koble CLIENT01 til domenet firma.local, teste flere domenebrukere, kontrollere gruppemedlemskap og arbeide med gruppebasert tilgang og Group Policy.

2. Oppsett og struktur

Jeg brukte DC01 som domenekontroller og CLIENT01 som Windows-klient i Hyper-V.

Jeg arbeidet med OU-strukturen Bedrift, Brukere, Support, Administrasjon og Grupper i Active Directory. Jeg brukte mappene C:\felles\Support og C:\felles\Administrasjon og sikkerhetsgrupper for tilgangsstyring.

3. Test av domenebrukere

Jeg meldte CLIENT01 inn i domenet firma.local og testet pålogging med Sara Ahmed, Mohamed Ali og Ali Hassan. Jeg fikk opplyst og kontrollert at testene var gjennomført.

4. Kontroll med kommandolinje

Jeg kjørte whoami på CLIENT01. Da jeg var logget inn som Sara Ahmed, fikk jeg resultatet firma\sara.ahmed.

Jeg kjørte også whoami /groups og fant blant annet FIRMA\GG-Support og FIRMA\DL-Felles-Support-RW. Slik kontrollerte jeg hvilke grupper brukeren tilhørte.

5. Group Policy (GPO)

Jeg opprettet GPO-Support-Brukerinnstilling og koblet den til Support-OU-en. Under User Configuration > Policies > Administrative Templates > Desktop aktiverte jeg innstillingen som fjerner Papirkurv-ikonet fra skrivebordet.

Jeg kjørte gpupdate /force på CLIENT01 og fikk melding om at både bruker- og datamaskinpolicy ble oppdatert.

6. Mapper og tilgangsstyring

Jeg arbeidet med gruppebaserte rettigheter for Support- og Administrasjon-mappene. Jeg bekreftet at Sara Ahmed kunne åpne Support-mappen fra CLIENT01.

Jeg testet brukerkontoene og mappetilgangene i laben. Jeg lærte at både delingsrettigheter og NTFS-rettigheter påvirker den effektive tilgangen.



Steg 2 - lag en trygg brukerpolicy
Mål

Målet mitt var å opprette en enkel og trygg brukerpolicy i Group Policy Management, knytte den til riktig organisasjonsenhet (OU) og teste at policyen ble brukt på en domenebruker på CLIENT01.

Gjennomføring

• Jeg åpnet Group Policy Management på domenekontrolleren DC01 i domenet firma.local.
• Jeg opprettet GPO-en GPO-Support-Brukerinnstilling og koblet den til Support-OU-en under Bedrift > Brukere > Support.
• Jeg valgte en enkel brukerinnstilling i Group Policy Editor. Jeg testet en innstilling knyttet til skrivebordet, blant annet å fjerne papirkurvikonet fra skrivebordet.
• Jeg logget på CLIENT01 med domenebrukeren sara.ahmed, som er medlem av GG-Support.
• Jeg kjørte kommandoen gpupdate /force for å oppdatere gruppepolicyene og deretter gpresult /r for å kontrollere hvilke GPO-er som var brukt.
Resultat og kontroll

Da jeg kjørte gpresult /r på CLIENT01, så jeg både GPO-Support-Brukerinnstilling og GPO-Support-Test under «Applied Group Policy Objects». Dette bekreftet at GPO-ene ble brukt for den innloggede brukeren.

Jeg kontrollerte også at endringen fra brukerpolicyen var synlig på CLIENT01. Testen viste dermed både at policyen ble brukt, og at den hadde den forventede virkningen.

Steg 3 - oppdater og bevis at policyen gjelder

Mål

Jeg skulle oppdatere gruppepolicyene på CLIENT01 og dokumentere at riktig GPO faktisk ble brukt på en bruker i Support-OU-en.

Gjennomføring

• Jeg logget på CLIENT01 med domenebrukeren firma\sara.ahmed.
• Jeg åpnet Ledetekst (CMD) og kjørte kommandoen gpupdate /force for å oppdatere gruppepolicyene.
• Deretter kjørte jeg gpresult /r for å se hvilke gruppepolicyobjekter som ble brukt på brukerkontoen.
• Jeg kontrollerte delen «Applied Group Policy Objects» og tok et skjermbilde som dokumentasjon.
Resultat

I resultatet fra gpresult /r så jeg at både GPO-Support-Brukerinnstilling og GPO-Support-Test stod under «Applied Group Policy Objects». Jeg så også at brukeren var medlem av GG-Support og DL-Felles-Support-RW. Dette viser at de oppførte GPO-ene ble brukt for brukeren på CLIENT01.

Konklusjon

Jeg bekreftet med gpresult /r at GPO-Support-Brukerinnstilling ble brukt på Support-brukeren sara.ahmed. Jeg dokumenterte resultatet med et skjermbilde, slik at jeg kan vise at policyen er brukt og ikke bare konfigurert.

Dokumentasjon – gpresult /r



Figur 1: Jeg kontrollerte anvendte GPO-er med gpresult /r på CLIENT01.


Steg 4 - AD-detektiv

Mål

Jeg undersøkte en mulig feil i domenemiljøet firma.local. Jeg brukte flere kommandoer for å finne ut hvorfor CLIENT01 ikke fikk forventede DNS-svar og hvorfor en av IP-adressene til DC01 ikke kunne nås.

Symptom → hypotese → test → funn → løsning

Symptom

På CLIENT01 fikk jeg ikke forventet svar ved oppslag av LDAP-tjenesteposter. Jeg kunne heller ikke nå 192.168.1.10 med ping.

Hypotese

Jeg mistenkte feil eller uheldig DNS-konfigurasjon og undersøkte også om DC01 hadde flere nettverkskort og IP-adresser.

Test

Jeg brukte ipconfig /all, nslookup firma.local, nslookup med SRV-oppslag, ping og dcdiag /test:dns. Jeg kontrollerte også DNS Manager og IPv4-innstillingene på DC01.

Funn

CLIENT01 hadde IP-adressen 192.168.1.108 og brukte DNS-server 192.168.1.104. Ping til 192.168.1.104 fungerte, mens ping til 192.168.1.10 ga «Destination host unreachable». På DC01 fant jeg 192.168.1.10 på Ethernet og 192.168.1.104 på vEthernet. I DNS Manager fantes _ldap- og _kerberos-postene under firma.local/_tcp. dcdiag rapporterte likevel at DNS-testen feilet.

Tiltak og ny test

Jeg fjernet 192.168.1.1 som alternativ DNS-server på nettverkskortet med IP 192.168.1.10, slik at foretrukket DNS-server fortsatt var 192.168.1.10. Etterpå kjørte jeg dcdiag /test:dns på nytt. Testen viste fortsatt «failed».

Konklusjon

Jeg dokumenterte feilsøkingen og fant en mulig DNS-konfigurasjonsfeil, men jeg fikk ikke bekreftet at hele problemet var løst. Den tydeligste testen som avdekket DNS-problemet var dcdiag /test:dns, mens ping og nslookup hjalp meg med å avgrense feilen.

Kommandoer jeg brukte

• ipconfig /all
• nslookup firma.local
• nslookup -type=SRV _ldap._tcp.firma.local 192.168.1.104
• ping 192.168.1.10
• ping 192.168.1.104
• dcdiag /test:dns


Torsdagens grunnoppgave

Active Directory, GPO og feilsøking | Dokumentasjon i jeg-form

1. Mål og labmiljø

Jeg jobbet i domenet firma.local med domenekontrolleren DC01 og klientmaskinen CLIENT01. Målet mitt var å konfigurere og kontrollere en brukerpolicy, feilsøke en feil og forklare hvordan Active Directory-tjenestene henger sammen.

2. GPO knyttet til riktig OU

Jeg opprettet GPO-en «GPO-Support-Brukerinnstilling» i Group Policy Management og koblet den til Support-OU-en under Bedrift → Brukere → Support. Jeg valgte en enkel brukerinnstilling som kunne kontrolleres på CLIENT01, knyttet til visningen av papirkurvikonet på skrivebordet. Jeg testet policyen med domenebrukeren firma\sara.ahmed.

3. Oppdatering og bevis med gpresult

På CLIENT01 logget jeg på som sara.ahmed og kjørte disse kommandoene:

• gpupdate /force
• gpresult /r
gpupdate /force meldte at oppdateringen av bruker- og datamaskinpolicy var fullført. I gpresult /r så jeg «GPO-Support-Brukerinnstilling» og «GPO-Support-Test» under anvendte gruppepolicyobjekter for brukeren. Dette var den viktigste dokumentasjonen på at policyen faktisk ble mottatt. Jeg kontrollerte også den synlige brukerinnstillingen på skrivebordet.

Dokumentasjonsvedlegg: Sett inn skjermbildet av gpresult /r her dersom det skal leveres som bevis.

4. Selvstendig feilsøking – AD-detektiv

Trinn

Min dokumentasjon

Symptom

CLIENT01 fikk ikke kontakt med IP-adressen 192.168.1.10, og DNS-oppslag etter enkelte AD-tjenesteposter mislyktes.

Hypotese

Jeg mistenkte en feil i DNS-konfigurasjonen eller nettverksoppsettet på DC01.

Test

Jeg brukte ipconfig /all, nslookup, ping og dcdiag /test:dns. Jeg undersøkte også DNS Manager og IPv4-innstillingene.

Funn

CLIENT01 brukte DNS-server 192.168.1.104. Ping til 192.168.1.104 fungerte, mens ping til 192.168.1.10 ga «Destination host unreachable». DC01 hadde både 192.168.1.10 og 192.168.1.104 på ulike adaptere. DNS Manager viste _ldap- og _kerberos-poster i firma.local, men dcdiag rapporterte DNS-feil.

Tiltak

Jeg fjernet 192.168.1.1 som alternativ DNS-server fra IPv4-konfigurasjonen på adapteren med 192.168.1.10, slik at 192.168.1.10 sto som foretrukket DNS-server.

Kontroll og status

Jeg kjørte dcdiag /test:dns på nytt. Testen viste fortsatt «failed». Derfor kan jeg ikke dokumentere at feilen ble fullstendig løst. Videre feilsøking krever gjennomgang av den detaljerte dcdiag-rapporten og nettverksadapterne.

Testen som tydeligst avdekket DNS-problemet, var dcdiag /test:dns. Ping-testene avdekket i tillegg forskjellen i nettverkstilgang mellom de to IP-adressene.

5. Forskjellen mellom OU, gruppe og GPO

OU: Jeg bruker en organisasjonsenhet (OU) til å organisere AD-objekter og bestemme hvor en GPO skal kobles, for eksempel Support-OU.

Gruppe: Jeg bruker sikkerhetsgrupper til å samle brukere og tildele tilgang til ressurser. Sara var medlem av GG-Support og DL-Felles-Support-RW.

GPO: Jeg bruker gruppepolicyobjekter (GPO) til å styre bruker- eller datamaskininnstillinger, for eksempel en skrivebordsinnstilling på CLIENT01.

6. Hvordan tjenestene henger sammen

DNS hjelper CLIENT01 å finne domenekontrolleren og AD-tjenestene. Domenekontrolleren DC01 kjører AD DS, som lagrer objekter som brukere, grupper og OU-er. LDAP brukes til å søke etter og lese informasjon om disse objektene. Sikkerhetsgrupper styrer hvilke ressurser en bruker kan få tilgang til, sammen med delings- og NTFS-rettigheter. GPO-er kobles til nettsteder, domener eller OU-er og brukes til å konfigurere innstillinger. Jeg kan kontrollere hvilke policyer som gjelder med gpresult /r.

7. Kjeden forklart med mitt eget labmiljø

DNS → domenekontroller → AD-objekt → gruppe → ressurs → LDAP-søk → GPO → test

På CLIENT01 bruker jeg DNS for å finne domenet firma.local og domenekontrolleren DC01. På DC01 ligger AD-objektet sara.ahmed. Brukeren er medlem av GG-Support og DL-Felles-Support-RW, som brukes ved tilgangskontroll til Support-ressursen. Jeg kan undersøke brukerens og gruppenes opplysninger gjennom LDAP-baserte AD-oppslag, for eksempel med Get-ADUser og Get-ADGroupMember. Support-OU-en har GPO-en GPO-Support-Brukerinnstilling koblet til seg. Til slutt kjører jeg gpupdate /force og gpresult /r på CLIENT01 for å dokumentere at policyen er anvendt. DNS-feilsøkingen viste samtidig hvorfor fungerende navneoppløsning er viktig for domenet.

8. Videre utforskning (valgfrie oppgaver)

Læreren oppga flere valgfrie utvidelser: Security Filtering, HTML-rapport med gpresult /h, Salg-OU med brukere og LDAP-søk, CSV-automatisering, FILE01 og delegering. Disse er ikke dokumentert som utført i denne rapporten.

9. Oppsummering

Jeg har opprettet og testet en enkel GPO, dokumentert den med gpresult /r og gjennomført en systematisk feilsøkingsprosess. Jeg har også forklart forskjellen mellom OU, gruppe og GPO og hvordan DNS, AD DS, LDAP, grupper, ressurser og policyer henger sammen. DNS-feilen var fortsatt ikke fullstendig løst ved siste kontroll, og dette er oppgitt tydelig i rapporten.




















