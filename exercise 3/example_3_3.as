# Count up to 3.
# - R0: loop index.
# - R1: loop limit.
# - R2: array index.
# - R3: temporary.
ldc R0 5
ldc R1 10
ldc R2 @array
loop:
str R0 R2
ldc R3 1
add R0 R3
add R2 R3
cpy R3 R1
sub R3 R0
bne R3 @loop
ldc R0 5
dec R2
reverse:
str R0 R2
ldc R3 1
add R0 R3
sub R2 R3
cpy R3 R1
sub R3 R0
bne R3 @reverse
hlt
.data
array: 10