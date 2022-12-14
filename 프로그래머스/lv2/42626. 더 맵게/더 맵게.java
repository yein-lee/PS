import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue();
        
        for (int aScoville : scoville) {
            heap.offer(aScoville);
        }
        
        while(heap.peek() < K){
            if(heap.size() < 2){
                answer = -1;
                break;
            }
            int lowestScoville = heap.poll();
            int secondLowestScoville = heap.poll();
            heap.offer(lowestScoville + secondLowestScoville*2);
            answer += 1;
        }

        return answer;
    }
}