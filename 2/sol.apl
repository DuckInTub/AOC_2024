f←{∧/2 ⍺⍺/⍵}      ⍝ Used to check inc.. or dec..
diff←{~∨/3<|2-/⍵} ⍝ Check that diff is max 3
safe←diff∧(>f∨<f)
+/safe¨d←⍎¨⊃⎕NGET 'input.txt' 1 ⍝ Part 1

⍝ Negate an identity matrix and
⍝ use each row as a mask for the rows
⍝ in the input data. This checks
⍝ if the row is safe after removing
⍝ any one of the elements.
safe2←{∨/safe¨(/∘⍵)¨↓~(,⍨⍴1↑⍨1∘+)≢⍵}
+/safe2¨d ⍝ Part 2
