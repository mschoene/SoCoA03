ldc R0 1
ldc R1 3
loop:
prr R1
sub R1 R0
bne R1 @loop
hlt
