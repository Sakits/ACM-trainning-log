比赛链接：https://vjudge.net/contest/417318
## Problem A. Almost Balanced Tree
&emsp;&emsp;考虑递归解决这个问题。

&emsp;&emsp;如果 $2$ 的个数是奇数，那么把当前的根设为 $2$，然后 $b - 1$；如果 $2$ 的个数是偶数，那么把当前的根设为 $1$，然后 $a - 1$。

&emsp;&emsp;左儿子递归到 $(\frac{a}{2}, \frac{b}{2})$，右儿子递归到 $(a - \frac{a}{2}, \frac{b}{2})$ 的状态即可。

&emsp;&emsp;$-1$ 的情况就是当 $b$ 是偶数但是此时 $a$ 为 $0$ 时，这样必定导致两个子树的和之差大于 $1$。

## Problem B. Brain-teaser
&emsp;&emsp;高超的爆搜，不是我负责的题型。

## Problem C. Color the Tree
&emsp;&emsp;考虑构造一个方案。

&emsp;&emsp;首先每个子树都是子问题，可以递归处理。

&emsp;&emsp;得到子树的方案之后，把子树的方案从多到少排序，每次按这个顺序把新的子树的方案逐个合并进当前这个树的方案中。

&emsp;&emsp;考虑现在要加进一个新的子树，那么这个新的子树的方案中每操作一步，都可以把合并之前的树的方案正序或者倒序进行一次，并且这样就是序列最长的情况。

&emsp;&emsp;方案直接用 vector 暴力就行了，$n$ 才 $20$ 复杂度不会爆炸。

## Problem D. Down We Dig
&emsp;&emsp;暴力很容易想到，每次加进来一行然后重新求 sg 函数就行。但是这样复杂度是 $O(n^2)$ 的承受不了。

&emsp;&emsp;但是由于每个点只能转移到后 $8$ 行，所以实际上重复计算了很多的状态。当第 $[i,i + 7]$ 行的 sg 值确定了之后，sg[1] 也就是游戏的胜负就已经确定了。

&emsp;&emsp;所以可以设 $f[i][state]$ 表示当前在第 $i$ 行，并且 $[i, i + 7]$ 行的胜负状态是 $state$，然后记忆化一下就行了。复杂度 $O(300000 \times 8 \times 2 ^ 8)$

## Problem E. Easy Measurements
&emsp;&emsp;实际上就是求 $\frac{a}{b} + \frac{c}{d} = \frac{b}{d}$ 的 $a$ 、$c$ 正整数对数。

&emsp;&emsp;用类似 exgcd 的做法算就可以了。

## Problem G. Geometrical Combinatorics
&emsp;&emsp;好像是个组合 + 计算几何题。

&emsp;&emsp;计算几何不会，交给队友了。

## Problem I. Interactive Knockout
&emsp;&emsp;关键是要知道，如果设整个图有 $s$ 个位置，随机走几乎可以保证会在 $\frac{s}{3}$ 轮把自己走死，所以只要占领 $\frac{s}{3}$ 的位置就行了。

&emsp;&emsp;可以选择占左上角的平行四边形或者左下角的平行四边形。先走到 $(0, 0)$，如果此时对方在上半部分，那就占左下角的平行四边形，反之占左上角的。

## Problem K. Kate’s 2021 Celebration
&emsp;&emsp;签到题。

## Problem L. Lookup Performance
&emsp;&emsp;直接找到边界的两个点，$2\times(dep_a + dep_b - dep_{lca(a, b)}) + 1$ 就是答案了。

&emsp;&emsp;被对面的 __stdcall 说的树状数组套线段树搞了一手心态，最后没敢上去写。更搞心态的是 lzd 上机 A 的那发也写了个树状数组。以后莽就完事了。

## Problem M. Miser
&emsp;&emsp;签到题。