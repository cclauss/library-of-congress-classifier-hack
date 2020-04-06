#!/usr/bin/env python3

from lcc_classifier import find_classification_strings, lcc_to_classification

test_cases = {
    "DP402.C8 O46 1995": [
        "World History and History of Europe",
        "Asia, Africa, Australia, New Zealand, Etc.",
        "History of Spain",
        "Local history and description",
        "Other cities, towns, etc., A-Z",
    ],
    "DR1313.3 .U54 1993": [
        "World History and History of Europe",
        "Asia, Africa, Australia, New Zealand, Etc.",
        "History of Spain",
        "Local history and description",
        "Other cities, towns, etc., A-Z",
    ],
    "DR82 .G46 1993": [
        "World History and History of Europe",
        "Asia, Africa, Australia, New Zealand, Etc.",
        "History of Spain",
        "Local history and description",
        "Other cities, towns, etc., A-Z",
    ],
    "DS557.8.M9 B55 1992B": [
        "World History and History of Europe",
        "Asia, Africa, Australia, New Zealand, Etc.",
        "History of Spain",
        "Local history and description",
        "Other cities, towns, etc., A-Z",
    ],
    "HM216 .G44 1993": [
        "Social sciences",
        "Sociology",
        "These are obsolete numbers no longer used by the Library of Congress",
    ],
    "HM261 .H47 1993": [
        "Social sciences",
        "Sociology",
        "These are obsolete numbers no longer used by the Library of Congress",
    ],
    "HN530.2.A85 I86 1992": [
        "Social sciences",
        "Social history and conditions. Social problems. Social Reform",
        "By region or country",
    ],
    "HQ755.8 .T63 1995": [
        "Social sciences",
        "The Family. Marriage. Women",
        "The family. Marriage. Home",
        "Parents. Parenthood",
    ],
    "KF27 .A3 1992H": [
        "Law",
        "Law of the United States",
        "Federal law. Common and collective state law: Individual states",
    ],
    "KF3613.4 .C34": [
        "Law",
        "Law of the United States",
        "Federal law. Common and collective state law: Individual states",
    ],
    "KHA878 .G37 1996": ["Law", "South America (General)", "Argentina"],
    "KHH3003 .Q57 1995": ["Law", "South America (General)", "Argentina"],
    "KK2222 .L36 1993": ["Law", "Europe", "Germany", "Germany and West Germany"],
    "KLA940 .K65 1990": [
        "Law",
        "Asia and Eurasia, Africa, Pacific Area, and Antarctica",
        "Eurasia",
        "Russia. Soviet Union",
    ],
    "SD418 .A38 1990": [
        "Agriculture",
        "Forestry",
        (
            "Conservation and protection: Including forest influences, damage by "
            "elements, fires, forest reserves"
        ),
    ],
    "TK5105.5 .O653 1993": [
        "Technology",
        "Electrical engineering. Electronics. Nuclear engineering",
        "Telecommunication: Including telegraphy, telephone, radio, radar, television",
    ],
}


def test_function():
    """
    >>> for i, (key, value) in enumerate(test_cases.items()):
    >>>     lcc_to_classification(key) == value
    >>>  lcc_to_classification("MLCM 95/14118 (P)")
    ['Medium size', '1995', 'Language and Literature']
    """
    pass


if __name__ == "__main__":
    import doctest

    find_classification_strings()
    
    errors = 0
    for key, value in test_cases.items():
        classification = lcc_to_classification(key)
        try:
            assert classification == value, f"{key}:\n{classification} != \n{value}"
        except AssertionError as e:
            errors += 1
            print(e)
    if errors:
        exit(errors)
            
    doctest.testmod()
