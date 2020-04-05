tests = {
    "DP402.C8 O46 1995": ['World History and History of Europe', 'Asia, Africa, Australia, New Zealand, Etc.', 'History of Spain', 'Local history and description', 'Other cities, towns, etc., A-Z'],
    "MLCM 95/14118 (P)": ['Medium size', '1995', 'Language and Literature'],
    "HQ755.8 .T63 1995":
        ['Social sciences', 'The Family. Marriage. Women', 'The family. Marriage. Home', 'Parents. Parenthood'],
    "KLA940 .K65 1990":
        ['Law', 'Asia and Eurasia, Africa, Pacific Area, and Antarctica', 'Eurasia', 'Russia. Soviet Union'],
    "KHA878 .G37 1996":
        ['Law', 'South America (General)', 'Argentina'],
    "KHH3003 .Q57 1995":
        ['Law', 'South America (General)', 'Argentina'],
    "HM216 .G44 1993":
        ['Social sciences', 'Sociology', 'These are obsolete numbers no longer used by the Library of Congress'],
    "SD418 .A38 1990":
        ['Agriculture', 'Forestry', 'Conservation and protection: Including forest influences, damage by elements, fires, forest reserves'],
    "KK2222 .L36 1993":
        ['Law', 'Europe', 'Germany', 'Germany and West Germany'],
    "HM261 .H47 1993":
        ['Social sciences', 'Sociology', 'These are obsolete numbers no longer used by the Library of Congress'],
    "KF27 .A3 1992H":
        ['Law', 'Law of the United States', 'Federal law. Common and collective state law: Individual states'],
    "KF3613.4 .C34":
        ['Law', 'Law of the United States', 'Federal law. Common and collective state law: Individual states'],
    "DR1313.3 .U54 1993":
        ['World History and History of Europe', 'Asia, Africa, Australia, New Zealand, Etc.', 'History of Spain', 'Local history and description', 'Other cities, towns, etc., A-Z'],
    "DS557.8.M9 B55 1992B":
        ['World History and History of Europe', 'Asia, Africa, Australia, New Zealand, Etc.', 'History of Spain', 'Local history and description', 'Other cities, towns, etc., A-Z'],
    "DR82 .G46 1993":
        ['World History and History of Europe', 'Asia, Africa, Australia, New Zealand, Etc.', 'History of Spain', 'Local history and description', 'Other cities, towns, etc., A-Z'],
    "HN530.2.A85 I86 1992":
        ['Social sciences', 'Social history and conditions. Social problems. Social Reform', 'By region or country'],
    "TK5105.5 .O653 1993":
        ['Technology', 'Electrical engineering. Electronics. Nuclear engineering', 'Telecommunication: Including telegraphy, telephone, radio, radar, television'],
}


def test_function():
    """
    >>> from lcc_classifier import lcc_to_classification
    >>> for i, key, value in enumerate(tests.items()):
    >>>     lcc_to_classification(key) == value
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
