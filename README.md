https://openlibrary.org/query.json?type=/type/edition&isbn_~=1*&limit=100

# Library of Congress classifier hack
Convert Library of Congress classification codes into the classification of a particular work.
* https://www.terkko.helsinki.fi/files/9666/classify_trnee_manual.pdf
* https://ejournals.bc.edu/index.php/ital/article/download/11585/9839/

### Organize classification data
This borrows heavily from https://github.com/thisismattmiller/lcc-pdf-to-json to parse the classification data out of .pdf files at http://www.loc.gov/aba/publications/FreeLCC/freelcc.html

### Classify a work based on its Library of Congress Classification code

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cclauss/library-of-congress-classifier-hack/master)

Once that boots up, open the __lcc_classifier.ipynb__ file.
