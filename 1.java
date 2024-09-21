public class DuplicateWordsCounter {
    public static void main(String[] args) {
        // 假设输入已经通过标准输入流获取，这里使用字符串模拟
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();  // 读取一行输入
		Map<Character, Integer> map = new LinkedHashMap<Character, Integer>();
		
		//writer your code here
		for (int i = 0; i < input.length(); i++) {
			char ch = input.charAt(i);
			if (map.containsKey(ch)) {
				map.put(ch, map.get(ch) + 1);
			} else {
				map.put(ch, 1);
			}
		}
		Set<Map.Entry<Character, Integer>> entrySet = map.entrySet();
		for (Map.Entry<Character, Integer> entry : entrySet) {
			System.out.println(entry.getKey() + ":" + entry.getValue());
		}
        // 处理输入
        int count = countDuplicateWords(input);

        // 输出结果
        System.out.println(count);
    }

    private static int countDuplicateWords(String sentence) {
        // 使用正则表达式分割句子为单词数组
        String[] words = sentence.toLowerCase().split("\\W+");

        Map<String, Integer> wordCount = new HashMap<>();
        int duplicates = 0;

        // 遍历单词数组
        for (String word : words) {
            if (!word.isEmpty()) {  // 忽略空字符串
                wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
                // 如果单词计数大于1，则为重复单词
                if (wordCount.get(word) == 2) {
                    duplicates++;
                }
            }
        }

        return duplicates;
    }
}