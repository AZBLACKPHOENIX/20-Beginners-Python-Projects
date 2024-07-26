#cols
for i in range(13):
    #rows
    for j in range(13):
     #print the table
        print(f"{i*j:4d}", end=" ")
    #add a new line completing the inner loop
    print()