import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public String minRemoveToMakeValid(String s) {
        Set<Integer> invalidIndices = new HashSet<>();
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();  
                } else {
                    invalidIndices.add(i);  
                }
            }
           
        }

    
        invalidIndices.addAll(stack);

       
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!invalidIndices.contains(i)) {
                sb.append(s.charAt(i));
            }
        }

        return sb.toString();
    }

    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minRemoveToMakeValid("lee(t(c)o)de)")); 
        System.out.println(sol.minRemoveToMakeValid("a)b(c)d"));      
        System.out.println(sol.minRemoveToMakeValid("))(("));         
    }
}