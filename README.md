# Willkommen zum Scam-Checker Backend

Scam-Checker benutzt verschiedene Wege Scamming, Pishing, Social Engineering und Viren zu erkennen und dich davor zu
warnen. Die Website kann 0-100 Punkte erreichen. 100 Punkte ist das beste und wird von uns somit nicht als gefährlich
erkannt. Dies ist das Schul Informatik Projekt von Dominic und Leo

## Phishing Database

Wir benutzten eine Database mit circa 75000 Domains, die Phishing sind, um mögliche Phishing Websites zu identifizieren.
Diese Database wurde von [Leo](https://github.com/Yuutokata/Pishing-Database) erstellt, sie ist gratis und kann von
jedem benutzt werden.

## Google SafeBrowsing API

Wir benutzen ebenfalls eine API von Google, die Malware, Social Engineering, möglich gefährliche Websites und
ungewünschte Software erkennen.

URLs zum Testen finden sie [hier](https://testsafebrowsing.appspot.com/)

## PyFunceble

Wir benutzen die Library PyFunceble, die ein DNS Lookup und die WHOIS Records überprüft. Da dies nicht unsere eigene
Library ist können wir leider keine URLs zum Testen vorlegen.
PyFunceble ist aber eine sehr bekannte und verlässliche Library, um dies zu überprüfen.
