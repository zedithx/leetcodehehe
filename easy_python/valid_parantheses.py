class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        I definitely want to use stack here. When I meet an open paranthesis, I will append to the stack.
        When i meet a close paranthesis I will pop from the stack. If the stack is empty at the end,
        then I return True, else return false
        """
        # Define a dictionary of possible paranthesis matching open to close
        paran_dict = {'[': ']', '{': '}', '(': ')'}
        # Define stack
        paran_storage = []
        for char in s:
            if char in paran_dict.keys():
                paran_storage.append(char)
            else:
                if paran_storage:
                    if char == paran_dict[paran_storage.pop()]:
                        pass
                    else:
                        return False
                else:
                    return False
        if not paran_storage:
            return True


print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))