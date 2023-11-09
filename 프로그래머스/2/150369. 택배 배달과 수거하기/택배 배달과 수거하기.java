class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        int deliveryAmount = 0;
        int pickUpAmount = 0;
        
        for(int i = n - 1; i >= 0; i--){
            deliveryAmount += deliveries[i];
            pickUpAmount += pickups[i];
            
            while(deliveryAmount > 0 || pickUpAmount > 0){
                deliveryAmount -= cap;
                pickUpAmount -= cap;
                answer += (i + 1) * 2;
            }
        }
        return answer;
    }
}