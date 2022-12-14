import java.util.*;

class Solution {
    ArrayList<Integer> permutedNums = new ArrayList<>();

    public void permutation(String[] arr, String[] out, boolean[] visited, int depth, int r){
        if(depth == r){
            StringBuilder numConcatStringBuilder = new StringBuilder();
            for(String num: out) {
                numConcatStringBuilder.append(num);
            }
            int numInt = Integer.parseInt(numConcatStringBuilder.toString());
            if(!permutedNums.contains(numInt)){
                permutedNums.add(numInt);
            }
            return;
        }
        for(int i=0; i<arr.length; i++){
            if(!visited[i]){
                visited[i] = true;
                out[depth] = arr[i];
                permutation(arr, out, visited, depth+1, r);
                visited[i] = false;
            }
        }
    }

    public boolean isPrimeNumber(int n){
        if(n==0){
            return false;
        }
        else if(n==1){
            return false;
        }
        else{
            for(int i=2; i<=Math.sqrt(n); i++){
                if(n%i==0){
                    return false;
                }
            }
        }
        return true;
    }

    public int solution(String numbers) {
        String [] numberStringArray = numbers.split("");

        for(int i=1; i<=numberStringArray.length; i++){
            permutation(numberStringArray, new String[i], new boolean[numberStringArray.length], 0, i);
        }


        int answer = 0;
        for(int num : permutedNums){
            if(isPrimeNumber(num)){
                answer ++;
            }
        }
        return answer;
    }
}