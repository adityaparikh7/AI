/*List of diseases and their symptoms*/
disease(bronchitis,cough,sore_throat,headache,chest_pain).
disease(chronic_pancreatitis,abdominal_pain,nausea,vomiting,lack_of_appetite).
disease(tuberculosis,lack_of_appetite,fever,fatigue,night_sweats).
disease(chest_infection,cough,breathlessness,chest_pain,disorientation).
disease(tonsilitis,sore_throat,fever,cough,voice_change).

/*Treatment for the disease*/
treat(bronchitis,drink_fluids,avoid_smoking).
treat(chronic_pancreatitis,avoid_alcohol,diet_change).
treat(tuberculosis,antibiotics,neuropathy).
treat(chest_infection,reat,avoid_smoking).
treat(tonsilitis,antibiotics,surgery_in_extreme_cases).


/*Rules for diagnosis*/
diagnosis(X,A,B,C,D):-
disease(X,A,B,C,D);disease(X,A,C,B,D);disease(X,B,C,A,D);disease(X,B,A,C,D);
disease(X,C,A,B,D);disease(X,C,B,A,D).
start:-
writef("Please enter the symptoms:"),
read(A),nl,
read(B),nl,
read(C),nl,
read(D),nl,
diagnosis(X,A,B,C,D), 
writef("You have been diagnosed with %t. \n",[X]),nl,
writef("Treatment recommended:"),
treat(X,Y,Z),nl,
writef("%t",[Y]),nl,
writef("%t",[Z]),
fail.