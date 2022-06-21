import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FloorDecoration_1388 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String map[][] = new String[n][m];
        int cnt = 0;
        boolean cnt_flag;

        for (int i=0; i<n; i++) {
            map[i] = br.readLine().split("");
        }

        for (int i=0; i<n; i++) {
            cnt_flag = false;
            for (int j=0; j<m; j++) {
                if (!cnt_flag) {
                    if (map[i][j].equals("-")) {
                        cnt_flag = true;
                        cnt += 1;
                    }
                }
                else {
                    if (!map[i][j].equals("-")) {
                        cnt_flag = false;
                    }
                }
            }
        }

        for (int i=0; i<m; i++) {
            cnt_flag = false;
            for (int j = 0; j < n; j++) {
                if (!cnt_flag) {
                    if (map[j][i].equals("|")) {
                        cnt_flag = true;
                        cnt += 1;
                    }
                } else {
                    if (!map[j][i].equals("|")) {
                        cnt_flag = false;
                    }
                }
            }
        }
        System.out.println(cnt);
    }
}
