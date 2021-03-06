比赛链接：https://vjudge.net/contest/417523
## A - Fast Forwarding
&emsp;&emsp;考虑先一堆 3x 到最大的速度，中间一段持续最大的速度，然后再一堆 1/3x，1/3x 那段把剩下的部分填完就好了。

## B - Estimating the Flood Risk
&emsp;&emsp;有解的充要条件是两两确定位置的点的曼哈顿距离大于等于高度之差。

&emsp;&emsp;然后剩下的填法就是这个点到所有确定位置的点的曼哈顿距离的 max。

## C - Wall Painting 
&emsp;&emsp;首先任意一个点不会被三条线段覆盖，否则去掉中间那个线段答案不会变劣。

&emsp;&emsp;其次选择的线段不可能出现互相包含的情况，否则删掉被包含的那条线段同样答案不会变劣。

&emsp;&emsp;然后就可以 dp 了，把线段按右端点排序，钦定 $f_i$ 表示第 $i$ 条线段要选的最大收益，转移用树状数组优化一下就好了。

## E - Reordering the Documents 
&emsp;&emsp;这题不是我做的，但可以口胡一下。

&emsp;&emsp;原题相当于把一个序列分成两个长度均不超过 $m$ 的递增子序列。那么可以看成是一段是属于第一个，一段属于第二个，然后交错的划分方式。

&emsp;&emsp;设 $f_{i, j}$ 表示第 $i$ 个属于其中一个子序列，当前这个子序列长度为 $j$，并且第 $i - 1$ 个是属于另外一个子序列的，换句话说这是一段的开头。

&emsp;&emsp;假设以 $i - 1$ 结尾的极长递增连续子段是 $[k, i - 1]$，那么 $f_{i, j}$ 可以从 $f_{k, i - j - (i - k)}$ 转移过来，这个前缀和记录一下就好了。

## G - Ambiguous Encoding 
&emsp;&emsp;会出现冲突的情况就是一个序列有两种不同的划分方式。

&emsp;&emsp;考虑对于两种划分方式，把每个字符串的结束位置作为划分点，对划分点进行dp。

&emsp;&emsp;当一种划分方案中的某个字符串到达结束位置，另一种划分方案如果也到达结束位置，那么就找到一种有两种划分方式的答案了。所以假设另一种划分方案没到达结束位置，并且设那是第 $i$ 个字符串的第 $j$ 个位置。于是$f_{i, j}$ 表示其中一种划分方案到达第 $i$ 个字符串的第 $j$ 个位置，并且另一种划分方案到达结束位置的最短长度。

&emsp;&emsp;转移有两种。一种是把第 $i$ 个字符串的剩下 $len - j$ 个位置匹配完，到达另一个字符串 $k$ 的第 $l$ 个位置。另一种是把第 $k$ 个字符串给匹配完，到达第 $i$ 个字符串的第 $j + len_k$ 个位置。

&emsp;&emsp;跑一下 dij 就可以知道最短长度了。

## H - Parentheses Editor 
&emsp;&emsp;没有 $-$ 操作的话就是 dp。有 $-$ 操作就回退一下状态就好了。

## I - One-Way Conveyors 
&emsp;&emsp;先边双缩一下点，然后就变成树的问题了。

&emsp;&emsp;剩下的定向相当于树上的路径赋值，因为只有最后一次查询，所以用倍增打标记就好了。

## K - Draw in Straight Lines 
&emsp;&emsp;网络流题，还没搞太懂，老大哥yyds!