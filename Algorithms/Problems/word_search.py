"""
Problem: Find word in grid
Can snake WASD, but not diagonal
"""

def main():
    # Problem: Find word in grid
    grid = [   ['a', 'v', 'l'],   ['p', 'e', 'a'],   ['y', 'e', 'p'],]  
    # Test cases
    # Match: ape, true
    # Not match: apple, false
    # Loop: apeva, false
    # Repeating: vee, true
    # Diagonal: ley, false

    # print("ape: ", find_word(grid, "ape"))
    # print("apple: ", find_word(grid, "apple"))
    print("apeva: ", find_word(grid, "apeva"))
    # print("vee: ", find_word(grid, "vee"))
    # print("ley: ", find_word(grid, "ley"))

def DFS(grid, target, start):    
    # init visited set & stack for DFS    
    visited = set()    
    stack = [start]

    while stack:        
        index, loc = stack.pop()        
        r, c = loc                

        # compare current char to target char        
        if grid[r][c] == target[index]: 
            # mark node as visited            
            visited.add((r,c))                    
            # If index is at end of target word, return true             
            if index == len(target)-1:              
                return True                        
            else: # else, continue matching remaining chars                
                # push unvisited neighbors to stack                
                for dr, dc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:                    
                    # Make sure neighbor is in grid                    
                    if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]):                         
                        # Make sure neighbor is not visited                         
                        if (dr, dc) not in visited:                            
                            stack.append([index+1, (dr, dc)])
    return False    

def find_word(grid, target): # O((N*M)^2)    
    # Find starting nodes (first char in target word)   
    N, M = len(grid), len(grid[0])     
       
    for r in range(N):         
        for c in range(M):            
            # Match first char to find starting node            
            if grid[r][c] == target[0]:                
                # If match, call DFS                
                start_node = [0, (r,c)] # Node info: [index, (row, col)]                
                if DFS(grid, target, start_node):                    
                    return True        
    return False

main()
