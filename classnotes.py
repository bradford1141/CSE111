def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """

    if quantity == 1:
        prepositional = [""]


def test_get_prepositional_phrase():
    prep_phrase = [""]
    for in range(2):
        prepositinal = get_prepositional_phrase(1)
        assert prepositinal in prep_phrase

print(f"{get_prepositional_phrase(quantity=1)}.")