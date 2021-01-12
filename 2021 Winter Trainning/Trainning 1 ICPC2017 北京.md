比赛链接：https://vjudge.net/contest/416707#overview
## C - Graph 
&emsp;&emsp;Solved by wennitao

&emsp;&emsp;回滚莫队 + 并查集

&emsp;&emsp;第一次看见这个是在ccz博客

&emsp;&emsp;https://www.cnblogs.com/ccz181078/p/5638860.html
## D - Chinese Checkers
&emsp;&emsp;大模拟题，没做

## E - Cats and Fish & F - Secret Poems 
&emsp;&emsp;Solved by wennitao

## G - Liaoning Ship’s Voyage 
&emsp;&emsp;是个不算难的计算几何，但是完全不会计算几何所以就不补了 

## H - Puzzle Game 
&emsp;&emsp;先预处理出最大权子矩阵，权值和设为 $ans1$

&emsp;&emsp;然后枚举每个点 $(i, j)$ 为要改变的点，那么改变之后的最大权为$\max($不包含这个点的最大权子矩阵, 
$ans1 + delta)$。

&emsp;&emsp;如果原矩阵最大权包含这个点，那么新矩阵最大权就是不包含这个点的最大权和最大权加上变化量的最大值。

&emsp;&emsp;如果原矩阵最大权不包含这个点，那么新矩阵最大权为原最大权。

&emsp;&emsp;上式子可以包含这两种情况。

## I - Colored Nodes
&emsp;&emsp;是个贼有意思的思维好题。
&emsp;&emsp;首先暴力做一轮，可以得到每个点经过一轮之后会变成哪个点的颜色。因为每个点指向一个点，所以这实际上变成了基环树森林。经过无限轮之后图中只会留下环上的颜色，并且环上每种颜色的答案都是相同的。
&emsp;&emsp;此时把每棵基环树缩成一个点，也就是把在某棵基环树里的点都视为一种颜色，然后再暴力模拟一轮，同时记录每种颜色的出现次数，最后把每种颜色的出现次数除以所在环的大小就是环上每一种颜色的出现次数了。最后答案除以 $n$ 即可。

## J - Pangu and Stones 
&emsp;&emsp;DP。

&emsp;&emsp;$f_{i, j, k}$ 表示区间 $[i, j]$，现在有 $k$ 堆石头的最小权值。

&emsp;&emsp;转移的时候 $k = l\sim r$ 都可以转移到 $k = 1$，代价就是所有石子的权值和。

&emsp;&emsp;注意每次 $k$ 通过 $k - 1$ 和 $1$ 来转移就好了，这样复杂度就是 $O(n^4)$ 的了。