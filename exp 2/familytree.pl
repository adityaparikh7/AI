% grandparents
parent(prakash, purvi).
parent(neela, purvi).
parent(prakash, deepa).
parent(neela, deepa).
parent(harendra, sandeep).
parent(bharti, sandeep).
parent(harendra, sanjay).
parent(bharti, sanjay).
parent(harendra, harrick).
parent(bharti, harrick).

% parents
parent(purvi, aditya).
parent(sandeep, aditya).

% siblings 
sibling(sandeep, sanjay).
sibling(sandeep, harrick).
sibling(sanjay, sandeep).
sibling(sanjay, harrick).
sibling(harrick, sandeep).
sibling(harrick, sanjay).
sibling(purvi, deepa).
sibling(deepa, purvi).

% spouse
husband(harendra, bharti).
husband(prakash, neela).
husband(sandeep, purvi).
wife(bharti, harendra).
wife(neela, prakash).
wife(purvi, sandeep).

% gender
male(harendra).
male(prakash).
male(sandeep).
male(sanjay).
male(harrick).
male(aditya).

female(bharti).
female(neela).
female(purvi).
female(deepa).

% rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
child(X, Y) :- parent(Y, X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandchild(X, Z) :- parent(Y, X), parent(Z, Y).
uncle(X, Y) :- male(X), parent(Z, Y), sibling(X, Z).
aunt(X, Y) :- female(X), parent(Z, Y), sibling(X, Z).
sister(X, Y) :- female(X), sibling(X, Y).
brother(Y, X) :- male(Y), sibling(X, Y).


/** <examples>
?- aunt(X, aditya).
?- uncle(X, aditya).
?- grandparent(X, aditya).
?- child(sandeep, X).
?- father(sandeep, X).
?- mother(purvi, X).
?- spouse(sandeep, X).
?- grandchild(aditya, X).
?- brother(sandeep, X).
?- sister(deepa, Y).
*/