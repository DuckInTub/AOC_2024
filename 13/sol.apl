⍝ Day 13
P←⍎¨¨('\d+'⎕S'&')¨({''∘≢¨⍵}⊆⊢)⊃⎕nget 'input.txt' 1

round←⌊0.5+⊢
whole←{0.01>|⍵-round ⍵}

solve←{
    ax ay bx by X Y←⍵
    nrB←(Y-X×ay÷ax)÷(by-bx×ay÷ax)
    nrA←(X-nrB×bx)÷ax
    nrA nrB
}

⎕PP←32
⍝ Part 1
⎕←+/3 1×+⌿↑t/⍨∧/⍤whole¨t←solve¨P
p2N←0 0 0 0 10000000000000 10000000000000
⍝ Part 2
⎕←+/3 1×+⌿↑t/⍨∧/⍤whole¨t←solve¨p2N∘+¨P

