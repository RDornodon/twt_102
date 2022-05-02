def T(B,P=88,Q=6):
 def S(l,c):A=[[*b]for b in B];A[l][c]=P;return A
 def W(B):C=[*map(list,zip(*B[::-1]))];return[P]*3in[sum(B,[])[::4],sum(C,[])[::4]]+B+C
 F=[(l,c)for l in(0,1,2)for c in(0,1,2)if 64>B[l][c]]
 if[]==F or Q<1:return 68
 N=[S(*L)for L in F]
 if any(map(W,N)):return P
 M=[T(b,b'XO'[P==88],Q-1)for b in N]
 if P in M:return P
 if 68 in M:return 68
 return b'XO'[P==88]
for I in[I:=input]*int(I()):print(chr(68if{*sum(A:=[[*map(ord,l)]for l in(I(),I(),I())],[])}=={35}else T(A)))