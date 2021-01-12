## A - Autonomous Vehicle
&emsp;&emsp;因为 $n$ 只有 $500$，所以交点个数不超过 $25000$ , 先暴力模拟一遍回到原点，这时候可以得到循环节的时间，把所求时间对这个取模，再暴力模拟一遍即可。

## B - Commemorative Dice 
&emsp;&emsp;签到题。

## C - Dessert Café 
&emsp;&emsp;题意理解题。

&emsp;&emsp;不难发现只要作为根时至少有两个不同子节点的子树中存在 complex 点或者本身为 complex 点的点就是 good 的。

## E - Imprecise Computer 
## F - Ink Mix 
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