# 高频题清单

按重要性两层组织：

- 🔥 **[Hot 100 主刷](#hot-100)**（100 题）：必须做完
- 📚 **[labuladong 扩展](#labuladong-扩展)**（68 题，二刷再说）：文件在 [`_labuladong_ext/`](_labuladong_ext/)

★ = 大厂面试出现频率最高的子集，建议反复刷。

---

<a id="hot-100"></a>
## 🔥 Hot 100（按 LeetCode 官方分类）

> 题号后面跟"→ 文件路径"，点开就能写。

### 哈希
- #1 两数之和 ★ → [01_array_string/0001_two_sum.py](01_array_string/0001_two_sum.py)
- #49 字母异位词分组 → [01_array_string/0049_group_anagrams.py](01_array_string/0049_group_anagrams.py)
- #128 最长连续序列 → [13_union_find/0128_longest_consecutive_sequence.py](13_union_find/0128_longest_consecutive_sequence.py)

### 双指针
- #283 移动零 → [04_two_pointers/0283_move_zeroes.py](04_two_pointers/0283_move_zeroes.py)
- #11 盛最多水的容器 → [04_two_pointers/0011_container_with_most_water.py](04_two_pointers/0011_container_with_most_water.py)
- #15 三数之和 ★ → [04_two_pointers/0015_three_sum.py](04_two_pointers/0015_three_sum.py)
- #42 接雨水 ★ → [11_monotonic_stack/0042_trapping_rain_water.py](11_monotonic_stack/0042_trapping_rain_water.py)

### 滑动窗口
- #3 无重复字符的最长子串 ★ → [05_sliding_window/0003_longest_substring.py](05_sliding_window/0003_longest_substring.py)
- #438 找到字符串中所有字母异位词 → [05_sliding_window/0438_find_anagrams.py](05_sliding_window/0438_find_anagrams.py)

### 子串
- #560 和为 K 的子数组 ★ → [15_prefix_sum/0560_subarray_sum_k.py](15_prefix_sum/0560_subarray_sum_k.py)
- #239 滑动窗口最大值 ★ → [11_monotonic_stack/0239_sliding_window_maximum.py](11_monotonic_stack/0239_sliding_window_maximum.py)
- #76 最小覆盖子串 ★ → [05_sliding_window/0076_minimum_window_substring.py](05_sliding_window/0076_minimum_window_substring.py)

### 普通数组
- #53 最大子数组和 ★ → [01_array_string/0053_max_subarray.py](01_array_string/0053_max_subarray.py)
- #56 合并区间 ★ → [01_array_string/0056_merge_intervals.py](01_array_string/0056_merge_intervals.py)
- #189 轮转数组 → [01_array_string/0189_rotate_array.py](01_array_string/0189_rotate_array.py)
- #238 除自身以外数组的乘积 → [01_array_string/0238_product_except_self.py](01_array_string/0238_product_except_self.py)
- #41 缺失的第一个正数 → [01_array_string/0041_first_missing_positive.py](01_array_string/0041_first_missing_positive.py)

### 矩阵
- #73 矩阵置零 → [01_array_string/0073_set_matrix_zeroes.py](01_array_string/0073_set_matrix_zeroes.py)
- #54 螺旋矩阵 → [01_array_string/0054_spiral_matrix.py](01_array_string/0054_spiral_matrix.py)
- #48 旋转图像 → [01_array_string/0048_rotate_image.py](01_array_string/0048_rotate_image.py)
- #240 搜索二维矩阵 II → [06_binary_search/0240_search_2d_matrix_ii.py](06_binary_search/0240_search_2d_matrix_ii.py)

### 链表
- #160 相交链表 → [02_linked_list/0160_intersection_of_two_lists.py](02_linked_list/0160_intersection_of_two_lists.py)
- #206 反转链表 ★ → [02_linked_list/0206_reverse_linked_list.py](02_linked_list/0206_reverse_linked_list.py)
- #234 回文链表 → [02_linked_list/0234_palindrome_linked_list.py](02_linked_list/0234_palindrome_linked_list.py)
- #141 环形链表 → [02_linked_list/0141_linked_list_cycle.py](02_linked_list/0141_linked_list_cycle.py)
- #142 环形链表 II ★ → [02_linked_list/0142_linked_list_cycle_ii.py](02_linked_list/0142_linked_list_cycle_ii.py)
- #21 合并两个有序链表 → [02_linked_list/0021_merge_two_sorted.py](02_linked_list/0021_merge_two_sorted.py)
- #2 两数相加 → [02_linked_list/0002_add_two_numbers.py](02_linked_list/0002_add_two_numbers.py)
- #19 删除倒数第 N 个节点 → [02_linked_list/0019_remove_nth_from_end.py](02_linked_list/0019_remove_nth_from_end.py)
- #24 两两交换链表中节点 → [02_linked_list/0024_swap_pairs.py](02_linked_list/0024_swap_pairs.py)
- #25 K 个一组翻转链表 ★ → [02_linked_list/0025_reverse_k_group.py](02_linked_list/0025_reverse_k_group.py)
- #138 复制带随机指针的链表 ★ → [02_linked_list/0138_copy_random_list.py](02_linked_list/0138_copy_random_list.py)
- #148 排序链表 → [02_linked_list/0148_sort_list.py](02_linked_list/0148_sort_list.py)
- #23 合并 K 个升序链表 ★ → [02_linked_list/0023_merge_k_sorted_lists.py](02_linked_list/0023_merge_k_sorted_lists.py)
- #146 LRU 缓存 ★ → [16_design/0146_lru_cache.py](16_design/0146_lru_cache.py)

### 二叉树
- #94 中序遍历 → [03_binary_tree/0094_inorder_traversal.py](03_binary_tree/0094_inorder_traversal.py)
- #104 最大深度 → [03_binary_tree/0104_max_depth.py](03_binary_tree/0104_max_depth.py)
- #226 翻转二叉树 → [03_binary_tree/0226_invert_binary_tree.py](03_binary_tree/0226_invert_binary_tree.py)
- #101 对称二叉树 → [03_binary_tree/0101_symmetric_tree.py](03_binary_tree/0101_symmetric_tree.py)
- #543 二叉树的直径 ★ → [03_binary_tree/0543_diameter.py](03_binary_tree/0543_diameter.py)
- #102 层序遍历 ★ → [03_binary_tree/0102_level_order.py](03_binary_tree/0102_level_order.py)
- #108 有序数组转 BST → [03_binary_tree/0108_sorted_array_to_bst.py](03_binary_tree/0108_sorted_array_to_bst.py)
- #98 验证 BST → [03_binary_tree/0098_validate_bst.py](03_binary_tree/0098_validate_bst.py)
- #230 BST 第 K 小 → [03_binary_tree/0230_kth_smallest_in_bst.py](03_binary_tree/0230_kth_smallest_in_bst.py)
- #199 二叉树右视图 → [03_binary_tree/0199_right_side_view.py](03_binary_tree/0199_right_side_view.py)
- #114 二叉树展开为链表 → [03_binary_tree/0114_flatten_binary_tree.py](03_binary_tree/0114_flatten_binary_tree.py)
- #105 前序+中序构造二叉树 ★ → [03_binary_tree/0105_construct_from_preorder_inorder.py](03_binary_tree/0105_construct_from_preorder_inorder.py)
- #437 路径总和 III → [15_prefix_sum/0437_path_sum_iii.py](15_prefix_sum/0437_path_sum_iii.py)
- #236 最近公共祖先 ★ → [03_binary_tree/0236_lowest_common_ancestor.py](03_binary_tree/0236_lowest_common_ancestor.py)
- #124 最大路径和 ★ → [03_binary_tree/0124_max_path_sum.py](03_binary_tree/0124_max_path_sum.py)

### 图论
- #200 岛屿数量 ★ → [07_dfs_bfs/0200_num_islands.py](07_dfs_bfs/0200_num_islands.py)
- #994 腐烂的橘子 → [07_dfs_bfs/0994_rotting_oranges.py](07_dfs_bfs/0994_rotting_oranges.py)
- #207 课程表 ★ → [14_graph/0207_course_schedule.py](14_graph/0207_course_schedule.py)
- #208 实现 Trie ★ → [16_design/0208_implement_trie.py](16_design/0208_implement_trie.py)

### 回溯
- #46 全排列 ★ → [08_backtracking/0046_permutations.py](08_backtracking/0046_permutations.py)
- #78 子集 ★ → [08_backtracking/0078_subsets.py](08_backtracking/0078_subsets.py)
- #17 电话号码字母组合 → [08_backtracking/0017_letter_combinations.py](08_backtracking/0017_letter_combinations.py)
- #39 组合总和 ★ → [08_backtracking/0039_combination_sum.py](08_backtracking/0039_combination_sum.py)
- #22 括号生成 ★ → [08_backtracking/0022_generate_parentheses.py](08_backtracking/0022_generate_parentheses.py)
- #79 单词搜索 → [08_backtracking/0079_word_search.py](08_backtracking/0079_word_search.py)
- #131 分割回文串 → [08_backtracking/0131_palindrome_partitioning.py](08_backtracking/0131_palindrome_partitioning.py)
- #51 N 皇后 ★ → [08_backtracking/0051_n_queens.py](08_backtracking/0051_n_queens.py)

### 二分查找
- #35 搜索插入位置 → [06_binary_search/0035_search_insert_position.py](06_binary_search/0035_search_insert_position.py)
- #74 搜索二维矩阵 → [06_binary_search/0074_search_2d_matrix.py](06_binary_search/0074_search_2d_matrix.py)
- #34 第一和最后位置 ★ → [06_binary_search/0034_first_last_position.py](06_binary_search/0034_first_last_position.py)
- #33 搜索旋转排序数组 ★ → [06_binary_search/0033_search_rotated.py](06_binary_search/0033_search_rotated.py)
- #153 寻找旋转数组最小值 → [06_binary_search/0153_find_min_in_rotated.py](06_binary_search/0153_find_min_in_rotated.py)
- #4 寻找两个正序数组的中位数 → [06_binary_search/0004_median_of_two_sorted_arrays.py](06_binary_search/0004_median_of_two_sorted_arrays.py)

### 栈
- #20 有效的括号 → [11_monotonic_stack/0020_valid_parentheses.py](11_monotonic_stack/0020_valid_parentheses.py)
- #155 最小栈 → [16_design/0155_min_stack.py](16_design/0155_min_stack.py)
- #394 字符串解码 → [11_monotonic_stack/0394_decode_string.py](11_monotonic_stack/0394_decode_string.py)
- #739 每日温度 ★ → [11_monotonic_stack/0739_daily_temperatures.py](11_monotonic_stack/0739_daily_temperatures.py)
- #84 柱状图最大矩形 ★ → [11_monotonic_stack/0084_largest_rectangle.py](11_monotonic_stack/0084_largest_rectangle.py)

### 堆
- #215 第 K 大 ★ → [12_heap_topk/0215_kth_largest.py](12_heap_topk/0215_kth_largest.py)
- #347 前 K 高频元素 ★ → [12_heap_topk/0347_top_k_frequent.py](12_heap_topk/0347_top_k_frequent.py)
- #295 数据流的中位数 ★ → [16_design/0295_find_median_from_data_stream.py](16_design/0295_find_median_from_data_stream.py)

### 贪心
- #121 买卖股票 I ★ → [09_dp/0121_best_time_buy_sell_stock.py](09_dp/0121_best_time_buy_sell_stock.py)
- #55 跳跃游戏 ★ → [10_greedy/0055_jump_game.py](10_greedy/0055_jump_game.py)
- #45 跳跃游戏 II → [10_greedy/0045_jump_game_ii.py](10_greedy/0045_jump_game_ii.py)
- #763 划分字母区间 → [10_greedy/0763_partition_labels.py](10_greedy/0763_partition_labels.py)

### 动态规划
- #70 爬楼梯 → [09_dp/0070_climbing_stairs.py](09_dp/0070_climbing_stairs.py)
- #118 杨辉三角 → [09_dp/0118_pascals_triangle.py](09_dp/0118_pascals_triangle.py)
- #198 打家劫舍 ★ → [09_dp/0198_house_robber.py](09_dp/0198_house_robber.py)
- #279 完全平方数 → [09_dp/0279_perfect_squares.py](09_dp/0279_perfect_squares.py)
- #322 零钱兑换 ★ → [09_dp/0322_coin_change.py](09_dp/0322_coin_change.py)
- #139 单词拆分 → [09_dp/0139_word_break.py](09_dp/0139_word_break.py)
- #300 最长递增子序列 ★ → [09_dp/0300_lis.py](09_dp/0300_lis.py)
- #152 乘积最大子数组 → [09_dp/0152_max_product_subarray.py](09_dp/0152_max_product_subarray.py)
- #416 分割等和子集 ★ → [09_dp/0416_partition_equal_subset_sum.py](09_dp/0416_partition_equal_subset_sum.py)
- #32 最长有效括号 → [09_dp/0032_longest_valid_parentheses.py](09_dp/0032_longest_valid_parentheses.py)

### 多维 DP
- #62 不同路径 → [09_dp/0062_unique_paths.py](09_dp/0062_unique_paths.py)
- #64 最小路径和 → [09_dp/0064_min_path_sum.py](09_dp/0064_min_path_sum.py)
- #5 最长回文子串 ★ → [01_array_string/0005_longest_palindrome.py](01_array_string/0005_longest_palindrome.py)
- #1143 最长公共子序列 ★ → [09_dp/1143_lcs.py](09_dp/1143_lcs.py)
- #72 编辑距离 ★ → [09_dp/0072_edit_distance.py](09_dp/0072_edit_distance.py)

### 技巧
- #136 只出现一次的数字 → [01_array_string/0136_single_number.py](01_array_string/0136_single_number.py)
- #169 多数元素 → [01_array_string/0169_majority_element.py](01_array_string/0169_majority_element.py)
- #75 颜色分类 → [04_two_pointers/0075_sort_colors.py](04_two_pointers/0075_sort_colors.py)
- #31 下一个排列 → [01_array_string/0031_next_permutation.py](01_array_string/0031_next_permutation.py)
- #287 寻找重复数 → [02_linked_list/0287_find_duplicate_number.py](02_linked_list/0287_find_duplicate_number.py)

### 加分必背（不在 Hot 100 主榜但大厂高频）
- #297 序列化与反序列化二叉树 ★ → [03_binary_tree/0297_serialize_deserialize.py](03_binary_tree/0297_serialize_deserialize.py)

---

<a id="labuladong-扩展"></a>
## 📚 labuladong 扩展（68 题，二刷再说）

文件全部在 [`_labuladong_ext/`](_labuladong_ext/) 下，按相同的 16 专题组织。一刷别动这些，等 Hot 100 全过一遍后再回来加深。

### 01 数组与字符串扩展
- #14 最长公共前缀 → [_labuladong_ext/01_array_string/0014_longest_common_prefix.py](_labuladong_ext/01_array_string/0014_longest_common_prefix.py)
- #88 合并两个有序数组 → [_labuladong_ext/01_array_string/0088_merge_sorted_array.py](_labuladong_ext/01_array_string/0088_merge_sorted_array.py)
- #165 比较版本号 → [_labuladong_ext/01_array_string/0165_compare_version.py](_labuladong_ext/01_array_string/0165_compare_version.py)

### 02 链表扩展
- #92 反转链表 II → [_labuladong_ext/02_linked_list/0092_reverse_linked_list_ii.py](_labuladong_ext/02_linked_list/0092_reverse_linked_list_ii.py)

### 03 二叉树扩展
- #144 前序遍历 → [_labuladong_ext/03_binary_tree/0144_preorder_traversal.py](_labuladong_ext/03_binary_tree/0144_preorder_traversal.py)
- #145 后序遍历 → [_labuladong_ext/03_binary_tree/0145_postorder_traversal.py](_labuladong_ext/03_binary_tree/0145_postorder_traversal.py)
- #110 平衡二叉树 → [_labuladong_ext/03_binary_tree/0110_balanced_binary_tree.py](_labuladong_ext/03_binary_tree/0110_balanced_binary_tree.py)
- #106 后序+中序构造二叉树 → [_labuladong_ext/03_binary_tree/0106_construct_from_inorder_postorder.py](_labuladong_ext/03_binary_tree/0106_construct_from_inorder_postorder.py)
- #700 BST 搜索 → [_labuladong_ext/03_binary_tree/0700_search_in_bst.py](_labuladong_ext/03_binary_tree/0700_search_in_bst.py)
- #701 BST 插入 → [_labuladong_ext/03_binary_tree/0701_insert_into_bst.py](_labuladong_ext/03_binary_tree/0701_insert_into_bst.py)
- #450 BST 删除 → [_labuladong_ext/03_binary_tree/0450_delete_node_in_bst.py](_labuladong_ext/03_binary_tree/0450_delete_node_in_bst.py)

### 04 双指针扩展
- #167 两数之和 II（有序） → [_labuladong_ext/04_two_pointers/0167_two_sum_ii.py](_labuladong_ext/04_two_pointers/0167_two_sum_ii.py)
- #16 最接近的三数之和 → [_labuladong_ext/04_two_pointers/0016_three_sum_closest.py](_labuladong_ext/04_two_pointers/0016_three_sum_closest.py)
- #18 四数之和 → [_labuladong_ext/04_two_pointers/0018_four_sum.py](_labuladong_ext/04_two_pointers/0018_four_sum.py)
- #26 删除有序数组重复项 → [_labuladong_ext/04_two_pointers/0026_remove_duplicates.py](_labuladong_ext/04_two_pointers/0026_remove_duplicates.py)

### 05 滑动窗口扩展
- #209 长度最小子数组 → [_labuladong_ext/05_sliding_window/0209_minimum_size_subarray_sum.py](_labuladong_ext/05_sliding_window/0209_minimum_size_subarray_sum.py)
- #567 字符串的排列 → [_labuladong_ext/05_sliding_window/0567_permutation_in_string.py](_labuladong_ext/05_sliding_window/0567_permutation_in_string.py)

### 06 二分扩展
- #704 二分查找（最基础模板） → [_labuladong_ext/06_binary_search/0704_binary_search.py](_labuladong_ext/06_binary_search/0704_binary_search.py)
- #162 寻找峰值 → [_labuladong_ext/06_binary_search/0162_find_peak_element.py](_labuladong_ext/06_binary_search/0162_find_peak_element.py)
- #875 爱吃香蕉的珂珂（二分答案） → [_labuladong_ext/06_binary_search/0875_koko_eating_bananas.py](_labuladong_ext/06_binary_search/0875_koko_eating_bananas.py)
- #410 分割数组的最大值 → [_labuladong_ext/06_binary_search/0410_split_array_largest_sum.py](_labuladong_ext/06_binary_search/0410_split_array_largest_sum.py)

### 07 DFS / BFS 扩展
- #111 二叉树最小深度 → [_labuladong_ext/07_dfs_bfs/0111_min_depth.py](_labuladong_ext/07_dfs_bfs/0111_min_depth.py)
- #695 岛屿最大面积 → [_labuladong_ext/07_dfs_bfs/0695_max_island_area.py](_labuladong_ext/07_dfs_bfs/0695_max_island_area.py)
- #130 被围绕的区域 → [_labuladong_ext/07_dfs_bfs/0130_surrounded_regions.py](_labuladong_ext/07_dfs_bfs/0130_surrounded_regions.py)
- #127 单词接龙 → [_labuladong_ext/07_dfs_bfs/0127_word_ladder.py](_labuladong_ext/07_dfs_bfs/0127_word_ladder.py)
- #752 打开转盘锁 → [_labuladong_ext/07_dfs_bfs/0752_open_the_lock.py](_labuladong_ext/07_dfs_bfs/0752_open_the_lock.py)

### 08 回溯扩展（去重变体）
- #47 全排列 II → [_labuladong_ext/08_backtracking/0047_permutations_ii.py](_labuladong_ext/08_backtracking/0047_permutations_ii.py)
- #90 子集 II → [_labuladong_ext/08_backtracking/0090_subsets_ii.py](_labuladong_ext/08_backtracking/0090_subsets_ii.py)
- #40 组合总和 II → [_labuladong_ext/08_backtracking/0040_combination_sum_ii.py](_labuladong_ext/08_backtracking/0040_combination_sum_ii.py)

### 09 DP 扩展
- #213 打家劫舍 II → [_labuladong_ext/09_dp/0213_house_robber_ii.py](_labuladong_ext/09_dp/0213_house_robber_ii.py)
- #337 打家劫舍 III（树形 DP） → [_labuladong_ext/09_dp/0337_house_robber_iii.py](_labuladong_ext/09_dp/0337_house_robber_iii.py)
- #122 买卖股票 II → [_labuladong_ext/09_dp/0122_best_time_buy_sell_stock_ii.py](_labuladong_ext/09_dp/0122_best_time_buy_sell_stock_ii.py)
- #123 买卖股票 III → [_labuladong_ext/09_dp/0123_best_time_buy_sell_stock_iii.py](_labuladong_ext/09_dp/0123_best_time_buy_sell_stock_iii.py)
- #188 买卖股票 IV → [_labuladong_ext/09_dp/0188_best_time_buy_sell_stock_iv.py](_labuladong_ext/09_dp/0188_best_time_buy_sell_stock_iv.py)
- #309 含冷冻期 → [_labuladong_ext/09_dp/0309_buy_sell_with_cooldown.py](_labuladong_ext/09_dp/0309_buy_sell_with_cooldown.py)
- #714 含手续费 → [_labuladong_ext/09_dp/0714_buy_sell_with_fee.py](_labuladong_ext/09_dp/0714_buy_sell_with_fee.py)
- #63 不同路径 II → [_labuladong_ext/09_dp/0063_unique_paths_ii.py](_labuladong_ext/09_dp/0063_unique_paths_ii.py)
- #221 最大正方形 → [_labuladong_ext/09_dp/0221_maximal_square.py](_labuladong_ext/09_dp/0221_maximal_square.py)
- #494 目标和 → [_labuladong_ext/09_dp/0494_target_sum.py](_labuladong_ext/09_dp/0494_target_sum.py)
- #518 零钱兑换 II → [_labuladong_ext/09_dp/0518_coin_change_ii.py](_labuladong_ext/09_dp/0518_coin_change_ii.py)
- #516 最长回文子序列 → [_labuladong_ext/09_dp/0516_longest_palindromic_subsequence.py](_labuladong_ext/09_dp/0516_longest_palindromic_subsequence.py)
- #312 戳气球（区间 DP） → [_labuladong_ext/09_dp/0312_burst_balloons.py](_labuladong_ext/09_dp/0312_burst_balloons.py)
- #877 石子游戏 → [_labuladong_ext/09_dp/0877_stone_game.py](_labuladong_ext/09_dp/0877_stone_game.py)

### 10 贪心扩展
- #134 加油站 → [_labuladong_ext/10_greedy/0134_gas_station.py](_labuladong_ext/10_greedy/0134_gas_station.py)
- #435 无重叠区间 → [_labuladong_ext/10_greedy/0435_non_overlapping_intervals.py](_labuladong_ext/10_greedy/0435_non_overlapping_intervals.py)
- #452 用最少箭引爆气球 → [_labuladong_ext/10_greedy/0452_min_arrows_burst_balloons.py](_labuladong_ext/10_greedy/0452_min_arrows_burst_balloons.py)
- #406 根据身高重建队列 → [_labuladong_ext/10_greedy/0406_queue_reconstruction_by_height.py](_labuladong_ext/10_greedy/0406_queue_reconstruction_by_height.py)

### 11 单调栈扩展
- #496 下一个更大元素 I → [_labuladong_ext/11_monotonic_stack/0496_next_greater_element_i.py](_labuladong_ext/11_monotonic_stack/0496_next_greater_element_i.py)
- #503 下一个更大元素 II（循环数组） → [_labuladong_ext/11_monotonic_stack/0503_next_greater_element_ii.py](_labuladong_ext/11_monotonic_stack/0503_next_greater_element_ii.py)
- #85 最大矩形 → [_labuladong_ext/11_monotonic_stack/0085_maximal_rectangle.py](_labuladong_ext/11_monotonic_stack/0085_maximal_rectangle.py)

### 12 堆 / TopK 扩展
- #692 前 K 高频单词 → [_labuladong_ext/12_heap_topk/0692_top_k_frequent_words.py](_labuladong_ext/12_heap_topk/0692_top_k_frequent_words.py)
- #378 有序矩阵第 K 小 → [_labuladong_ext/12_heap_topk/0378_kth_smallest_in_sorted_matrix.py](_labuladong_ext/12_heap_topk/0378_kth_smallest_in_sorted_matrix.py)

### 13 并查集扩展
- #547 省份数量（UF 模板） → [_labuladong_ext/13_union_find/0547_provinces.py](_labuladong_ext/13_union_find/0547_provinces.py)
- #684 冗余连接 → [_labuladong_ext/13_union_find/0684_redundant_connection.py](_labuladong_ext/13_union_find/0684_redundant_connection.py)
- #685 冗余连接 II → [_labuladong_ext/13_union_find/0685_redundant_connection_ii.py](_labuladong_ext/13_union_find/0685_redundant_connection_ii.py)
- #990 等式方程的可满足性 → [_labuladong_ext/13_union_find/0990_satisfiability_of_equality.py](_labuladong_ext/13_union_find/0990_satisfiability_of_equality.py)

### 14 图论扩展
- #210 课程表 II → [_labuladong_ext/14_graph/0210_course_schedule_ii.py](_labuladong_ext/14_graph/0210_course_schedule_ii.py)
- #743 网络延迟时间（Dijkstra） → [_labuladong_ext/14_graph/0743_network_delay_time.py](_labuladong_ext/14_graph/0743_network_delay_time.py)
- #787 K 站中转最便宜航班（Bellman-Ford） → [_labuladong_ext/14_graph/0787_cheapest_flights.py](_labuladong_ext/14_graph/0787_cheapest_flights.py)
- #1584 连接所有点最小费用（MST） → [_labuladong_ext/14_graph/1584_min_cost_connect_points.py](_labuladong_ext/14_graph/1584_min_cost_connect_points.py)

### 15 前缀和 / 差分扩展
- #303 区域和检索 → [_labuladong_ext/15_prefix_sum/0303_range_sum_query.py](_labuladong_ext/15_prefix_sum/0303_range_sum_query.py)
- #304 二维区域和 → [_labuladong_ext/15_prefix_sum/0304_range_sum_query_2d.py](_labuladong_ext/15_prefix_sum/0304_range_sum_query_2d.py)
- #974 和可被 K 整除的子数组 → [_labuladong_ext/15_prefix_sum/0974_subarray_sums_divisible_by_k.py](_labuladong_ext/15_prefix_sum/0974_subarray_sums_divisible_by_k.py)
- #1109 航班预订统计（差分） → [_labuladong_ext/15_prefix_sum/1109_corporate_flight_bookings.py](_labuladong_ext/15_prefix_sum/1109_corporate_flight_bookings.py)

### 16 设计扩展
- #232 用栈实现队列 → [_labuladong_ext/16_design/0232_implement_queue_using_stacks.py](_labuladong_ext/16_design/0232_implement_queue_using_stacks.py)
- #380 O(1) 时间插入删除随机 → [_labuladong_ext/16_design/0380_insert_delete_get_random.py](_labuladong_ext/16_design/0380_insert_delete_get_random.py)
- #211 添加与搜索单词 → [_labuladong_ext/16_design/0211_word_dictionary.py](_labuladong_ext/16_design/0211_word_dictionary.py)
- #460 LFU 缓存 → [_labuladong_ext/16_design/0460_lfu_cache.py](_labuladong_ext/16_design/0460_lfu_cache.py)

---

## 复盘节奏建议

- **第一遍**：按 [README.md](README.md) 路线图，每周专题打开对应目录把 ★ 题做完，再把同专题非 ★ 全做完。**只做 16 个 topic 目录里的，不动 `_labuladong_ext/`**。
- **第二遍**：只做被自己标记过"卡壳"的题（看每题文件顶部 docstring 复盘要点 / [_review/](_review/) 笔记）。可选做 `_labuladong_ext/` 中你薄弱专题对应的扩展。
- **冲刺周**：每天回看 5 道 ★ 题，能在 5 分钟内说出"思路+模板"算过关。
