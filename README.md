# rolldice
A python script for "rolling" dice notation used in table-top RPGs and a script for modeling the results.

Many table-top role-playing games use the following notation to describe rolls that players make: 

`NdX`

Where N is the number of dice and X is the number of sides on each die.  

For example, damage from a rapier in D&D:

`1d6+DEX piercing damage`

or a quantity of treasure

`3d6*100 copper pieces`


rolldice is a program that interprets and emulates this notation, producing a quantity and identifier pair

modeldice is a program that interprets and models the notation, producing a probability distribution of the roll

## Supported Dice Notation
The 'd' in the dice notation is treated like an operator.  It means "roll a die with [number after the d] sides [number before the d] times and sum the result."

It is interpreted as an operator after the parentheses:
Parentheses, *Dice*, Exponents, Multiplication, Addition

It is important to note, though, that the order of operations on either side of the d is not assumed to be left-right.  
`2d4d6` is arbitrary, and will throw an error.  
`(2d4)d6` and `2d(4d6)` are both acceptable.  

The expression can use most mathematics that python normally supports:
`(-2d4+(7d8)**2)d10/5+2d6%2`

### Dropping Dice
In D&D 5e, Wizards of the Coast introduced an "advantage/disadvantage" system, which basically means you drop the lowest or the highest of 2d20.  Long before that, the standard way to produce a new heroic character's attribute scores was to roll 4d6 and drop the lowest for each attribute.  

In order to do that, use the `l` or `h` modifier to drop the lowest or highest:

`NdX<[l|h][M]`

where M is the number to drop from that end.  


Advantage: `2d20l1`

Disadvantage: `2d20h1'

Stat roll: `4d6l1 STR, 4d6l1 DEX, 4d6l1 CON, 4d6l1 INT, 4d6l1 WIS, 4d6l1 CHA`


## Modeling Dice
It is important to know that the dice model is an exhaustive, brute force method that does not work well for large numbers.  For example:

`modeldice 4d6l1` takes very little time to complete.  

`modeldice 3d100` takes a very long time to complete.

This is a bug and needs a better solution.

