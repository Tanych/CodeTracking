class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for index in range(len(s)):
            if s[index] == '(' or s[index] == '[' or s[index] == '{':
                stack.append(s[index])
            if s[index] == ')':
                if not stack or stack.pop()!='(':
                    return False
            if s[index] == ']':
                if not stack  or stack.pop()!='[':
                    return False
            if s[index] == '}':
                if not stack  or stack.pop()!='{':
                    return False
                    
        return False if stack else True