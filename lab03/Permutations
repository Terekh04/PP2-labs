def generate_permutations(string, step=0):
    if string==string[::-1]:
        print(string)
        return 
    if step == len(string):
        print("".join(string))  
        return
    
    for i in range(step, len(string)):
        s_list = list(string)  
        s_list[step], s_list[i] = s_list[i], s_list[step]  
        generate_permutations(s_list, step + 1)  

