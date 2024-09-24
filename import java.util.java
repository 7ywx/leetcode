import java.util.Scanner;

public class Skiing {
    private static int[][] heights;
    private static int[][] dp;
    private static int n, m;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 输入矩阵的大小
        n = scanner.nextInt();
        m = scanner.nextInt();
        heights = new int[n][m];
        dp = new int[n][m]; // 用于存储最长路径长度

        // 输入高度矩阵
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                heights[i][j] = scanner.nextInt();
                dp[i][j] = -1; // 初始化为 -1，表示未计算
            }
        }

        int longestPath = 0;

        // 遍历每个位置，寻找最长滑雪路径
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                longestPath = Math.max(longestPath, dfs(i, j));
            }
        }

        System.out.println(longestPath);
        scanner.close();
    }

    private static int dfs(int x, int y) {
        // 如果已经计算过，直接返回
        if (dp[x][y] != -1) {
            return dp[x][y];
        }

        int maxPath = 1; // 至少包含当前位置
        int[] dx = {1, -1, 0, 0}; // 上下移动
        int[] dy = {0, 0, 1, -1}; // 左右移动

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            // 检查新位置是否在范围内且高度低于当前高度
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && heights[nx][ny] < heights[x][y]) {
                maxPath = Math.max(maxPath, 1 + dfs(nx, ny));
            }
        }

        dp[x][y] = maxPath; // 存储结果
        return maxPath;
    }
}
/*import java.util.Scanner;
import static java.lang.Math.max;
// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        while (in.hasNextInt()) { // 注意 while 处理多个 case
            int a = in.nextInt();
            int b = in.nextInt();

            int [][] skiMap = new int[a][b];
            for (int i = 0; i < b; i++){
                for (int j = 0; j < a; j++){
                    skiMap[i][j] = in.nextInt();
                }
            }

            int longestPat = longestPath(skiMap);
            System.out.println(longestPat);
        }
    }
    public static int longestPath(int[][] skiMap){
        if (skiMap == null || skiMap.length==0 || skiMap[0].length==0) return 0;

        int rows = skiMap.length;
        int cols = skiMap[0].length;
        int [][] dp = new int[rows][cols];
        for (int i = 0; i < rows;i++){
            for(int j= 0;j<cols;j++){
                dp[i][j] = 1;
            }
        }

        for (int r = 0; r <rows;r++){
            for(int c = 0; c<cols;c++){
                for (int[] dir : new int[][]{{-1, 0}, {1,0}, {0,-1}, {0,1}}) {
                    int nr = r + dir[0];
                    int nc = c+dir[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && skiMap[nr][nc] < skiMap[r][c]){
                        dp[r][c] = Math.max(dp[r][c], dp[nr][nc] + 1);
                    }
                }
            }
        }
        int max = 0;
        for (int[] row : dp){
            for (int length:row){
                max = Math.max(max, length);
            }
        }
        return max;

    }
} */
