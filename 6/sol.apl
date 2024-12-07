⍝ Day 6
O←(+/1 0J1×⊢)¨⍸'#'=m←↑⊃⎕nget 'input.txt' 1
S←+/1 0J1×⊃⍸'^'=m
F←¯1J0
shp←⍴m

]dinput
step←{ ⍝ Makes one guard step, returns (F)acing (A)t
     O←⍺
     A F←⍵
     trn←0J¯1∘×
     O∊⍨⊂A+F: F,⍥⊂⍨A+F←trn⍣{~O∊⍨A+⍺}⊢F ⍝ Turn until no obstacle
     F,⍥⊂⍨A+F
 }

⍝ Take steps until outside grid
⍝ Keep track of pairs of (location, facing) 
went←O{⍵,⍨⊂⍺ step ⊃⍵}⍣{(t∊⍨⊃shp)∨0∊t←9 11○⊃⊃⍺}⊢⊂S F
⍝ Grab out all unique locations minus outside location
≢loc←∪⊃¨went ⍝ Part 1

sim←{⍵,⍨⊂⍺ step ⊃⍵}⍣{((⊂⊃⍺)∊1↓⍺)∨(t∊⍨⊃shp)∨0∊t←9 11○⊃⊃⍺}
+/{(1↓d)∊⍨⊂⊃d←(⊂S F) sim⍨ O,⊂⍵}¨loc
