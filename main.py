# python3

def parallel_processing(n, m, data):
    output = []
    x=0
    time=0
    while time<math.ceil(m/n):
        for i in range(n):
            if j>=m:
                break
            if time ==0:
                output.append((i,0))
            else:
                output.append((i,time+data[x-2]-1))
            x+=1
        time+=1
    return output



    return output



def main():
    line=list(map(int,input().split()))
    n = line[0]
    m = line[1]
    data=list(map(int,input().split()))
    

   
    result = parallel_processing(n,m,data)
    
    for i,j in result:
        print(i,j)



if __name__ == "__main__":
    main()
