class py_solution:
	   def is_valid_parenthese(self, str1):
	        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
	        for parenthese in str1:
	            if parenthese in pchar:
	                stack.append(parenthese)
	            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
	                return False
	        return len(stack) == 0
for i in range(0,4):
     string =input("enter parnethesis:") 	
     print(py_solution().is_valid_parenthese(string))
