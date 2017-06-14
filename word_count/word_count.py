def words(statement):
    """
        Function that takes in a statement and returns a dictionary with words
        use in in the statement as keys and the number of times the words has
        been used as values.
    """

    words_dict = {}
    if isinstance(statement, str):
        words = statement.split()
    else:
        raise TypeError('Function only takes in strings')

    for word in words:
        if word not in words_dict:
            if word.isdigit():
                words_dict[int(word)] = 1
            else:
                words_dict[word] = 1
        else:
            if word.isdigit():
                words_dict[int(word)] += 1
            else:
                words_dict[word] += 1

    return words_dict
