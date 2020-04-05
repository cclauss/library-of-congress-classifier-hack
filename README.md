# Library of Congress classifier hack
Convert Library of Congress classification codes into the classification of a particular work.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cclauss/library-of-congress-classifier-hack/master) and once it has booted up, click the __lcc_classifier.ipynb__ file.

### Organize classification data
This borrows heavily from https://github.com/thisismattmiller/lcc-pdf-to-json to parse the classification data out of .pdf files at http://www.loc.gov/aba/publications/FreeLCC/freelcc.html

### Classify a work based on its Library of Congress Classification code


Open Library ID | Library of Congress Classification code
-- | --
[OL1025841M](https://openlibrary.org/books/OL1025841M) | [HB1951 .R64 1995](https://openlibrary.org/books/HB1951.R641995)
[OL1025966M](https://openlibrary.org/books/OL1025966M) | [DP402.C8 O46 1995](https://openlibrary.org/books/DP402.C8O461995)
[OL1026156M](https://openlibrary.org/books/OL1026156M) | [CS879 .R3 1995](https://openlibrary.org/books/CS879.R31995)
[OL1026211M](https://openlibrary.org/books/OL1026211M) | [NC248.S22 A4 1992](https://openlibrary.org/books/NC248.S22A41992)
[OL102629M](https://openlibrary.org/books/OL102629M) | [TJ563 .P66 1998](https://openlibrary.org/books/TJ563.P661998)
[OL1026596M](https://openlibrary.org/books/OL1026596M) | [PQ3919.2.M2866 C83 1994](https://openlibrary.org/books/PQ3919.2.M2866C831994)
[OL1026624M](https://openlibrary.org/books/OL1026624M) | [NA2500 .H64 1995](https://openlibrary.org/books/NA2500.H641995)
[OL1026668M](https://openlibrary.org/books/OL1026668M) | [PN517 .L38 1994](https://openlibrary.org/books/PN517.L381994)
[OL1026747M](https://openlibrary.org/books/OL1026747M) | [MLCM 95/14118 (P)](https://openlibrary.org/books/MLCM95/14118(P))
[OL102706M](https://openlibrary.org/books/OL102706M) | [QA331.3 .M39 1998](https://openlibrary.org/books/QA331.3.M391998)
[OL1027106M](https://openlibrary.org/books/OL1027106M) | [PT8951.12.R5 M56 1980](https://openlibrary.org/books/PT8951.12.R5M561980)
[OL1027418M](https://openlibrary.org/books/OL1027418M) | [MLCS 96/04520 (P)](https://openlibrary.org/books/MLCS96/04520(P))
[OL1027454M](https://openlibrary.org/books/OL1027454M) | [HQ755.8 .T63 1995](https://openlibrary.org/books/HQ755.8.T631995)
[OL1028019M](https://openlibrary.org/books/OL1028019M) | [MLCS 97/02275 (T)](https://openlibrary.org/books/MLCS97/02275(T))
[OL1028055M](https://openlibrary.org/books/OL1028055M) | [PZ70.C9 F657 1995](https://openlibrary.org/books/PZ70.C9F6571995)
[OL1028253M](https://openlibrary.org/books/OL1028253M) | [HC241 .G683 1995](https://openlibrary.org/books/HC241.G6831995)
[OL1028626M](https://openlibrary.org/books/OL1028626M) | [MLCS 95/08574 (U)](https://openlibrary.org/books/MLCS95/08574(U))
[OL1028701M](https://openlibrary.org/books/OL1028701M) | [HC371 .M45 nr. 122](https://openlibrary.org/books/HC371.M45nr.122)
[OL102878M](https://openlibrary.org/books/OL102878M) | [MLCS 2002/05802 (P)](https://openlibrary.org/books/MLCS2002/05802(P))
[OL1029016M](https://openlibrary.org/books/OL1029016M) | [IN PROCESS](https://openlibrary.org/books/INPROCESS)
[OL102935M](https://openlibrary.org/books/OL102935M) | [KLA940 .K65 1990](https://openlibrary.org/books/KLA940.K651990)
[OL1029463M](https://openlibrary.org/books/OL1029463M) | [KHA878 .G37 1996](https://openlibrary.org/books/KHA878.G371996)
[OL1029540M](https://openlibrary.org/books/OL1029540M) | [KHH3003 .Q57 1995](https://openlibrary.org/books/KHH3003.Q571995)
[OL1030429M](https://openlibrary.org/books/OL1030429M) | [TX819.A1 T733 1991](https://openlibrary.org/books/TX819.A1T7331991)
[OL1030465M](https://openlibrary.org/books/OL1030465M) | [PQ7298.12.A40 S26 1987](https://openlibrary.org/books/PQ7298.12.A40S261987)
[OL1030780M](https://openlibrary.org/books/OL1030780M) | [HM216 .G44 1993](https://openlibrary.org/books/HM216.G441993)
[OL1030894M](https://openlibrary.org/books/OL1030894M) | [SD409 .A38 1990](https://openlibrary.org/books/SD409.A381990)
[OL1031493M](https://openlibrary.org/books/OL1031493M) | [J451 .N4 1990z](https://openlibrary.org/books/J451.N41990z)
[OL1031615M](https://openlibrary.org/books/OL1031615M) | [TR850 .F88 1993](https://openlibrary.org/books/TR850.F881993)
[OL1031659M](https://openlibrary.org/books/OL1031659M) | [MLCS 93/14492 (P)](https://openlibrary.org/books/MLCS93/14492(P))
[OL1031710M](https://openlibrary.org/books/OL1031710M) | [KK2222 .L36 1993](https://openlibrary.org/books/KK2222.L361993)
[OL1031822M](https://openlibrary.org/books/OL1031822M) | [G525 .M486 1991](https://openlibrary.org/books/G525.M4861991)
[OL1032690M](https://openlibrary.org/books/OL1032690M) | [HM261 .H47 1993](https://openlibrary.org/books/HM261.H471993)
[OL1032795M](https://openlibrary.org/books/OL1032795M) | [PQ8098.23.O516 L38 1988](https://openlibrary.org/books/PQ8098.23.O516L381988)
[OL1032953M](https://openlibrary.org/books/OL1032953M) | [PL191 .I94 1992](https://openlibrary.org/books/PL191.I941992)
[OL1033073M](https://openlibrary.org/books/OL1033073M) | [LF3194.C65 A657 1992](https://openlibrary.org/books/LF3194.C65A6571992)
[OL103482M](https://openlibrary.org/books/OL103482M) | [PG5438.V25 J47 1999](https://openlibrary.org/books/PG5438.V25J471999)
[OL1035916M](https://openlibrary.org/books/OL1035916M) | [HG1615 .M32 1993](https://openlibrary.org/books/HG1615.M321993)
[OL1036001M](https://openlibrary.org/books/OL1036001M) | [KF27 .A3 1992h](https://openlibrary.org/books/KF27.A31992h)
[OL103608M](https://openlibrary.org/books/OL103608M) | [PT1937.A1 G35 1999](https://openlibrary.org/books/PT1937.A1G351999)
[OL1036126M](https://openlibrary.org/books/OL1036126M) | [MLCS 98/02371 (H)](https://openlibrary.org/books/MLCS98/02371(H))
[OL1036553M](https://openlibrary.org/books/OL1036553M) | [MLCM 93/05262 (D)](https://openlibrary.org/books/MLCM93/05262(D))
[OL1036719M](https://openlibrary.org/books/OL1036719M) | [KF3613.4 .C34](https://openlibrary.org/books/KF3613.4.C34)
[OL1036755M](https://openlibrary.org/books/OL1036755M) | [DR1313.3 .U54 1993](https://openlibrary.org/books/DR1313.3.U541993)
[OL1037020M](https://openlibrary.org/books/OL1037020M) | [DS557.8.M9 B55 1992b](https://openlibrary.org/books/DS557.8.M9B551992b)
[OL1037176M](https://openlibrary.org/books/OL1037176M) | [DR82 .G46 1993](https://openlibrary.org/books/DR82.G461993)
[OL1037305M](https://openlibrary.org/books/OL1037305M) | [PT2678.E3393 S36 1993](https://openlibrary.org/books/PT2678.E3393S361993)
[OL1037349M](https://openlibrary.org/books/OL1037349M) | [HN530.2.A85 I86 1992](https://openlibrary.org/books/HN530.2.A85I861992)
[OL1037631M](https://openlibrary.org/books/OL1037631M) | [TK5105.5 .O653 1993](https://openlibrary.org/books/TK5105.5.O6531993)
[OL1038111M](https://openlibrary.org/books/OL1038111M) | [AM79.5.B26 B34 1993](https://openlibrary.org/books/AM79.5.B26B341993)
