⍝ Day 7
⎕PP←32
d←{⍎¨'\d+'⎕S'&'⊢⍵}¨⊃⎕nget 'test.txt' 1

evaluate←{⍎⍕¯1↓,⍵,' ',⍪0,⍨⍺}
combs←{,⍵ ∘.⍺⍺⍣(⍺-1)⊢ ⍵}


∇ r←can line;op_combs
 T r←(⊃line)(1↓line)
 op_combs←(¯2+≢line),combs'+×'
 :For comb :In op_combs
     :If T=comb evaluate r
         r←1
         :Return
     :EndIf
 :EndFor
∇ r←0

⍝ Part 1
+/{T r←(⊃⍵)(1↓⍵) ⋄ T∊evaluate∘r¨(¯2+≢⍵),combs '+×':T ⋄ 0}¨d


