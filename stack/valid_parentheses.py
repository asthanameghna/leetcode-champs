class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_open = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:  
                if len(stack) == 0:  
                    return False

                last_ch = stack.pop()
                if closing_to_open[ch] != last_ch:
                    return False

        return len(stack) == 0
        

            
