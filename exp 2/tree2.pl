male(tukaram).
male(vasant).
male(nitin).
male(yogesh).
male(vikrant).
male(mahendra).
male(harsh).
male(jatin).

female(tarabai).
female(vanadana).
female(devyani).
female(varsha).
female(kirti).
female(sangita).
female(rahi).
female(tanaya).
female(disha).
female(siya).
female(purva).

parent(tukaram, nitin).
parent(tarabai, nitin).
parent(tukaram, devyani).
parent(tarabai, devyani).
parent(vasant, varsha).
parent(vandana, varsha).
parent(vasant, mahendra).
parent(vandana, mahendra).
parent(vasant, kirti).
parent(vandana, kirti).
parent(yogesh, harsh).
parent(devyani, harsh).
parent(nitin, rahi).
parent(varsha, rahi).
parent(vikrant, tanaya).
parent(kirti, tanaya).
parent(mahendra, disha).
parent(sangita, disha).
parent(nitin, siya).
parent(varsha, siya).
parent(vikrant, jatin).
parent(kirti, jatin).
parent(mahendra, purva).
parent(sangita, purva).

husband(tukaram, tarabai).
husband(vasant, vandana).
husband(nitin, varsha).
husband(yogesh, devyani).
husband(mahendra, sangita).
husband(vikrant, kirti).

wife(tarabai, tukaram).
wife(vandana, vasant).
wife(varsha, nitin).
wife(devyani, yogesh).
wife(sangita, mahendra).
wife(kirti, vikrant).




mother(X, Y) :- parent(X, Y),female(X).
father(X, Y) :- parent(X, Y),male(X).
sibling(X, Y) :- father(Z, X), father(Z, Y), mother(W, X), mother(W, Y), X\==Y.
sister(X, Y) :- female(X), sibling(X, Y).
brother(Y, X) :- male(Y), sibling(X, Y).
spouse(X, Y) :- husband(X,Y) ; wife(X,Y).
grandparent(Z, X) :- parent(Z, W), parent(W, X).
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W).
cousin_brother(X, Y) :- male(X), cousin(X, Y).
cousin_sister(X, Y) :- female(X), cousin(X, Y).
uncle(X, Y) :- male(X), parent(Z, Y), sibling(X, Z).
aunt(X, Y) :- female(X), parent(Z, Y), sibling(X, Z).
