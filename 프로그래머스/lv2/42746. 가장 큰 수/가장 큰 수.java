import java.util.Arrays;

import java.util.Comparator;


class Solution {
    public String solution(int[] numbers) {
        String[] numbersString = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            numbersString[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(numbersString, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return (b+a).compareTo(a+b);
            }
        });

        StringBuilder answer = new StringBuilder();
        if(numbersString[0].equals("0")){
           answer = new StringBuilder("0"); 
        }
        else{
            for (String s : numbersString) {
                answer.append(s);
            }
        }
        return answer.toString();
    }
}