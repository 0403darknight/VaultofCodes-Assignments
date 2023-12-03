while True:
    try:
        bg = float(input("Enter your budget:"))
        s = bg
    except ValueError:
        print("Print number as a amount")
        continue
    else:
        break
a ={"name":[], "quant":[], "price":[]}
b = list(a.values())
na = b[0]
qu = b[1]
pr = b[2]
while True:
    try:
        ch = int(input("1.ADD\n2.EXIT\n ENTER your choice:"))
    except ValueError:
        print("\nError: Choose only the given option")
        continue
    else:
        if ch == 1 and s>0:
            pn = input("Enter product name : ")
            q = input("Enter the quantity :")
            p = float(input("Enter the price of the product :"))
            if p>s:
                print("\n Can't buy the product")
                continue
            else:
                if pn in na:
                    ind = na.index(pn)
                    qu.remove(qu[ind])
                    pr.remove(pr[ind])
                    qu.insert(ind, q)
                    pr.insert(ind, p)
                    s = bg-sum(pr)
                    print("\n Amount left :",s)
                else:
                    na.append(pn)
                    qu.append(q)
                    pr.append(p)
                    s = bg-sum(pr)
                    print("\n Amount left :", s)
        elif s<= 0:
            print("\n No Budget")
        else:
            break
print("\n Amount left: RS.",s)
if s in pr:
    print("\n Amount left can buy you a", na[pr.index(s)])
print("\n\n\n\nGROCERY LIST")
for i in range(len(na)):
    print(na[i], qu[i], pr[i])
