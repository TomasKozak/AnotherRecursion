Veľký štvorec môžeme rozdeliť na 4 kvadranty.

Úplne rovnako môžeme každý kvadrant rozdeliť na menšie kvadranty.

Vidíte, že tieto menšie kvadranty v 2 sú očíslované ako 21, 22, 23, 24. Ľubovoľný kvadrant môžeme rozdeliť na 4 menšie.

Takýmto delením môžeme ísť do nejakej danej hĺbky n, kým neprídeme na elementárny štvorček, ktorý sa už deliť nedá. Napr. hĺbka n=1 znamená, že plocha sa skladá z 2x2 elementárnych štvorčekov a deliť ju môžeme maximálne raz na 4 základné kvadranty. Hĺbka n=4 označuje 16x16 elementárnych štvorčekov, ktorú môžeme deliť maximálne 4-krát. Potom napr. kvadrant 2 je veľký 8x8 elementárnych štvorčekov, kvadrant 23 zaberá 4x4 štvorčekov, kvadrant 234 zaberá 2x2 štvorčeky a zrejme 2343 už len jeden. Teda pre dané n poradové číslo kvadrantu má zmysel s maximálnym počtom cifier n. Čím má číselné označenie kvadrantu menej cifier, tým je kvadrant väčší (napr. 0-ciferné číslo kvadrantu označuje celý štvorec).

Napíšte pythonovský modul, ktorý bude obsahovať jedinú triedu Stvorce a žiadne iné globálne premenné:
