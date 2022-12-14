import java.util.Stack;

class Solution {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<number.length(); i++){
            Character currentCharacter = number.charAt(i);
            while(!stack.empty() && currentCharacter.compareTo(stack.peek())>0 && k-->0){
                stack.pop();
            }
            stack.push(currentCharacter);
        }
        
        while(k-->0){
            stack.pop();
        }
        
        StringBuilder answerStringBuilder = new StringBuilder();
        for (Character character : stack) {
            answerStringBuilder.append(character);
        }
        return answerStringBuilder.toString();
    }
}