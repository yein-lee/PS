import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        Deque<Integer> peopleDeque = new ArrayDeque<Integer>();
        for(int weight: people){
            peopleDeque.add(weight);
        }

        int answer = 0;
        while(!peopleDeque.isEmpty()){
            if(peopleDeque.size()>1){
                if(peopleDeque.peekFirst() + peopleDeque.peekLast() <= limit){
                    peopleDeque.pollFirst();
                    peopleDeque.pollLast();
                    answer ++;
                }
                else{
                    peopleDeque.pollLast();
                    answer ++;
                }
            }
            else{
                peopleDeque.pollLast();
                answer ++;
            }
        }
        return answer;
    }
}