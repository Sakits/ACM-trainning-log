比赛链接：https://vjudge.net/contest/416814#overview
## Problem A. Cyclic Troubles
## Problem B. Bergamot Problem
&emsp;&emsp;爆搜，可以用 bitset 预处理一下，复杂度贝尔数 $Bell(13)$。

## Problem C. Berhatton
## Problem E. Dance it up!
&emsp;&emsp;大讨论 DP。

&emsp;&emsp;状态记一下现在第几个 beat，两只脚的位置和两只脚前一次踩没踩，转移复杂度 $O(64)$，复杂度 $O(1000 * 64 * 64)$。

&emsp;&emsp;方案只要记录一下转移就好了。

## Problem F. Text Editor
&emsp;&emsp;搞个链表模拟一下就好了。

## Problem G. Friends of Friends
## Problem H. Berodoskar Development
## Problem I. The last hour of the contest
## Problem J. Geologist Dubrovsky
&emsp;&emsp;科学计算题，留着明年再做。

## Problem K. Terrorists in Berland
&emsp;&emsp;枚举割点，做全局最小割，SW算法可以记录方案，但是我不会。所以又写了最小割树，枚举两个点查最小割，如果最小割等于 SW 算出来的答案就把这两个点当源汇再跑一次 dinic，在 S 集和 T 集之间的边就是要割掉的边。
