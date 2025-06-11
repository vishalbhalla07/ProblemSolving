class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [4 2 -1 -2 4 -5 5]
        # [4 3 -6 ]
        
        stack = []
        if not asteroids:
            return None

        stack.append(asteroids[0])
        # add the next element
        # a for loop to keep getting the next element 
        for i in range(1,len(asteroids)):
            new_asteroid = asteroids[i]

            # check if it is left or right
            # if right:
                # add to stack and continue
            if new_asteroid > 0:
                stack.append(new_asteroid)
            # elif new_asteroid is going left 
            else:
                if stack and stack[-1]<0:
                    stack.append(new_asteroid)
                else:
                    while stack and stack[-1]>0 and abs(stack[-1])<abs(new_asteroid):
                        stack.pop() #[ 4 -6 ]
                        continue
                    if not stack:
                        stack.append(new_asteroid)
                    else:
                        top_asteroid = stack[-1]
                        # add the asteroid also if runs out of space
                        if top_asteroid <0 :
                            stack.append(new_asteroid)
                        elif abs(top_asteroid) == abs(new_asteroid): 
                            # top_asteroid == new_asteroid:
                            stack.pop()

        return stack

            # i run out of stack and need to add this, or break and continue the for loop 

            # if stack exists and top is stack going right

                # if it is, check if value at top of stack is < new asteroid
                    # stack.pop()  
                    # continue the while process 
                # elif equal 
                    # stack.pop()
                    # break
                # else
                    # if the right element is larger, new_asteroid will just break
                    # break
            # else if the top is going left, then simply add to the stack since no collision would happen
        
