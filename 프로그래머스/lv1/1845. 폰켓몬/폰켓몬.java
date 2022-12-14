import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> poketmonNums = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(poketmonNums.containsKey(nums[i])){
                poketmonNums.put(nums[i], poketmonNums.get(nums[i])+1);
            }
            else{
                poketmonNums.put(nums[i], 1);
            }
        }

        int answer = Math.min(poketmonNums.size(), nums.length/2);
        return answer;
    }
}