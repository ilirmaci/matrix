voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 
        1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    cumulative = {}
    for l in voting_data:
        l = l.split()
        cumulative[l[0]] = [int(x) for x in l[3:]]
    return cumulative 
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
    >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
    >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
    -2
    """
    return sum([x*y for (x,y) in zip(voting_dict[sen_a], voting_dict[sen_b])])


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
    >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
    >>> most_similar('Klein', vd)
    'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    current_max = -60
    for k in voting_dict:
        sim = policy_compare(sen, k, voting_dict) if sen != k else -60
        if sim > current_max:
            current_max = sim
            closest = k
    return closest
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
    >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
    >>> least_similar('Klein', vd)
    'Ravella'
    """
    current_min = 60
    for k in voting_dict:
        sim = policy_compare(sen, k, voting_dict) if sen != k else 60
        if sim < current_min:
            current_min = sim
            furthest = k
    return furthest
    
    

## Task 5

votes = create_voting_dict()

most_like_chafee    = most_similar('Chafee', votes)
least_like_santorum = least_similar('Santorum', votes)

# Task 6

def get_party_set(party):
    '''(str) -> set
    Return set of senators from party.
    '''
    senators = set()
    for l in voting_data:
        l = l.split()
        if l[1] == party:
            senators.update({l[0]})
    return senators


def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
    >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
    >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
    -0.5
    """
    avg_record = find_average_record(sen_set, voting_dict)
    return sum([(x*y) for (x, y) in zip(voting_dict[sen], avg_record)])

def most_average(sen_set, voting_dict):
    '''(set, dict) -> str
    Return name of senator from sen_set whose voting record in voting_dict is most
    similar to the set average.
    '''
    greatest_sim = -50
    avg_record = find_average_record(sen_set, voting_dict)
    for senator in sen_set:
        sim = sum([(x*y) for (x, y) in zip(voting_dict[senator], avg_record)])
        if sim > greatest_sim:
            greatest_sim = sim
            most_avg = senator
    return senator

most_average_Democrat = 'Carper'

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
    >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
    >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
    [-0.5, -0.5, 0.0]
    """
    total = [0 for i in range(len(voting_dict))]
    denom = len(sen_set)
    for sen in sen_set:
        total = [x+y for (x, y) in zip(total, voting_dict[sen])]
    return [x/denom for x in total]

democrats = get_party_set('D')

average_Democrat_record = find_average_record(democrats, votes)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
    >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
    >>> bitter_rivals(voting_dict)
    ('Fox-Epstein', 'Ravella')
    """
    bitterest = (..., ...)
    furthest = 1000
    senators = list(voting_dict.keys())
    for i in range(len(senators)):
        for j in range(i, len(senators)):
            sim = policy_compare(senators[i], senators[j], voting_dict)
            if sim < furthest:
                furthest = sim
                bitterest = (senators[i], senators[j])
    return bitterest
