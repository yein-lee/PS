import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


public class Main {
    static int N;
    static int[][] arr;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static List<Integer> houseCount;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        visited = new boolean[N][N];
        houseCount = new ArrayList<>();

        for(int i=0; i<N; i++) {
            String str = br.readLine();
            for(int j=0; j<N; j++) {
                arr[i][j] = Character.getNumericValue(str.charAt(j));
                visited[i][j] = false;
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(arr[i][j]==1 && !visited[i][j]){
                    bfs(i, j);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(houseCount.size()).append("\n");
        Collections.sort(houseCount);
        for (Object o : houseCount) {
            sb.append(o).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    public static void bfs(int x, int y){
        int count = 0;
        Queue<int []> queue = new LinkedList<>();

        queue.add(new int[]{x,y});
        visited[x][y] = true;
        count ++;

        while(!queue.isEmpty()){
            int [] currentCoordinate = queue.poll();
            int currentX = currentCoordinate[0];
            int currentY = currentCoordinate[1];
            for(int i=0; i<4; i++){
                int moveX = currentX + dx[i];
                int moveY = currentY + dy[i];
                if(moveX<N && moveX>=0 && moveY<N && moveY>=0 && arr[moveX][moveY]==1 && !visited[moveX][moveY]){
                    visited[moveX][moveY] = true;
                    count++;
                    queue.add(new int[]{moveX,moveY});
                }
            }
        }
        houseCount.add(count);
    }
}