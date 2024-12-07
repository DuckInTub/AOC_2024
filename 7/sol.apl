⍝ Day 7
⎕PP←32
d←{⍎¨'\d+'⎕S'&'⊢⍵}¨⊃⎕nget 'test.txt' 1

evaluate←{⍎⍕⌽¯1↓,⍵,⍥⍪0,⍨⍺}
combs←{,⍵ ∘.⍺⍺⍣(⍺-1)⊢ ⍵}
⍝ Part 1
+/{T r←(⊃⍵)(1↓⍵)⋄T∊evaluate∘r¨(¯1+≢r) ,combs '+×':T ⋄ 0}¨d

