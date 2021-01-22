## A - Relic Discovery
&emsp;&emsp;签到题

## B - Pocket Cube
&emsp;&emsp;小模拟题

## C - Pocky
&emsp;&emsp;列出期望的式子，两边求导，解一个微分方程就可以了。

## D - Lucky Coins
&emsp;&emsp;首先因为每个硬币的概率在 0.4 到 0.6 之间，所以就算有 1000000 个，持续到 100 轮的概率还是非常小的。设第 $i$ 种硬币的正面概率是 $p_i$，有 $a_i$ 个，那么在第 $n$ 轮全部被丢掉的概率是 $(1 - p_i^n) ^ {a_i}$，这个在 100 轮后是非常接近 1 的。

&emsp;&emsp;于是枚举第 $i$ 种硬币留到最后并且在第 $n$ 轮被全部丢掉，那么这个概率为 $((1 - p_i^{n + 1}) ^ {a_i} - (1 - p_i^n) ^ {a_i}) \times  \prod\limits_{j \neq i}(1 - p_{j}^n)^{a_j}$。

## G - Coding Contest
&emsp;&emsp;取对数就变成加法了，然后就是浮点数最小费用流，要加 eps

## J - Cliques
&emsp;&emsp;好像又是个乱搞题，搞不来，队长切了

