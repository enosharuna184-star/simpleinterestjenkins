def simInt(principal, interest, time):
    return (principal*interest*time)/100

if __name__ == "__main__":
    p = int(input("Enter principal amount"))
    i = int(input("Enter interest"))
    t = int(input("Enter time"))

    print("Simple interest: ", simInt(p,i,t))