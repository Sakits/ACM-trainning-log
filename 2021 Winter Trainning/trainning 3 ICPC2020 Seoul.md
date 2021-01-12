## A - Autonomous Vehicle
&emsp;&emsp;因为 $n$ 只有 $500$，所以交点个数不超过 $25000$ , 先暴力模拟一遍回到原点，这时候可以得到循环节的时间，把所求时间对这个取模，再暴力模拟一遍即可。

## B - Commemorative Dice 
&emsp;&emsp;签到题。

## C - Dessert Café 
&emsp;&emsp;题意理解题。

&emsp;&emsp;不难发现只要作为根时至少有两个不同子节点的子树中存在 complex 点或者本身为 complex 点的点就是 good 的。

## E - Imprecise Computer 
&emsp;&emsp;细节题，讨论一下就好了。

&emsp;&emsp;首先可以去掉差值 $\geq 2$ 的那些比赛，视为只有 $i$ 和 $i + 1$ 比的比赛，记为第 $i$ 场。

&emsp;&emsp;第 $i$ 场比赛可以给 $|r_1(i) - r_2(i)|$ 和 $|r_1(i + 1) - r_2(i + 1)|$ 同时以 $0$ 或 $1$ 的贡献。

&emsp;&emsp;细节是没有第 $n$ 场比赛，需要仔细讨论。

## F - Ink Mix 
&emsp;&emsp;题意理解题 + 支配树板子题

## G - Mobile Robot 
&emsp;&emsp;机器人的相对位置不变，并且位置要么是整点要么是 0.5 的点，然后推推式子就完了。

## H - Needle 
&emsp;&emsp;可以直接 bitset 存下三行的位置，然后枚举中间行与上下两行点的横坐标之差，用 bitset 左右移然后 and 一下之后 1 的个数就是这个横坐标之差的答案了。

&emsp;&emsp;用 FFT 做也可以，而且会更快。

## I - Stock Analysis 
&emsp;&emsp;离线处理询问，询问按权值排序，节点也按权值排序把小于等于询问权值的区间加入数据结构。查询用二维树状数组处理，相当于询问区间 $l$ 大于等于询问区间 $l$， $r$ 小于等于询问区间 $r$ 的矩阵最大值，这些都是前后缀，所以可以用树状数组解决。

## J - Switches 
&emsp;&emsp;直接线性基，用 bitset 维护一下方案，复杂度 $O(\frac{500 ^ 3}{32})。$

## K - Tiling Polyomino 
## L - Two Buildings 
&emsp;&emsp;首先很容易发现，左端点一定是从左到右的严格上升序列中的点，右端点一定是从右到左的严格上升序列中的点，否则一定可以向左向右把左右端点扩展到这两个序列中的点。
&emsp;&emsp;一个比较难想到的性质：转移具有决策单调性，这个写个式子就能证明了。
&emsp;&emsp;设 $i < j < k < l$，只需要证明如果从 $j$ 转移到 $k$ 比从 $i$ 转移到 $k$ 优，那么 $i$ 转移到 $l$ 一定比 $j$ 转移到 $l$ 劣即可，也就是转移不能交叉。
&emsp;&emsp;有决策单调性就可以用分治来优化了。