比赛链接：https://vjudge.net/contest/417508
## Problem A. Digits Are Not Just Characters
&emsp;&emsp;模拟题。

## Problem B. Arithmetic Progressions
&emsp;&emsp;这题卡 map 空间也太阴间了...

&emsp;&emsp;因为是集合所以直接先排个序就好了。然后设 $f_{i, j}$ 表示以 $i$ 结尾，差为 $a_i - a_j$ 的最长等差子序列，转移二分一下 $j$ 是否有个差是 $a_i - a_j$ 就好了。

## Problem C. Emergency Evacuation
&emsp;&emsp;模拟题 * 2。

## Problem D. Shortest Common Non-Subsequence
&emsp;&emsp;dp。

&emsp;&emsp;设 $f_{i, j}$ 表示第一个字符串从头开始匹配到 $i$，第二个字符串从头开始匹配到 $j$ 的最短字符串长度。

&emsp;&emsp;求方案的话按位贪心，判断填完之后剩下的部分还能不能到达答案即可。

## Problem E. Eulerian Flight Tour
&emsp;&emsp;欧拉回路的充要条件是每个点的度数都是偶数，但是一开始每个点的初始度数都不同，所以直接处理比较麻烦，不如考虑先补成完全图再进行删边，删边必须在原图的补图中，这样所有点的初始度数都是奇数的（如果原图是奇数个点补成完全图就好了）。

&emsp;&emsp;考虑补图，任意一个连通块点数必须是偶数，否则无论怎么删边度数为奇数的点还是奇数度数。并且如果是偶数就一定可以补成合法的，找到一棵生成树搞起来就好了。

&emsp;&emsp;剩下的按整个图连通不连通讨论一下就好了。还需要特判一下一个点和一个连通块的情况。

## Problem F. Fair Chocolate-Cutting
&emsp;&emsp;是个不难的几何题，但是感觉不太好写。

&emsp;&emsp;面积相同的直线一定经过质心，然后三分一下就好了。

## Problem G. What Goes Up Must Come Down
&emsp;&emsp;每次找到最小的数，然后直接把它换到两端里更近的一端，再把它删掉就是最优策略。

&emsp;&emsp;可以直接模拟，也可以分析一下发现就是求一下正反逆序对。

## Problem J. Colorful Tree
&emsp;&emsp;只想到两个 log 的，一个 log 的有点妙，没想到。

&emsp;&emsp;两个 log 就是直接单独考虑把每一种颜色的操作拿出来单独做，每次相当于在树上找到离这个点最近的同色的祖先，然后把这条路径给删掉或者加上。

&emsp;&emsp;找最近同色祖先的操作就是把这种颜色的点权值设为 1，其他的设为 0，然后每次倍增向上挑同时链查一下路径的权值和就能找到了。

&emsp;&emsp;一个 log 的做法是把每一种颜色的直接按 dfs 序塞进 set，维护 set 里相邻两点的距离和 set 头尾的距离和，这样涉及到的边的每一条边权都会被加两次，除以 2 就是答案了。

## Problem K. Sixth Sense
&emsp;&emsp;田忌赛马题。

&emsp;&emsp;首先贪心策略是把两个序列都排序，第一个序列维护一个指针，表示对方前 $i$ 匹 🐎 被干掉了，然后扫自己的 🐎，如果指针当前指的 🐎 能被自己当前扫到的 🐎 干掉，就把指针向后移动一位，否则不管。然后最后指针移动了几次就能干掉对方的几个 🐎。

&emsp;&emsp;考虑字典序最大的方案，对于每一个位置分两种情况二分，第一种是这一局干不掉对方的 🐎 ，第二种是能干掉，在这两种情况内部是分别满足二分性的。二分了这一位的答案之后，剩下的位数按照前一段提到的贪心方法 check 一下答案是否会变劣即可。

&emsp;&emsp;check 可以直接暴力 $O(n)$，用霍尔定理 + 数据结构维护一下好像可以做到 $O(\log)$，那这题说不定是可以 $O(n\log ^ 2n)$的。