ldc R0 0
ldc R1 09
ldr R1 R2
loop:
cpy R2 R0
sub R1 R0
str R2 R3
beq R1 @loop
prm R3
hlt

