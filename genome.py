def get_ngrams(seq, n):
    """Returns the ngrams of the sequence.
    Parameter: seq is a string
               n is the number to get.
    Returns: a set of ngrams.
    Pre-conditions: seq is a string
                    n is an int.
    Post-conditions: A set is returned."""
    return set([seq[i:n + i] for i in range(len(seq)) if len(seq[i:n+i]) == n])

class GenomeData:
    """Abstracts the Genome data for an organism.

    Attributes: _id is the organism ID.
                _sequence is the genome sequence.
                _ngrams is the set of ngrams for the sequence.
    Methods: __init__ is the constructor.
             id getter for _id.
             sequence getter for _sequence.
             ngrams getter for _ngrams."""

    def __init__(self, identity, seq, n):
        """Constructor for GenomeData.
        Parameters: identity is the id of the organism.
                    seq is the genome sequence.
                    n is the ngram number.
        Returns: GenomeData
        Pre-conditions: identity is a string
                        seq is a string
                        n is an int
        Post-conditions: A GenomeData is born."""
        self._id = identity
        self._sequence = seq
        self._ngrams = get_ngrams(seq, n)

    def id(self):
        """Getter for _id.
        Parameters: None
        Returns: _id
        Pre-conditions: None
        Post-conditions: a string is returned."""
        return self._id

    def sequence(self):
        """Getter for _sequence
        Parameters: None
        Returns: a string
        Pre-conditions: None
        Post-conditions: A string is returned."""
        return self._sequence

    def ngrams(self):
        """Getter for ngrams.
        Parameters: None
        Returns: a set of ngram.
        Pre-conditions: None
        Post-conditions: a set is returned."""
        return self._ngrams

    
