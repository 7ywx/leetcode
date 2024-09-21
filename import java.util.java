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
