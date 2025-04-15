
# Workshop micro:bit met # Cutebot
Tijdens deze workshop gaan we aan de slag met micro:bit in combinatie met de Cutebot. In de Git repository staan in de src folder twee mappen:

- cutebot-timing
- cutebot-gyro

## cutebot-timing
Om te kijken welke kant de robot op kan gaan draait de robot aan de hand van timing. Wanneer de robot op een "kruispunt" terecht komt kijkt de robot eerst of hij rechtdoor kan, vervolgens gaat hij links en rechts draaien om te controleren of er een lijn is. De robot draait maximaal voor een vooraf geconfigureerde tijd. Deze tijd is geconfigureerd in MAX_DIRECTION_CHECK_TIME. Wanneer er geen lijn is gevonden draait de robot terug en gaat hij een andere kant controleren. Tijdens het draaien wordt pas na een bepaalde tijd gecontroleerd of er een lijn is. Deze waarde is geconfigureerd in DIRECTION_CHECK_DELAY. Dit is om ervoor te zorgen dat de huidige lijn niet als optie wordt gezien wanneer links of rechts gecontroleerd wordt. Afhankelijk van de baterijstatus kunnen de SPEED en de DRIVE_WHILE_LOST_LINE_TIME aangepast worden. Hoe voller de batterij, hoe lager de speed. De DRIVE_WHILE_LOST_LINE_TIME wordt gebruikt om nog een klein stukje door te rijden wanneer de lijn niet meer gezien wordt.

## cutebot-gyro
Om gebruik te maken van deze versie moet de GY-271 aangesloten worden. Het interne kompas van de micro:bit kan alleen gebruikt worden wanneer dit bordje horizontaal is aangesloten. Op de cutecar gaat dit niet. Net als bij de cutebot-timing zijn hier ook de SPEED en de DRIVE_WHILE_LOST_LINE_TIME van toepassing.

Deze versie maakt gebruik van het kompas om te draaien en weer terug te draaien. In theorie zou dit betrouwbaarder moeten zijn dan de timing versie. Het kompas moet echter wel zover mogelijk van de cutebot geplaatst worden om te interferentie te voorkomen. Het kompas lijkt hier erg gevoelig voor te zijn.

### Verbeteringen
- Maak gebruik van de ultrasonic sensor om muren te herkennen
- Het doolhof is een 7x7 grid, probeer de kortste weg te vinden.
- Herken andere robots in het doolhof
- Herkennen uitgang doolhof (ultrasonic sensor kan ver kijken > 100cm)

### Links:
- [Smart Cutebot Samples for Python](https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot-python.html)
- [IDE in de browser](https://python.microbit.org/v/beta)
- [micro:bit Python VSCode](https://marketplace.visualstudio.com/items?itemName=MAKinteract.micro-bit-python)






