import re

class InvalidAffixPairSpecification(object):
    """Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 26
    
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """
    def isSatisfiedBy(self, word):
        if re.match(r'^me(.*)kan$', word):
            return False

        if word == 'ketahui':
            return False

        invalidAffixes = [r'^ber(.*)i$',
            r'^di(.*)an$',
            r'^ke(.*)i$',
            r'^ke(.*)an$',
            r'^me(.*)an$',
            r'^me(.*)an$',
            r'^ter(.*)an$',
            r'^per(.*)an$']

        contains = False
        for invalidAffix in invalidAffixes:
            contains = contains or re.match(invalidAffix, word)

        return contains


