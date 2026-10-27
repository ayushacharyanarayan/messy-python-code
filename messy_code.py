# BEFORE: messy version (hard to read, repeated logic, unclear names)
a=[["Amit",78,85,90],["Riya",92,88,95],["Karan",45,50,38],["Sneha",67,72,60]]
t=0
top=""
m=0
for i in a:
    n=i[0]
    s=i[1]+i[2]+i[3]
    av=s/3
    if av>=90:
        g="A"
    else:
        if av>=75:
            g="B"
        else:
            if av>=60:
                g="C"
            else:
                if av>=40:
                    g="D"
                else:
                    g="F"
    print("Name:",n,"Total:",s,"Average:",round(av,2),"Grade:",g)
    t=t+av
    if av>m:
        m=av
        top=n
print("Class average:",round(t/len(a),2))
print("Topper:",top,"with",round(m,2))
