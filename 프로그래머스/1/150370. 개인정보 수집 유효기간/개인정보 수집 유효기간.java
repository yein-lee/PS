import java.time.LocalDate;
import java.util.HashMap;
import java.util.ArrayList;


class Solution {
    private int getDate(String date){
        String[] parts = date.split("\\.");
        int year = Integer.parseInt(parts[0]);
        int month = Integer.parseInt(parts[1]);
        int day = Integer.parseInt(parts[2]);
        return year * 12 * 28 + month * 28 + day;
    }
    
    public int[] solution(String today, String[] terms, String[] privacies) {
        int todayDate = getDate(today);
        
        HashMap<String, Integer> termMap = new HashMap<>();
        for(String term: terms){
            String[] parts = term.split(" ");
            termMap.put(parts[0], Integer.parseInt(parts[1]));
        }
        
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i < privacies.length; i++){
            String[] parts = privacies[i].split(" ");
            
            if(getDate(parts[0]) + termMap.get(parts[1]) * 28 - 1 < todayDate){
                answer.add(i+1);
            }
        }

        return answer.stream().mapToInt(integer -> integer).toArray();
    }
}