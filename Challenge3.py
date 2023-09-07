# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".




# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
 

# Constraints:

# The given address is a valid IPv4 address.


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        result_address = ""
        
        for char in address:
            if char == ".":
                result_address += "[.]"
            else:
                result_address += char
        
        return result_address

solution = Solution()


address1 = "1.1.1.1"
address2 = "255.100.50.0"

afficher_address1 = solution.defangIPaddr(address1)
print(afficher_address1)

afficher_address2 = solution.defangIPaddr(address2)
print(afficher_address2)
