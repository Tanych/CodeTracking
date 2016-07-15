/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        // Write your code here
        ArrayList<Integer> nums=new ArrayList<Integer>();
        
        while(head!=null){
            nums.add(head.val);
            head=head.next;
        }
        
        int size=nums.size();
        
        if(nums==null || size==1)
            return true;
        else {
            int left = 0;
            int right = size - 1;
            while(left < right) {
                if(nums.get(left) != nums.get(right)) 
                {
                    System.out.print(nums.get(left)+";"+nums.get(right));
                    return false;
                }
                left++;
                right--;
            } 
            return true;
        }
        
       
            
    }
}