⍝ Nice fucking comment
d←⊃,/⊃⎕nget 'input.txt' 1
+/×/¨⍎¨'(?<=mul\()\d+,\d+(?=\))'⎕S'&'⊢d
d←{2::⍵ ⋄ ⍎⍵}¨'(do\(\)|don''t\(\)|(?<=mul\()\d+,\d+(?=\)))'⎕S'&'⊢d

