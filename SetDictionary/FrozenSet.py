fvr_sub = ["OS", "DBMS", "ALGO"]
print(fvr_sub)
#  frozenset will make list immutable
# order may not be preserved
fvr_sub = frozenset(fvr_sub)
print(fvr_sub)
fvr_sub[1] = "networking"

print(fvr_sub)