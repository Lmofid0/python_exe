################################################## problem 1 #######################################################
nums = [2,7,11,15]
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
# print(Solution().twoSum(nums, 9)) 

############################################ problem 2 #######################################
# 👉 AJOUTEZ CES LIGNES AU DÉBUT DE VOTRE CODE 👈
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ENSUITE votre code (qui fonctionnera maintenant)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # ✅ Maintenant ça marche !
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10
        
        return dummy.next
# Pour tester
def create_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
result = Solution().addTwoNumbers(create_list([2,4,3]), create_list([5,6,4]))
print(list_to_array(result))  # [7,0,8]
# # Test
# l1 = create_list([4, 4, 8])
# l2 = create_list([5, 6, 4])
# result = Solution().addTwoNumbers(l1, l2)
# print(list_to_array(result))  # [7, 0, 8]

# def addTwoNumbers(self, l1, l2):
#     dummy = cur = ListNode(0)
#     carry = 0
#     while l1 or l2 or carry:
#         if l1:
#             carry += l1.val
#             l1 = l1.next
#         if l2:
#             carry += l2.val
#             l2 = l2.next
#         cur.next = ListNode(carry%10)
#         cur = cur.next
#         carry //= 10
#     return dummy.next
