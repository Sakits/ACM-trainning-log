# D - Knapsack Queries on a tree
&emsp;&emsp;两种暴力，一种是直接背包，预处理 $O(n)$，询问 $O(1)$，一种是直接当 np 问题做，询问复杂度 $O(2^{depth}) = O(n)$。
&emsp;&emsp;平衡一下两部分复杂度就好了，$O((n + Q)\sqrt{n})$。