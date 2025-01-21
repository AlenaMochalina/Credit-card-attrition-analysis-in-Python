# Credit-card-attrition-analysis-in-Python

Tento projekt se zaměřuje na analýzu odchodu zákazníků pro společnost vydávající kreditní karty. Cílem je identifikovat klíčové faktory přispívající k úbytku zákazníků a poskytovat doporučení pro cílené retenční kampaně.

##Datová sada
Datová sada obsahuje informace o zákaznících shromážděné z portfolia spotřebitelských kreditních karet. Jejím cílem je pomoci analytikům předvídat odchod zákazníků. Obsahuje:

Demografické údaje: věk, pohlaví, rodinný stav a příjmová kategorie.
Informace o vztahu zákazníka s poskytovatelem kreditní karty: typ karty, počet měsíců od registrace, období neaktivity.
Chování zákazníků při výdajích: revolvingový zůstatek, úvěrový limit, průměrná míra nákupu.
Analyzovatelné metriky: změna výdajů mezi čtvrtletími, průměrný poměr využití, počet kontaktů za 12 měsíců, úroveň vzdělání a další.
Dataset byl získán z tohoto zdroje: https://zenodo.org/records/4322342#.Y8OsBdJBwUE

##Metody analýzy
Pro zpracování dat jsme použili následující metody strojového učení:

Shlukování: Segmentace zákazníků do skupin na základě podobných charakteristik.
Klasifikace: Predikce odchodu zákazníka (attrition) na základě dostupných dat.
##Klíčové výsledky
Shlukování
Nejvíce odcházejí ženy ve věku 43–50 let s nejnižšími příjmy.
Na základě těchto zjištění mohou být zavedeny cílené retenční kampaně, například:
Personalizované nabídky.
Zlepšené služby.
Speciální loajální programy.
Klasifikace
Byl vytvořen model klasifikace, který dokáže identifikovat zákazníky s vysokou pravděpodobností odchodu. Tento model může sloužit jako nástroj pro cílené retenční strategie.

##Ukázka analýzy
Celou datovou analýzu si můžete prohlédnout v souboru:  
**[Credit-card-attrition-analysis-in-Python.ipynb](https://github.com/AlenaMochalina/Credit-card-attrition-analysis-in-Python/blob/main/Credit-card-attrition-analysis-in-Python.ipynb)**


