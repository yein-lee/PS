import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.PriorityQueue;


class Edge implements Comparable<Edge> {

    private int vertex1;
    private int vertex2;
    private int weight;

    public Edge(int [] cost) {
        this.vertex1 = cost[0];
        this.vertex2 = cost[1];
        this.weight = cost[2];
    }

    public int getVertex1(){
        return this.vertex1;
    }

    public int getVertex2(){
        return this.vertex2;
    }

    public int getWeight(){
        return this.weight;
    }

    @Override
    public int compareTo(Edge edge) {
        if (this.weight > edge.getWeight())
            return 1;
        else if (this.weight < edge.getWeight())
            return -1;
        return 0;
    }
}

class Solution {
    public int solution(int n, int[][] costs) {
        List<Edge> edgesElse = new ArrayList<>();
        for(int [] cost: costs){
            edgesElse.add(new Edge(cost));
        }
        PriorityQueue<Edge> edgesCandidate = new PriorityQueue<>();

        List<Integer> visited = new ArrayList<>();
        visited.add(costs[0][0]);

        for (Iterator<Edge> iterator = edgesElse.iterator(); iterator.hasNext();) {
            Edge edge = iterator.next();
            if(edge.getVertex1()==costs[0][0] || edge.getVertex2()==costs[0][0]){
                edgesCandidate.add(edge);
                iterator.remove();
            }
        }

        int answer = 0;
        while(visited.size()<n){
            Edge edgeCandidate = edgesCandidate.remove();
            if(visited.contains(edgeCandidate.getVertex1()) && !visited.contains(edgeCandidate.getVertex2())){
                visited.add(edgeCandidate.getVertex2());
                answer += edgeCandidate.getWeight();
                for (Iterator<Edge> iterator = edgesElse.iterator(); iterator.hasNext();) {
                    Edge edge = iterator.next();
                    if(edge.getVertex1()==edgeCandidate.getVertex2() || edge.getVertex2()==edgeCandidate.getVertex2()){
                        edgesCandidate.add(edge);
                        iterator.remove();
                    }
                }
            }
            else if(!visited.contains(edgeCandidate.getVertex1()) && visited.contains(edgeCandidate.getVertex2())){
                visited.add(edgeCandidate.getVertex1());
                answer += edgeCandidate.getWeight();
                for (Iterator<Edge> iterator = edgesElse.iterator(); iterator.hasNext();) {
                    Edge edge = iterator.next();
                    if(edge.getVertex1()==edgeCandidate.getVertex1() || edge.getVertex2()==edgeCandidate.getVertex1()){
                        edgesCandidate.add(edge);
                        iterator.remove();
                    }
                }
            }
        }

        return answer;
    }
}