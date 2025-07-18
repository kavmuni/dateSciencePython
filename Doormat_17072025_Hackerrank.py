def matDesign(m, n):
    #print("rows: ", m, " ~ Columns: ", n)
    welString = "-" * ((n-7)//2) + "WELCOME" + "-" * ((n-7)//2)
    #print(welString)
    if n > m:
        for rec in range(1,m):
            #print(rec, rec%2)
            if rec%2 != 0:
                v = int((n-(3*rec))//2)
                sp_ch = ".|." * (rec)
                #print(v, sp_ch)
                hyphen_ = ("-" * v).strip()
                finalres = hyphen_+ sp_ch + hyphen_
                print(finalres)
        print(welString)
        for rec in range(m).__reversed__():
            #print(rec, rec%2)
            if rec%2 != 0:
                v = int((n-(3*rec))//2)
                sp_ch = ".|." * (rec)
                #print(v, sp_ch)
                hyphen_ = ("-" * v).strip()
                finalres = hyphen_+ sp_ch + hyphen_
                print(finalres)
        return 1
    else:
        return -1
if __name__ == '__main__':
    m,n = map(int, input().split())
    matDesign(m, n)



"""
C:\Users\devis\anaconda3\python.exe C:\Users\devis\PycharmProjects\dateSciencePython\17072025_Hackerrank.py 
13 39
------------------.|.------------------
---------------.|..|..|.---------------
------------.|..|..|..|..|.------------
---------.|..|..|..|..|..|..|.---------
------.|..|..|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|..|..|.---
----------------WELCOME----------------
---.|..|..|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|..|..|.------
---------.|..|..|..|..|..|..|.---------
------------.|..|..|..|..|.------------
---------------.|..|..|.---------------
------------------.|.------------------

Process finished with exit code 0
"""
