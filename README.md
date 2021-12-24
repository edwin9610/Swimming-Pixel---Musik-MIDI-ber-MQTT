# Swimming-Pixel---MusikMIDI-over-MQTT
## Einführung
Die Stadt Karlsruhe wurde 2019 von der UNESCO mit dem Titel City of Media Arts ausgezeichnet. Repräsentativ für diese Auszeichnung stehen Events, wie die Schlosslichtspiele, aber auch dauerhafte Einrichtungen, wie zum Beispiel das ZKM. Die Hochschule Karlsruhe möchte sich ebenfalls daran beteiligen, die Stadt durch mediale Kunst einzigartig zu machen.

So soll im Rahmen der Lehrveranstaltungen von EU4M Mikrokontroller, energieeffiziente Mikrokwontroller und Mechatronik Dialog das Projekt Simming Pixels verwirklicht werden. Hierzu sollen die Studierenden schwimmende LED-Pixel konstruieren, die unteranderem mit Hilfe der Musik-MIDI abgespielt werden können und somit den Schlossteich mit verschiedenen Lichtsequenzen erstrahlen lassen.

Dokumentation: http://hit-karlsruhe.de/hit-info/info-ws21/SP-MD/

## Aufgabenstellung
Ziel der Aufgabe ist, dass sich eine Lightshow nach dem Takt einer Musik darstellen lässt. Damit die Signale der MIDI einer Musik erfasst werden können, müssen die Signale zuerst auf Studio One bearbeitet werden. Die Signale umfassen velocity, pitch, etc. der Musik und werden vom Studio One exportiert. Die können dann mit Python programmiert und den einzelnen ESP32 zugeordnet werden. Die Übertragung der Nachrichten zwischen Python und ESP32 erfolgt über MQTT.

Link zum Youtube: https://youtu.be/OSWcBiRY-Ac
