import java.util.*;


class Solution {
    public int solution(String s) {
        Map<String, String> map = Map.of(
            "zero", "0",
            "one", "1",
            "two", "2",
            "three", "3",
            "four", "4",
            "five", "5",
            "six", "6",
            "seven", "7",
            "eight", "8",
            "nine", "9"
        );
        
        String answer = "";
        int i = 0;
        int j = 0;
        for(i=0; i<s.length(); i++){
            if(Character.isDigit(s.charAt(i))){
                answer += s.substring(i, i+1);
                continue;
            }
            for(j=i+1; j<=s.length(); j++){
                if(map.containsKey(s.substring(i, j))){
                    answer += map.get(s.substring(i, j));
                    break;
                }
            }
            i = j - 1;
        }
        
        return Integer.parseInt(answer);
    }
}