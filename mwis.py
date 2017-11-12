

# Raj Pokhrel
# CMPSC 465

#main function
# n is the number of vertices
# weights is a list of their weights, v_1, ..., v_n


def mwis (n, weights):
    #
    #FILL IN CODE HERE

    weights = [0] + weights
    opt = [0, weights[1]]  # Declare a array to hold that holds the optimial solution
    sol_items = []         # Array that will hold the white-space delimited integers, sorted in increasing order

    for i in range(2,n+1):  # Use a for loop to calculate the best optimial solution
        opt.append(max(opt[i - 1], opt[i - 2] + weights[i] )) 
      # OPT(i) = max( v_i + OPT(i - 2), OPT(i- 1) )

    sol_tot_weight = opt[n] # Store the best optimial to total weight

    i = n
    while i > 1:    # Used while loop to find the white-space delimited integers
        if opt[i - 2] + weights[i] > opt[i - 1]:
            sol_items.append(i-1)
            i -= 2

            if i == 1:
                sol_items.append(i-1)
                break
        else:
            i -= 1

    opt.pop(0) # Remove the first element from the array
    return (opt, sol_tot_weight, sorted(sol_items)) # return the optimal solution

#Read input
f = open("input.txt", "r")
weights = [int(x) for x in f.readline().split()]
n = len (weights)

#call mwis
(opt, sol_tot_weight, sol_items) = mwis(n, weights)

#output solution
print ' '.join(map(str, opt))
print sol_tot_weight
print ' '.join(map(str, sol_items))
