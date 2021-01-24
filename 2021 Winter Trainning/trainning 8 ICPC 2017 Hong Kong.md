比赛链接：https://vjudge.net/contest/418309

这场都是十年脑血栓题，服了

## A - A
&emsp;&emsp;python / java 题，就离谱

## B - B
&emsp;&emsp;操作的顺序是无所谓的，直接扫描线 + 线段树就好了。

## C - C
&emsp;&emsp;小模拟，几个置换搞搞看看包不包含一不一样就好了

## D - D
&emsp;&emsp;直接 floyd

## E - E 
&emsp;&emsp;排序、二分、贪心

## F - F 
&emsp;&emsp;签到题

## G - G 
&emsp;&emsp;背包 dp + 贪心求方案 
&emsp;&emsp;trainning 6 有两道类似的题

## H - H
&emsp;&emsp;python / java 题，就离谱

## I - I 
&emsp;&emsp;python / java 题，就离谱

## J - J 
&emsp;&emsp;考虑三角形一定是一黑两白或者一白两黑，考虑其中一种怎么做就行了。

&emsp;&emsp;不妨设一黑两白，那么能组成三角形一定是黑的在其中一个白的距离 d 内，一个在距离 d 外。

&emsp;&emsp;考虑两个白点，两种方向的贡献分别是两个白点距离为 d 内部的黑点个数，所以只要把每个点距离为 d 内的黑点个数求出来就完了。

&emsp;&emsp;先把曼哈顿距离转成切比雪夫距离，然后按 x 排序，对 y 轴建线段树，把 x 轴范围 d 内的点加进线段树里，直接查 y 轴范围为 d 内的点数就行了。

&emsp;&emsp;然后每个点最大值就看看之前扫过的比自己多的黑点个数加进来，比自己小的就加自己，最小值就加比自己少的。

&emsp;&emsp;重合部分直接边算边统计然后减掉就行了，这个不影响大小关系。

## K - K
&emsp;&emsp;高超的搜索题。