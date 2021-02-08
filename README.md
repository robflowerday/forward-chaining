# forward-chaining
This algorithm, takes in Horn Clauses in implication form and a proposition that you would like to determine as true of false:

e.g.
o: Alice is outside
r: It is raining
w: Alice is wet

-o: Alice is not outside
-r: It is not raining
-w: Alice is not wet

o and r implies w

would be written as [['o', 'r'], 'w']
