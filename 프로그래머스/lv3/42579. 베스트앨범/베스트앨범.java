import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;


class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> genreTotalCountMap = new HashMap<>();
        for(int i=0; i<genres.length; i++){
            genreTotalCountMap.put(genres[i], genreTotalCountMap.getOrDefault(genres[i], 0) + plays[i]);
        }

        HashMap<String, HashMap<Integer, Integer>> genreMusicsMap = new HashMap<>();
        for(int i=0; i<genres.length; i++){
            genreTotalCountMap.put(genres[i], genreTotalCountMap.getOrDefault(genres[i], 0));
            if(genreMusicsMap.containsKey(genres[i])){
                genreMusicsMap.get(genres[i]).put(i, plays[i]);
            }
            else{
                HashMap<Integer, Integer> map = new HashMap();
                map.put(i, plays[i]);
                genreMusicsMap.put(genres[i], map);
            }
        }

        ArrayList<Integer> answerList = new ArrayList<>();
        List<Entry<String, Integer>> list = new ArrayList<>(genreTotalCountMap.entrySet());
        list.sort(Entry.<String, Integer>comparingByValue().reversed());
        for (Entry<String, Integer> entry : list) {
            String genre = entry.getKey();
            HashMap<Integer, Integer> numPlaysMap = genreMusicsMap.get(genre);
            List<Entry<Integer, Integer>> numPlayList = new ArrayList<>(numPlaysMap.entrySet());
            numPlayList.sort(Entry.<Integer, Integer>comparingByValue().reversed().thenComparing(Entry.comparingByKey()));
            for (int j = 0; j < Math.min(numPlayList.size(), 2); j++) {
                answerList.add(numPlayList.get(j).getKey());
            }
        }

        int[] answer = new int[answerList.size()];
        for(int i=0; i<answerList.size(); i++){
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}