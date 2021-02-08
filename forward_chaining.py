class Clause:
    def __init__(self, premise, conclusion):
        self.premise = premise
        self.conclusion = conclusion
        self.count = len(premise)

class KB:
    def __init__(self, clauses, propositions):
        self.clauses = clauses
        self.propositions = propositions

def forward_chaining(kb, q):
    agenda = kb.propositions

    list_ = []
    for clause in kb.clauses:
        for proposition in clause.premise:
            list_.append(proposition)
        list_.append(clause.conclusion)
    for proposition in kb.propositions:
        list_.append(proposition)

    set_ = set(list_)
    infered = {}
    for proposition in set_:
        infered[proposition] = False

    while len(agenda) > 0:
        proposition = agenda.pop()
        if proposition == q:
            return True
        if infered[proposition] == False:
            infered[proposition] = True
            for clause in kb.clauses:
                if proposition in clause.premise:
                    clause.count -= 1
                    if clause.count == 0:
                        agenda.append(clause.conclusion)
    return False

# u: people have umbrellas
# o: Alice is outside
# r: it is raining
# w: alice is wet
'''
clause_raining = Clause(['u'], 'r')
clause_wet = Clause(['o','r'],'w')
clauses = [clause_raining, clause_wet]
propositions = ['u','o']
q = 'w'
'''

'''
c1 = Clause(['p'], 'q')
c2 = Clause(['l','m'], 'p')
c3 = Clause(['b','l'], 'm')
c4 = Clause(['a','p'], 'l')
c5 = Clause(['a','b'], 'l')
clauses = [c1, c2, c3, c4, c5]
propositions = ['a','b']
q = 'q'
'''

'''
# simplified wumpus world
c1 = Clause(['s11','-w21'],'w12')
c2 = Clause(['s11','-w12'],'w21')
c3 = Clause(['s12','-w22'],'w11')
c4 = Clause(['s12','-w11'],'w22')
c5 = Clause(['s31','-w32'],'w21')
c6 = Clause(['s31','-w21'],'w32')

c7 = Clause(['s21', '-w11','-w22'],'w31')
c8 = Clause(['s21', '-w11','-w31'],'w22')
c9 = Clause(['s21', '-w22','-w31'],'w11')

c10 = Clause(['s22', '-w32','-w21'],'w12')
c11 = Clause(['s22', '-w32','-w12'],'w21')
c12 = Clause(['s22', '-w21','-w12'],'w32')

c13 = Clause(['w11'],'-w12')
c14 = Clause(['w12'],'-w11')
c15 = Clause(['w11'],'-w22')
c16 = Clause(['w22'],'-w11')
c17 = Clause(['w11'],'-w21')
c18 = Clause(['w21'],'-w11')
c19 = Clause(['w11'],'-w33')
c20 = Clause(['w33'],'-w11')
c21 = Clause(['w11'],'-w31')
c22 = Clause(['w31'],'-w11')

c23 = Clause(['w12'],'-w21')
c24 = Clause(['w21'],'-w12')
c25 = Clause(['w12'],'-w22')
c26 = Clause(['w22'],'-w12')
c27 = Clause(['w12'],'-w31')
c28 = Clause(['w31'],'-w12')
c29 = Clause(['w12'],'-w32')
c30 = Clause(['w32'],'-w12')

c31 = Clause(['w21'],'-w22')
c32 = Clause(['w22'],'-w21')
c33 = Clause(['w21'],'-w31')
c34 = Clause(['w31'],'-w21')
c35 = Clause(['w21'],'-w32')
c36 = Clause(['w32'],'-w21')

c37 = Clause(['w22'],'-w31')
c38 = Clause(['w31'],'-w22')
c39 = Clause(['w22'],'-w33')
c40 = Clause(['w33'],'-w22')

c41 = Clause(['w31'],'-w32')
c42 = Clause(['w32'],'-w31')

clauses = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42]
propositions = ['s11', 's22', '-w12']
q = 'w31'
'''


# build your own pc
c1 = Clause(['a'], '-b')
c2 = Clause(['b'], '-a')
c3 = Clause(['c'], '-d')
c4 = Clause(['d'], '-c')
c5 = Clause(['e'], '-f')
c6 = Clause(['f'], '-e')
c7 = Clause(['j'], '-k')
c8 = Clause(['k'], '-j')
c9 = Clause(['g'], '-b')
c10 = Clause(['b'], 'h')
c11 = Clause(['a','d'], 'h')
c12 = Clause(['g'], 'i')
c13 = Clause(['f'], 'i')
c14 = Clause(['h','i'], 'k')
c15 = Clause(['d','f'], 'k')

clauses = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]


#propositions = ['b', 'j', 'g']
#q = 'g'


propositions = ['a', 'd', 'j']
q = 'f'


kb = KB(clauses, propositions)

print(forward_chaining(kb, q))
