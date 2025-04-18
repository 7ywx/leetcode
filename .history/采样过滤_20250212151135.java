// /**
//  * 采样过滤.
//  * @param M         故障确认周期数.
//  * @param T         故障次数门限.
//  * @param P         故障恢复周期数.
//  * @param samples   样品数据.
//  * @return          正常值的最长连续周期.
//  *
//  * 工具是否故障的规则：     在 m 个周期内，故障次数为 t 次
//  * 判断故障恢复条件：      产生故障后（确认工具故障，才为产生故障后） e 个周期内，采样数据一直为正常值.
//  * 错误采样数据处理方式：   检测到故障之后，丢弃从故障开始到故障恢复的采样数据.
//  *                      检测到故障之前，错误的采样数据，由最近一个正常值代替；如果前面没有正常的采样值，则丢弃该采样数据.
//  *
//  *  错误采样数据确认方式：s[i] <= 0
//  *                    s[i] < s[i-1]
//  *                    s[i] - s[i-1] >= 10
//  *
//  *  首先要在 每一个 m 周期内，统计错误采样数据的次数.
//  */
// private static int takeSampleFilter(int M, int T, int P, int[] samples) {
//     // 下标 i ->  正常迭代下标.
//     int i= 0;
//     int n = samples.length;
//     int cycle = 0,fail = 0;

//     // 用一个栈把正常数据的下标都给保存下来.
//     Deque<Integer> deque = new LinkedList<>();

//     while(i < n) {
//         //  直接判断在 M 周期内是不是进入了故障恢复期.
//         if(cycle <= M) {
//             // cycle永远小于M，因为进入下一个周期，会重置 cycle 和 fail.
//             if(fail == T) {
//                 // 这个时候进入恢复周期，产生故障之后，优先进入恢复周期，即使 M 周期没有走完.
//                 // 恢复周期为 T
//                 int count = P;
//                 while(count > 0 && i < n) {
//                     if(judge(samples, i)) {
//                         // 这里的话， 表示数据还是异常.
//                         count = P;
//                     } else {
//                         count--;
//                     }
//                     i++;
//                 }
//                 // 如果已经恢复，那么进入到正常的周期循环，此时 i 的位置代表了，数据恢复正常之后的第一个数据位置.
//                 cycle = fail = 0;
//                 continue;
//             }
//             if(cycle == M) {
//                 // 进入下一个周期.
//                 cycle = fail = 0;
//                 continue;
//             }
//         }

//         // true ： 数据采样错误.
//         if(judge(samples, i)) {
//             // 故障次数+1
//             fail++;
//             //  数据故障，判断是否可以被近似正常值代替.
//             //  栈不为空，表示存在近似正常数据.
//             if(!deque.isEmpty()) {
//                 samples[i] = samples[deque.peek()];
//                 deque.push(i);
//             }
//         } else {
//             //  如果是正确采样数据的话，保存下标.
//             deque.push(i);
//         }
//         // 周期数+1
//         cycle++;
//         i++;
//     }

//     int ans = 0;
//     int lastIndex = deque.pop();
//     int temp = 1;
//     while(!deque.isEmpty()) {
//         if(deque.peek() + 1 == lastIndex) {
//             temp++;
//             lastIndex = deque.pop();
//         } else {
//             ans = Math.max(ans, temp);
//             lastIndex = deque.pop();
//             temp = 1;
//         }
//     }

//     return ans==0?temp:ans;
// }

// private static boolean judge(int[] samples, int i) {
//     return samples[i] <= 0 || (i >= 1 && (samples[i] < samples[i-1])) || samples[i] - samples[i-1] >= 10;
// }

public class SampleFilter {

    /**
     * 采样过滤.
     *
     * @param M       故障确认周期数.
     * @param T       故障次数门限.
     * @param P       故障恢复周期数.
     * @param samples 样品数据.
     * @return 正常值的最长连续周期.
     */
    private static int takeSampleFilter(int M, int T, int P, int[] samples) {
        // 下标 i -> 正常迭代下标.
        int i = 0;
        int n = samples.length;
        int cycle = 0, fail = 0;

        // 用一个栈把正常数据的下标都给保存下来.
        Deque<Integer> deque = new LinkedList<>();

        while (i < n) {
            // 直接判断在 M 周期内是不是进入了故障恢复期.
            if (cycle <= M) {
                // cycle永远小于M，因为进入下一个周期，会重置 cycle 和 fail.
                if (fail == T) {
                    // 这个时候进入恢复周期，产生故障之后，优先进入恢复周期，即使 M 周期没有走完.
                    // 恢复周期为 T
                    int count = P;
                    while (count > 0 && i < n) {
                        if (judge(samples, i)) {
                            // 这里的话， 表示数据还是异常.
                            count = P;
                        } else {
                            count--;
                        }
                        i++;
                    }
                    // 如果已经恢复，那么进入到正常的周期循环，此时 i 的位置代表了，数据恢复正常之后的第一个数据位置.
                    cycle = fail = 0;
                    continue;
                }
                if (cycle == M) {
                    // 进入下一个周期.
                    cycle = fail = 0;
                    continue;
                }
            }

            // true ： 数据采样错误.
            if (judge(samples, i)) {
                // 故障次数+1
                fail++;
                // 数据故障，判断是否可以被近似正常值代替.
                // 栈不为空，表示存在近似正常数据.
                if (!deque.isEmpty()) {
                    samples[i] = samples[deque.peek()];
                    deque.push(i);
                }
            } else {
                // 如果是正确采样数据的话，保存下标.
                deque.push(i);
            }
            // 周期数+1
            cycle++;
            i++;
        }

        int ans = 0;
        int lastIndex = deque.pop();
        int temp = 1;
        while (!deque.isEmpty()) {
            if (deque.peek() + 1 == lastIndex) {
                temp++;
                lastIndex = deque.pop();
            } else {
                ans = Math.max(ans, temp);
                lastIndex = deque.pop();
                temp = 1;
            }
        }

        return ans == 0 ? temp : ans;
    }

    private static boolean judge(int[] samples, int i) {
        return samples[i] <= 0 || (i >= 1 && (samples[i] < samples[i - 1])) || samples[i] - samples[i - 1] >= 10;
    }

    public static void main(String[] args) {
        // 测试用例
        int M = 5;
        int T = 3;
        int P = 2;
        int[] samples = { 1, 2, 3, -1, 4, 5, 15, 6, 7, 8 };
        System.out.println("最长连续正常周期: " + takeSampleFilter(M, T, P, samples));
    }
}
