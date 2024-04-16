"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...
    """For finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, path):
        """Read Dictionary and reports item read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")


    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in dict_file]
    

    def random(self):
        """random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Speclized word finder excludes blank lines
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip()and not w.startswith('#')]

   




