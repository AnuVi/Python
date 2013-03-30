def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    nume = 0
    for char in dna:
        nume = nume + 1
    return nume
    
    



def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    if (get_length(dna1)> get_length(dna2)):
        return True
    else:
         return False




def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    nuc = 0
    for char in dna:
        if char in nucleotide:
            nuc = nuc+1
    return nuc



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    if dna2[0:] in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    '''
    (str) -> bool
    Return True if and only if DNA consists of 'A', 'T','C','G'
    >>> is_valid_sequence('ATCGCA')
    True
    >>> is_valid_sequence('ATcGCA')
    False
    '''
    nuc_not = 0
    for char in dna:
        if char not in ('ATCG'):
            nuc_not = nuc_not+1
    if(nuc_not > 0):
        return False
    else:
        return True
    
def insert_sequence(dna1, dna2, index):
    '''
    Return string there dna2 is placed ig given idnex  in dna1
    >>>insert_sequence('CCGG', 'AT',2)
    'CCATGG'
    '''
    if (len(dna1)<index):
        return 'Dna1 is smaller than your given index'
    elif(len(dna1)==1 & index==1):
        seq = dna1[0]+dna2
        return seq
    else:
        seq = dna1[:index]+dna1[index]+dna2 + dna1[index:]
        return seq
def get_complement (nucleotide):
    '''
     (str) -> str
     Return compplement nucleotide of a given nucleotide
     >>>get_complement ('A')
     ' T'
    '''
    if (nucleotide=='A'):
        return 'T'
    elif (nucleotide=='T'):
        return 'A'
    elif (nucleotide=='C'):
        return 'G'
    elif (nucleotide=='G'):
        return 'C'

def complementary_sequence(dna):
    '''
    (str) -> str
     Return the DNA sequence that is complementary to the given DNA sequence.
     >>>get_complementary_sequence('AT')
     'TA'
    '''
    st=''
    for char in dna:
         c=get_complement(char)
         st +=c
    return st

