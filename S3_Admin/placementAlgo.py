from createObject import getInput
import copy
import boto3

def resource_processor(operation, server_list, free_pack = None, min = None):
    if (operation == 'sum'):
        sums = []
        sums.append(sum([obj["cpu_usage"] for obj in server_list]))
        sums.append(sum([obj["memory_usage"] for obj in server_list]))
        return sums
    if (operation == 'vm_load'):
       
        return [server_list["cpu_usage"],server_list["memory_usage"]]
    if (operation == 'min_checker') :
        print(free_pack, server_list)
        diff = [(limit - allo) for (limit, allo) in zip(free_pack, server_list)]
        if sum(diff) < sum(min):
            return True
        else :
            return False
    if (operation == 'min_return'):
        diff = [(limit - allo) for (limit, allo) in zip(free_pack, server_list)]
        return diff
    if operation == 'allo_check' :
        for (vm_resource, free_resource) in zip(server_list, free_pack):
            if vm_resource > free_resource :
                return False
        return True
def check_violation(server_vm, c=[15, 15]):
    res_sum = resource_processor('sum', server_vm)
    for (vm_sum, capacity) in zip(res_sum, c):
        if (vm_sum > capacity):
            return True
    return False

def firstFit(popped_vm, n, c, new_allo):
    # res is number of servers
    no_exist_servers = len(new_allo)

    # Create an array to store the present allocation for next cycle
    #server_rem = new_allo.copy()
    server_rem=copy.copy(new_allo)

    # Place popped vms  
    for i in range(n):

        # Initialize minimum space left and index
        # of best bin
        min = [ele + 1 for ele in c]
        best_server_index = 0

        for j in range(no_exist_servers):
            free_pack = [(limit - allocated) for (limit, allocated) in zip(c, resource_processor('sum', server_rem[j][1]))]
            # print(free_pack)
            print(free_pack,resource_processor('vm_load' ,popped_vm[i]),resource_processor('allo_check' ,resource_processor('vm_load' ,popped_vm[i]), free_pack),resource_processor('min_checker', resource_processor('vm_load' ,popped_vm[i]), free_pack, min))
            if resource_processor('allo_check' ,resource_processor('vm_load' ,popped_vm[i]), free_pack) and resource_processor('min_checker', resource_processor('vm_load' ,popped_vm[i]), free_pack, min):
                best_server_index = j
                min = resource_processor('min_return',resource_processor('vm_load' ,popped_vm[i]), free_pack, min)
                #print('hi')

                # If no server could accommodate popped_vm[i],
        # create a new server
        if (sum(min) == (sum(c) + len(c))):
            server_rem.append([no_exist_servers + 1])
            server_rem[no_exist_servers].append([popped_vm[i]])
            no_exist_servers += 1
        else:  # Assign the vm to best server
            server_rem[best_server_index][1].append(popped_vm[i])
    return server_rem




def pop_vms(server_vm, c):
    index = dict()
    temp = []
    max_usage = 0
    for i in server_vm:
        #temp = server_vm.copy()
        temp=copy.copy(server_vm)
        temp.remove(i)
        usage = resource_processor("sum",temp)
        # print('sums:', usage)
        if not check_violation(temp,c) and sum(usage)>max_usage:
            index = i
            max_usage = sum(usage)
    # print(index)
    if not index :
        index = [0,0]
        max_usage = 0
        for i in server_vm:
            #temp = server_vm.copy()
            temp=copy.copy(server_vm)
            temp.remove(i)
            for j in temp :
                #temp_2 = temp.copy()
                temp_2=copy.copy(temp)
                temp_2.remove(j)
                usage = resource_processor("sum", temp_2)
                # print('sums for 2:', usage)
                if not check_violation(temp_2,c) and sum(usage) > max_usage:
                    index[0] = i
                    index[1] = j
                    max_usage  = sum(usage)
    if len(index) == 2:
        print(server_vm)
        server_vm.remove(index[0])
        server_vm.remove(index[1])
    else :
        server_vm.remove(index)
    return index, server_vm                  

       


def initialize_weights(input, c):
    popped_vm = []
    new_allo = []
    j = 0
    violation_check = []

    for i in input:
        new_allo.append([])
        new_allo[j].append(i[0])
        violation_check = check_violation(i[1], c)
        if violation_check:
            popped_ele, remaining = pop_vms(i[1], c)
            if type(popped_ele) != type({}):
                for vm in popped_ele:
                    popped_vm.append(vm)
            else :
                popped_vm.append(popped_ele)
            new_allo[j].append(remaining)
        else :
            new_allo[j].append(i[1])    
        j += 1
    return popped_vm, new_allo


def push():
        s3 = boto3.client('s3')
        s3.upload_file('vmServer_map.csv','myvmdata','vmServer_map.csv')

# Driver code 9,15  
def getBestFit():
    '''input = [[1, [{"vm_id": 101, "cpu_usage": 5, "memory_usage": 4},
                  {"vm_id": 102, "cpu_usage": 5, "memory_usage": 7},
                  {"vm_id": 103, "cpu_usage": 7, "memory_usage": 9}]], [2, [
        {"vm_id": 201, "cpu_usage": 4, "memory_usage": 8},
        {"vm_id": 202, "cpu_usage": 1, "memory_usage": 10},
        {"vm_id": 203, "cpu_usage": 3, "memory_usage": 9},
        {"vm_id": 204, "cpu_usage": 8, "memory_usage": 6}]], [3, [
        {"vm_id": 301, "cpu_usage": 4, "memory_usage": 1},
        {"vm_id": 302, "cpu_usage": 5, "memory_usage": 6},
        {"vm_id": 303, "cpu_usage": 7, "memory_usage": 7}]]]
    c = [15, 15]'''
    input=getInput()
    '''input=[[1, [{'cpu_usage': 83.0, 'vm_id': 1.0, 'memory_usage': 84.0}, {'cpu_usage': 85.0, 'vm_id': 2.0, 'memory_usage': 79.0}, {'cpu_usage': 82.0, 'vm_id': 3.0, 'memory_usage': 76.0}, {'cpu_usage': 83.0, 'vm_id': 4.0, 'memory_usage': 71.0}]]]'''

    #print("Printing intput")
    #print(input)
    c = [200, 200]

    # [resource_processor('sum',li[1]) for li in input]
    popped_vm, new_allo = initialize_weights(input, c)
    # print(popped_vm)
    # print(new_allo)
    n = len(popped_vm)
    print("Output")
    print(firstFit(popped_vm,n ,c, new_allo))
    return firstFit(popped_vm,n ,c, new_allo)
    #print("Number of bins required in First Fit : ", firstFit(popped_vm,n ,c, new_allo))
#print(getBestFit())
# This code is contributed by Rajput-Ji
