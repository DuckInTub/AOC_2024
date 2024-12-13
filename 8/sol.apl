⍝ Day 8 APL
syms←1↓∪∊m←↑⊃⎕nget 'test.txt' 1
locs←{⍸⍵=m}¨syms
H W←⍴m
in_bound←{∧/(H∘≥∧0∘<)⍵}

]dinput
calc←{
    r1 c1 r2 c2←⍵
    dr dc←(r1-r2)(c1-c2)
    a1←(r2-dr)(c2-dc)
    a2←(r1+dr)(c1+dc)
    ret←a1 a2
    ret/⍨in_bound¨ret
 }

≢∪↓{(2÷⍨≢⍵)2⍴⍵}∊{calc¨,∘.,⍨⍸m=⍵}¨syms
