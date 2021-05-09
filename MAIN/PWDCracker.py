# Python Program, to search for the HASHes of the LEAKED PWDs (stored and provided in pwd_dump.txt), from a dummy file (pwdhash.txt) containing most used PWDs with their MD5 hashes.

P , Q = open ("pwd_dump.txt",'r') , open ("pwdhash.txt",'r')
PWD = j = []

# Making a LIST of PWDs that are meant to be analyzed!
for i in P:
    j=(i.split(':'))
    PWD.append(j[0])
    if '\n' in j[1]: PWD.append(j[1][:-1])
    else: PWD.append(j[1])

PWDCHECK = []

# Making a LIST of available PWDs with their MD5 HASHes!
for ii in Q:
    jj=(ii.strip().split(' '))
    PWDCHECK.append(jj[0])
    if '\n' in jj[-1]: PWDCHECK.append(jj[-1][:-1])
    else: PWDCHECK.append(jj[-1])

      
# ANALYZING PROCEDURE
print("              CRACKED PASSWORDS -- MD5              \n\n")
for p in range(1,len(PWD),1):
    if PWD[p] in PWDCHECK:
        print(PWD[p-1] + ":" + PWD[p] + " ---> " + PWDCHECK[(PWDCHECK.index(PWD[p]))-1])

P.close()
Q.close()
