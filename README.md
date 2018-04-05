# jaarkalender
Jaarkalender met weeknummers

Invoer is een jaartal, waarna het jaar per kwartaal wordt afgedrukt. Per week wordt het ISO-weeknummer gegeven.

Overwegingen bij het ontwerp:
1. Het programma is procedureel opgezet. Dit omdat ik nog niet bekend ben met OO binnen Python.

2. Indexering: Bij de datastructuur kalender is een dummy maand toegevoegd zodat januari, maand 1, ook index 1 heeft. Hetzelfde geldt voor de indexering van de dagen in de maand.

3. Het ontwerp is gebaseerd op het decorator-principe. We beginnen met een lijst dagnummers en verrijken die met steeds meer informatie (trailers en weeknummers) zodat de maand uiteindelijk als een vierkant kan worden uitgeprint.

4. Na decoratie is de info beschikbaar als 2D matrix zodat deze ook goed te verwerken is via template engines zoals Ninja.



