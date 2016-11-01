# Klingel
Das Ziel ist eine API zu schreiben über die ein Ton wiedergegeben werden kann. Das soll als Klingel im örtlichen Hackerspace vspace.one eingesetzt werden. Sodass man im ersten Schritt über das WLAN Netzwerk die Klingel auslösen kann. Im nächsten Schritt soll das Auslösen über eine Knopf, der an der Außenseite angebracht ist, auslöst werden. Das ist für diese API aber egal. Die API ist dafür gedacht auf einem RaspberryPi ausgeführt zu werden. Der Default-Pin ist der GPIO23.

## Ausführen
Zum Starten das Script `klingel.py` mit python ausführen. Dazu muss die RPi GPIO Lib installiert sein.

## Installieren
Zum Installieren bitte das Bash-Script `install.sh` mit Root-Rechten ausführen. Das aktuelle Installationsscript funktioniert nur für Distributionen die systemd verwenden. Bisher wurde nur Raspbian getestet.

Um den Service zu aktivieren ´systemctl enable klingel` ausführen. `systemctl status klingel` zeigt den Status an.

## Licence
GPLv2

## Todos
+ unterstütze mehrer unterschiedliche Events wie "Space-Status changed", "New User in IRC", ...

## Geräte und Tests
Bisher wurde das Script auf folgenden Geräten getestet:

Erfolgreich:
+ RaspberryPi 1, Rasbian

Nicht Erfolgreich:

## Credits
+ [https://pypi.python.org/pypi/RPi.GPIO](RPi.GPIO)
