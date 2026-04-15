import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        List<Integer>[] red = new ArrayList[n];
        List<Integer>[] blue = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            red[i] = new ArrayList<>();
            blue[i] = new ArrayList<>();
        }

        for (int[] e : redEdges) red[e[0]].add(e[1]);
        for (int[] e : blueEdges) blue[e[0]].add(e[1]);

        int[][] dist = new int[n][2];
        for (int[] d : dist) Arrays.fill(d, -1);

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        q.offer(new int[]{0, 1});
        dist[0][0] = dist[0][1] = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int node = curr[0], color = curr[1];

            if (color == 0) {
                for (int nei : blue[node]) {
                    if (dist[nei][1] == -1) {
                        dist[nei][1] = dist[node][0] + 1;
                        q.offer(new int[]{nei, 1});
                    }
                }
            } else {
                for (int nei : red[node]) {
                    if (dist[nei][0] == -1) {
                        dist[nei][0] = dist[node][1] + 1;
                        q.offer(new int[]{nei, 0});
                    }
                }
            }
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            if (dist[i][0] == -1 || dist[i][1] == -1) {
                res[i] = Math.max(dist[i][0], dist[i][1]);
            } else {
                res[i] = Math.min(dist[i][0], dist[i][1]);
            }
        }
        return res;
    }
}