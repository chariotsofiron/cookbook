% FREQUENCY
% count occurrences of element E
count(_, [], 0).
count(E, [H|T], N0) :-
   (E=H -> C is 1; C is 0),
   count(E, T, N1),
   N0 is N1+C.

% COUNTDOWN
countDownR(N) :- N<0,!.
countDownR(N) :- writeln(N), 
    NN is N-1, 
    countDownR(NN).

% FACTORIAL
fact(0, 1).
fact(N, F) :-
    N > 0,
    N1 is N-1,
    fact(N1, F1),
    F is F1 * N.

% SQUARE ROOT
int(0).
int(N) :-
    int(N1),
    N is N1 + 1.
root(N,R) :-
    int(K),
    K*K > N, !,
    R is K-1.

% RANGE
range(Low, Low, _).
range(Out,Low,High) :-
    NewLow is Low+1,
    NewLow =< High,
    range(Out, NewLow, High).

% RANGE LIST
range(L) :-
    findall(N, between(1, 6, N), L).

% MAX OF TWO ELEMENTS
max(X, Y, X) :-
    X >= Y, !.
max(_, Y, Y).


% LIST MAP (add 1 to every element)
addUp(Xs, Ys) :- maplist(addUp2, Xs, Ys).
addUp2(X, Y) :- Y is X + 2.

% LIST SUM
list_sum([], 0).
list_sum([H|T], Sum) :-
   list_sum(T, Rest),
   Sum is H + Rest.


% LIST LAST ELEMENT
my_last(X,[X]) :- !.
my_last(X,[_|T]) :- my_last(X,T).

% LIST 2ND LAST ELEMENT
lst_but_one(X, [X,_]) :- !.
lst_but_one(X, [_|T]) :- lst_but_one(X,T).


% LIST NTH ELEMENT
element_at(X,[X|_], 1) :- !.
element_at(X,[_|T], N) :-
        M is N - 1,
        element_at(X, T, M).

% LIST LENGTH
my_length(1, [_]) :- !.
my_length(X, [_|T]) :-
        my_length(Y,T),
        X is Y+1.

% LIST REVERSE
reverse(L, R) :- reverse(L,[],R).
reverse([H],L,[H|L]) :- !.
reverse([X|T],L,R) :- reverse(T,[X|L],R).

% LIST REVERSE 2
reverse([],[]).
reverse([H|T], L2) :-
    reverse(T, L3),
    append(L3, [H], L2).



% LIST FLATTEN
my_flatten([H], X) :-
        is_list(H),
        my_flatten(H,X).
my_flatten([H], [H]).
my_flatten([H|T], X) :-
        is_list(H),
        my_flatten(H, Y),
        my_flatten(T, Z),
        append(Y,Z,X).
my_flatten([H|T], [H|X]) :- my_flatten(T,X).


% IS PALINDROME
palindrome(L) :- reverse(L,L).


% LIST REMOVE CONSECUTIVE DUPLICATES
compress([H], [H]).
compress([H,H|T], X) :- compress([H|T],X).
compress([H|T], [H|X]) :- compress(T, X).


% 1.09 Pack consecutive duplicates of list elements into sublists.
pack([], []).
pack([H,H|T], X) :- pack([[H,H]|T],X).
pack([[H|Hs]|[H|T]], X) :- pack([[H,H|Hs]|T], X).
pack([H|T], [[H]|X]) :-
        not(is_list(H)),
        pack(T,X).
pack([H|T], [H|X]) :- pack(T,X).

% 1.10 Run-length encoding of a list.
encode([], []) :- !.
encode(L, [[N,X]|Y]) :-
        pack(L,[[X|Xs]|T]),
        length([X|Xs],N),
        !,encode(T, Y).


% LIST SLICE
slice([H|_], 1, 1, [H]).
slice([H|T], 1, To, [H|X]) :-
        N is To - 1,
        slice(T, 1, N, X).
slice([_|T], From, To, L) :-
        N is From - 1,
        M is To - 1,
        slice(T, N, M, L).


% LIST PERMUTATIONS
permutations([], []).
permutations([X|Xs], Ys) :-
    permutations(Xs, Zs),
    insert(X, Zs, Ys).

insert(X, Xs, [X|Xs]).
insert(X, [Y|Ys], [Y|Zs]) :-
    insert(X, Ys, Zs).



% LIST REMOVE DUPLICATES
unique([],[]).
unique([H | T], List) :-    
    member(H, T),
    unique( T, List), !.
unique([H | T], [H|T1]) :- 
    \+member(H, T),
    unique( T, T1), !.


% LIST NESTED FLIP
flippers([],[]).
flippers([(E1, E2)|T], [(E2, E1)| T2]):- flippers(T,T2).