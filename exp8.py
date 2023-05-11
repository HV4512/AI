def unification(a,b):
    
    if len(a) != len(b):
        return "Unification Failed"
    elif(a[0] != b[0]):
        return "Unification Failed"
    else:
        result = str(a[0])+"["+str(a[1])
    
    for l in range(2,len(a)-1):
        
        if(a[l]==";" or a[l]==","):
            result+=", ("
            continue
        result += a[l]
        result += "/"
        result += b[l]
        result += ")"
    result+="]"
    print("Unification Success")
    return result

a = "p(x,y)"

b = "p(p,q)"

print(unification(a, b))