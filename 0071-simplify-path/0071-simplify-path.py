class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the string by "/" and store in components
        components = path.split("/")
        # Stack to keep track of the elements
        stack = []

        # iterate over the components
        for comp in components:
            # if empty or "." then it can be ignored
            if comp == "" or comp == ".":
                continue
            # If ".." then we need to take out the prev component
            if comp == "..":
                if stack: stack.pop()
            # Else add the component to the top of the stack
            else:
                stack.append(comp)

        # return the stack by seperating it with "/"
        return "/" + "/".join(stack) 
