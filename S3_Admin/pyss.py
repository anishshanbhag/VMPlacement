# Python3 program to find number of bins required using 
# First Fit algorithm. 

# Returns number of bins required using first fit 
# online algorithm 
def firstFit(weight, n, c, new_allo): 
        
        # res is number of servers
        res = len(new_allo)

        # Create an array to store the present allocation for next cycle
        bin_rem = new_allo 

        # Place popped vms  
        for i in range(n): 
            
            
            j = 0
            
            # Initialize minimum space left and index 
            # of best bin 
            min = c + 1 
            bi = 0

            for j in range(res): 
                temp = c - sum(bin_rem[j][1])
                if (  temp >= weight[i] and temp - weight[i] < min): 
                    bi = j 
                    min = temp - weight[i] 
                    
        # If no server could accommodate weight[i], 
        # create a new server
            if (min == c + 1):
                bin_rem.append([res+1])
                bin_rem[res].append([weight[i]]) 
                res += 1
            else: # Assign the vm to best server 
                bin_rem[bi][1].append(weight[i]) 
        return bin_rem 

def initialize_weights(input, c):
    popped_vm = []
    new_allo = []
    j=0
    for i in input:
        new_allo.append([])
        new_allo[j].append(i[0])
        if sum(i[1]) > c:
            popped_vm.append(min(i[1]))
            i[1].remove(min(i[1]))
        new_allo[j].append(i[1])
        j += 1    
    return popped_vm, new_allo        


# Driver code 
if __name__ == '__main__': 
        input = [[1, [1,5,7]], [2, [4,1,3,8]], [3, [2,5,7]]]
        c = 15
        weight, new_allo = initialize_weights(input, c) 
        # print(weight, new_allo)
        n = len(weight); 
        print("Number of bins required in First Fit : ", firstFit(weight,n ,c, new_allo))
	
# This code is contributed by Rajput-Ji 
