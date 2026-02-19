import java.util.*;

public class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < asteroids.length; i++) {
            int curr = asteroids[i];

            
            if (curr < 0) {
                boolean destroyed = false;

                
                while (!stack.isEmpty() && stack.peek() > 0) {
                    int prev = stack.peek();

                    if (prev < -curr) {
                       
                        stack.pop();
                    } else if (prev == -curr) {
                    
                        stack.pop();
                        destroyed = true;
                        break;
                    } else {
                       
                        destroyed = true;
                        break;
                    }
                }

                if (!destroyed) {
                    stack.push(curr);
                }
            } else {
                
                stack.push(curr);
            }
        }

        
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }
}