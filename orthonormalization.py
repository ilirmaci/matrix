def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    from orthogonalization import orthogonalize
    from math import sqrt
    
    L_star = orthogonalize(L)
    return [v/sqrt(v*v) for v in L_star]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    from orthogonalization import aug_orthogonalize
    from math import sqrt
    
    (Qlist, Rlist) = aug_orthogonalize(L)
    # Rlist rows to be scaled up by norm of Qlist vectors
    Rmult = [sqrt(v*v) for v in Qlist]
    Qmult = [1/x for x in Rmult]
    
    return ([x*v for (x,v) in zip(Qmult, Qlist)],
            [adjust(Rmult, w) for w in Rlist])
    
def adjust(multipliers, v):
    '''(list of num, Vec) -> Vec
    Return vector with same domain as v and each entry multiplied by
    corresponding factor in multipliers, i.e. the entry-by-entry product
    as if multipliers were a Vec.
    Prerequisite: v.D = {1, 2, ..., len(v.D)-1}
    '''
    from vec import Vec
    return Vec(v.D, {k:multipliers[k]*v[k] for k in v.f})
