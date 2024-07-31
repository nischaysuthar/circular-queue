front=-1
rear=-1
max=3
q=[None]*max

while True:
    print("\nQueue operations")
    print("1.Enqueue")
    print("2.denqueue")
    print("3.display")
    print("4.exit")
    c=int(input("Enter choice:"))
    
    if c==1:
        if (rear+1)%max==front:
            print("Queue overflow")
        else:
            e=int(input("Enter element:"))
            if front==-1:
                front=0
            rear=(rear+1)%max
            q[rear]=e
            print("Element enqueued:",e)
            
    elif c==2:
        if front==-1:
            print("Queue underflow")
        else:
            print("Element removed:",q[front])
            if front==rear:
                front=rear=-1
            else:
                front=(front+1)%max
    
    elif c==3:
        if front==-1:
            print("Queue is empty")
        else:
            i=front
            while True:
                print(q[i],end=" ")
                if i==rear:
                    break
                i=(i+1)%max

    
    elif c==4:
        print("Exiting")
        break
    else:
        print("Invalid choice")   
    

                              