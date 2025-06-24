**Въведение**

**1. Модел в пространство на състоянието**

&emsp;&ensp; $x_{k + 1} = \text{Ax}_{k} + \text{Bu}_{k} + w_{k}$, &emsp;&ensp; уравнение на състоянието (state equation)

&emsp;&ensp; $y_{k} = \text{Cx}_{k} + \text{Du}_{k} + v_{k}$. &emsp;&ensp; уравнение на изхода (observation equation)

**2. Връзка описанието в пространство на състоянието за SISO ARX модел**

За ARX($n,m$) модел

&emsp;&ensp; $y_k =  -a_1\,y_{k-1} - a_2\,y_{k-2} - \cdots - a_n\,y_{k-n}
+ b_0\,u_{k} + b_1\,u_{k-1} + \cdots + b_m\,u_{k-m} + e_k$

**2.1 Уравнение на състоянието (матрица $A$ и вектор $B$)**

&emsp;&ensp; $x_{k+1} = A\,x_k + B\,u_k + w_k$

където

&emsp;&ensp; $A = 
\begin{bmatrix}
0      & 1      & 0      & \cdots & 0      \\[6pt]
0      & 0      & 1      & \cdots & 0      \\[-2pt]
\vdots &        & \ddots & \ddots & \vdots \\[2pt]
0      & 0      & \cdots & 0      & 1      \\[6pt]
-\,a_n & -\,a_{n-1} & \cdots & -\,a_2 & -\,a_1
\end{bmatrix}$, 

&emsp;&ensp; $B =
\begin{bmatrix}
0 \\[3pt]
0 \\[3pt]
\vdots \\[3pt]
0 \\[3pt]
1
\end{bmatrix}$.

**2.2 Уравнение на изхода (матрица $C$ и скалар $D$)**

&emsp;&ensp; $y_k = C\,x_k + D\,u_k + v_k$,

където

&emsp;&ensp; $C = 
\begin{bmatrix}
b_m - b_0\,a_n,\; 
b_{m-1} - b_0\,a_{n-1},\;
\cdots,\;
b_1 - b_0\,a_{\,n-m+1}
\end{bmatrix}$,

(ако $m<n$, $C$ се допълва с нули до дължина $n$) и

&emsp;&ensp; $D = [\,b_0\,]$.

**3. На едно IO описание съществуват безброй описания в ПС**

**3.1 Преобразение на състоянието с матрица $T$**

Всяка реализация на модела в ПС се получава чрез трансформация на подобие

&emsp;&ensp; $z_k = T\,x_k$,

където $T\in\mathbb{R}^{n\times n}$ е обратима матрица. Тогава

&emsp;&ensp; $\begin{aligned}
z_{k+1}
&= T\,x_{k+1}
= T\,(A\,x_k + B\,u_k)
= (T\,A\,T^{-1})\,z_k \;+\; (T\,B)\,u_k,\\
y_k
&= C\,x_k + D\,u_k
= (C\,T^{-1})\,z_k \;+\; D\,u_k.
\end{aligned}$

**3.2 Нова реализация в ПС**

&emsp;&ensp; $\begin{aligned}
z_{k+1} &= A'\,z_k + B'\,u_k,\\
y_k     &= C'\,z_k + D'\,u_k.
\end{aligned}$

където

&emsp;&ensp; $A' = T\,A\,T^{-1},\quad B' = T\,B,\quad C' = C\,T^{-1},\quad
D' = D$.

С тези $A',B',C',D'$ се получава алтернативна реализация в ПС.


**4. Филтър на Калман**

ФК е инструмент за оценка на скритите състояниа в динамична система в условията на неопределеност в системата и в данните.

**Подготовка на данните за месец** *k*

**1. Формиране на рискови зони**

За всеки месец активните договори се групират в $n$ на брой групи
(рискови зони) според ${\hat{p}}_{j,k}$ по метода equal-ranges. Този
подход е unsupervised, но е възможно да се приложи supervised подход и
да се дефинира desired-risk за всяка зона.

Всеки клиент $j = \overline{1,N_{k}}$ попада в съответна зона $i$ според
${\hat{p}}_{j,k}$. Петте зони са: Low Risk, Low to Medium Risk, Medium
Risk, Medium to High Risk и High Risk.

**2. Статистики за рискови зони**

Наблюдаваната (емпирична) оценка на вероятността за добър платец в
$i$-ата зона e

&emsp;&ensp; ${\overline{p}}_{i,k} = \frac{1}{N_{i,k}}\sum_{j \in \text{bin}i}^{}p_{j,k}$.

Тази величина се използва за формиране на наблюдаваните log-odds

&emsp;&ensp; $y_{k}^{\left( i \right)} = \log\frac{\overline{p}_{i,k}^{\left( i \right)}}{1 - \overline{p}_{k}^{\left( i \right)}}$.

Така за текущия $k$-ти месец векторът на наблюденията е

&emsp;&ensp; $y_{k} = \left\lbrack y_{1,k}y_{2,k}\text{...}y_{n,k} \right\rbrack^{T}$.

**Модел в пространство на състоянието**

Описание в пространство на състоянието

&emsp;&ensp; $x_{k + 1} = \text{Ax}_{k} + \text{Bu}_{k} + w_{k}$, &emsp;&ensp; уравнение на
състоянието (state equation)

&emsp;&ensp; $y_{k} = \text{Cx}_{k} + \text{Du}_{k} + v_{k}$. &emsp;&ensp; уравнение на изхода
(observation equation)

Финално описание

В задачата:

&emsp;&ensp; $A = I_{n}$ - състоянието се изменя по случаен/стохастичен закон (random
walk)

&emsp;&ensp; $B = 0$ - няма външни фактори

&emsp;&ensp; $C = I_{n}$, $D = 0$

&emsp;&ensp; $x_{k + 1} = x_{k} + w_{k}$

&emsp;&ensp; $y_{k} = x_{k} + v_{k}$


**2. Въвеждане на адитивна нискочестотна компонента (тренд) в модела**

Нека $x_{t,k}$ е векторът на бавните изменения на log-odds по зони:

&emsp;&ensp; $x_{t,k} = \left\lbrack x_{t,1,k}\;x_{t,2,k}\;\text{...}\;x_{t,n,k} \right\rbrack^{T}$

Тогава, пълният вектор на състоянието, включващ неизмеримите log-odds по
зони и съответните им бавноизменящи се адитивни съставки е

&emsp;&ensp; $x_{k} \leftarrow \left\lbrack x_{k}^{T} \; x_{t,k}^{T} \right\rbrack^{T}$

Описание в пространство на състоянието

&emsp;&ensp; $x_{k + 1} = \text{Ax}_{k} + \text{Bu}_{k} + w_{k}$

&emsp;&ensp; $y_{k} = \text{Cx}_{k} + \text{Du}_{k} + v_{k}$

където

&emsp;&ensp; $A = \begin{bmatrix}
I_{n} & I_{n} \\
0_{n} & I_{n} \\
\end{bmatrix}$ - състоянието се изменя по случаен закон (random walk)
около адитивната бавноизменяща се (тренд) компонента

&emsp;&ensp; $B = 0$ - няма външни фактори

&emsp;&ensp; $C = \left\lbrack I_{n}0_{n} \right\rbrack$, $D = 0$

Финално описание

&emsp;&ensp; $x_{k + 1} = \text{Ax}_{k} + w_{k}$

&emsp;&ensp; $y_{k} = \text{Cx}_{k} + v_{k}$

**Филтър на Калман (обш вид)**

**1. Алгоритъм на филтъра на Калман**

1\. Корекция на оценката на състоянието &emsp;&ensp; $x_{k/k} = x_{k/k - 1} + K_{k}\left( y_{k} - y_{k/k - 1} \right)$

2\. Предсказване на състоянието и изхода &emsp;&ensp; $x_{k+1/k} = \text{Ax}_{k/k} + \text{Bu}_{k}$

&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp;&emsp;&ensp; $y_{k+1/k} = \text{Cx}_{k+1/k}$

3\. Предсказване на КМГ в оценката на състоянието &emsp;&ensp; $P_{k+1/k} = \text{AP}_{k}A^{T} + Q$

4\. Предсказване на КМГ на оценката на изхода &emsp;&ensp; „$S_{k + 1} = \text{CP}_{k+1/k}C^{T} + R$

5\. Усилване на филтъра (Калманово усилване) &emsp;&ensp; $K_{k + 1} = P_{k+1/k}C^{T}S_{k + 1}^{- 1}$

6\. Корекция на КМГ в оценката на състояниет о&emsp;&ensp; $P_{k + 1} = P_{k+1/k} - K_{k + 1}S_{k + 1}K_{k + 1}^{T}$

КМГ -- ковариационна матрица на грешката

**2. Извеждане на филтъра на Калман (вариант 1)**

Филтъра на Калман се търси от вида

&emsp;&ensp; $x_{k+1/k + 1} = A_{f}x_{k/k} + B_{f}u_{k} + \text{Ky}_{k + 1}$,

т.е. се търсят матриците $A_{f}$, $B_{f}$ и $K$. Матрицата $K$ се нарича
Калманово усилване.

Грешка в оценяването на състоянието е

&emsp;&ensp; $e_{k + 1} = x_{k + 1} - x_{k+1/k + 1}$.

Този израз може да се развие по следния начин

&emsp;&ensp; $\begin{matrix}
e_{k + 1} = x_{k + 1} - x_{k+1/k + 1} = \text{Ax}_{k} + \text{Bu}_{k} + w_{k} - A_{f}x_{k/k} - B_{f}u_{k} - \text{Ky}_{k + 1} = \text{...} = A_{f}e_{k} + h_{k} \\
\end{matrix}$ (0)

-- изисквания към ФК

1\) Неизместеност на оценките, т.е. $m_{e,k} = 0$

&emsp;&ensp; $m_{e,k + 1} = A_{f}\underset{0}{\overset{m_{e,k}}{\underbrace{}}} + m_{h,k}$,
(0.5)

Условието за неизместеност се изпълнява ако $m_{h,k} = 0$

където

&emsp;&ensp; $m_{h,k} = \left( A - A_{f} - \text{KCA} \right)\underset{. \neq 0}{\overset{m_{x,k}}{\underbrace{}}} + \left( B - B_{f} - \text{KCB} \right)\underset{. \neq 0}{\overset{u_{k}}{\underbrace{}}}$

За $A_{f}$ и $B_{f}$ се получава $A_{f} = \left( I - \text{KC} \right)A$
и $B_{f} = \left( I - \text{KC} \right)B$. В такъв случай уравнението на
филтъра добива вида

&emsp;&ensp;
$\begin{matrix}
x_{k+1/k + 1} = \left( I - \text{KC} \right)\text{Ax}_{k/k} + \left( I - \text{KC} \right)\text{Bu}_{k} + \text{Ky}_{k + 1} = \text{Ax}_{k/k} + \text{Bu}_{k} + K\left( y_{k + 1} - \text{CAx}_{k/k} - \text{CBu}_{k} \right)\text{.} \\
\end{matrix}$

Обновяващата формула за оценките добива вида

&emsp;&ensp; $x_{k+1/k + 1} = x_{k+1/k} + K\left( y_{k + 1} - y_{k+1/k} \right)$.

2\) Минимална дисперсия на оценките, т.е.
$\underset{K}{\text{min}}P_{k}$

*P~k~* е ковариационната матрица на грешката (КМГ). Отчитайки първото
условие, за (0) се получава

&emsp;&ensp; $e_{k + 1} = A_{f}e_{k} + \left( I - \text{KC} \right)w_{k} - \text{Kv}_{k + 1} = A_{f}e_{k} + n_{k}$,
(1)

където $n_{k} =$.

Ковариационната матрица $P_{k}$ е

&emsp;&ensp; $P_{k} = M\{ e_{k}e_{k}^{T}\}$

Нека $V_{n}$ е дисперсията на $n_{k}$. От (1) и поради това, че $e_{k}$
и $n_{k}$ са некорелирани се достига до диференчното уравнение на
Ляпунов

&emsp;&ensp; $P_{k + 1} = A_{f}P_{k}A_{f}^{T} + V_{n}$. (2)

Замествайки $A_{f}$ в (2) се получава

&emsp;&ensp; $P_{k + 1} = \left( I - \text{KC} \right)AP_{k}A^{T}\left( I - \text{KC} \right)^{T} + V_{n}$
(3)

Задачата за намиране на $K$, удовлетворяваща второто условие за
минимална дисперсия е трудна за решаване, защото се търси минимум на
матрична функция по отношение на матричен аргумент. Тази задача може да
се опрости, като $K$ се представи по следния начин

&emsp;&ensp; $K = K_{\text{opt}} + \alpha\overset{\sim}{K}$. (4)

Матрицата $K_{\text{opt}}$ е търсената, оптимална матрица на усилването
на ФК, $\overset{\sim}{K}$ е произволна, а $\alpha$ е скалар, по който
реално се извършва диференцирането. По този начин задачата

&emsp;&ensp; $\underset{K}{\text{min}}P_{k}$ се свежда до
$\underset{\alpha}{\text{min}}P_{k}$\|~α=0.

Изразът (4) за $K$ се замества в (3), равенството се диференцира по
$\alpha$, скаларът $\alpha$ се замества с 0 и така се получава

&emsp;&ensp; $K_{\text{opt}} = K_{k + 1} = P_{k+1/k}C^{T}\left( V_{v} + \text{CP}_{k+1/k}C^{T} \right)^{- 1} = P_{k+1/k}C^{T}S_{k + 1}^{- 1}$.

За $P_{k + 1}$ се получава

&emsp;&ensp; $P_{k + 1} = P_{k+1/k} - K_{k + 1}S_{k + 1}K_{k + 1}^{T}$

**2. Линеаризация с ред на Тейлър**

Представеният подход се базира на **разширения филтър на Калман**, приложим при **нелинейни модели в пространство на състоянието**. За целта се извършва апроксимация на нелинейните функции чрез **разлагане в ред на Тейлър от първи ред**.

Системата се описва чрез:

&emsp;&ensp; $x_k = f(x_{k-1}, u_{k-1}) + w_{k-1}$,

&emsp;&ensp; $y_k = h(x_k, u_k) + v_k$,

където:

* $x_k \in \mathbb{R}^n$ представлява състоянието в момент $k$,
* $u_k \in \mathbb{R}^m$ е управляващ вход,
* $y_k \in \mathbb{R}^r$ е наблюдението,
* $w_{k-1} \sim \mathcal{N}(0, Q)$ е системен шум,
* $v_k \sim \mathcal{N}(0, R)$ е шум в измерването.

---

### Линеаризация на модела

При наличие на нелинейност във функциите $f(\cdot)$ и $h(\cdot)$, се прилага разлагане в ред на Тейлър от първи ред около предварително оцененото състояние $\bar{x}_k$, прието като прогноза за $x_k$ в момент $k$.

---

#### Апроксимация на $f(x_k, u_k)$:

&emsp;&ensp; $f(x_k, u_k) \approx f(\bar{x}_k, u_k) + \frac{\partial f}{\partial x} \bigg|_{\bar{x}_k, u_k} (x_k - \bar{x}_k) + \frac{\partial f}{\partial u} \bigg|_{\bar{x}_k, u_k} (u_k - u_k)$

Тъй като $(u_k - u_k) = 0$, съответният член се елиминира. Въвеждат се означения:

&emsp;&ensp; $A = \left. \frac{\partial f}{\partial x} \right|_{\bar{x}_k, u_k}, \quad B = \left. \frac{\partial f}{\partial u} \right|_{\bar{x}_k, u_k}$

Получава се линейна аппроксимация:

&emsp;&ensp; $f(x_k, u_k) \approx f(\bar{x}_k, u_k) + A (x_k - \bar{x}_k)$

...


#### Апроксимация на $h(x_k, u_k)$:

&emsp;&ensp; $h(x_k, u_k) \approx h(\bar{x}_k, u_k) + \frac{\partial h}{\partial x} \bigg|_{\bar{x}_k, u_k} (x_k - \bar{x}_k) + \frac{\partial h}{\partial u} \bigg|_{\bar{x}_k, u_k} (u_k - u_k)$

И тук $(u_k - u_k) = 0$, поради което остава:

&emsp;&ensp; $C = \left. \frac{\partial h}{\partial x} \right|_{\bar{x}_k, u_k}, \quad D = \left. \frac{\partial h}{\partial u} \right|_{\bar{x}_k, u_k}$

Следователно:
&emsp;&ensp; $h(x_k, u_k) \approx h(\bar{x}_k, u_k) + C (x_k - \bar{x}_k)$


### Линеен модел след апроксимацията

След извършената линеаризация, моделът приема линейна форма:

&emsp;&ensp; $x_{k+1} = A x_k + B u_k + w_k$

&emsp;&ensp; $y_k = C x_k + D u_k + v_k$

Тази форма позволява прилагане на стандартния филтър на Калман. Матриците $A$, $B$, $C$, $D$ се изчисляват числено във всяка итерация на базата на текущата оценка $\bar{x}_k$.


**Означения**:

&emsp;&ensp; $i$ &emsp;&ensp; индекс на текущата рискова зона

&emsp;&ensp; $j$ &emsp;&ensp; индекс на активен договор

&emsp;&ensp; $k$ &emsp;&ensp; индекс на текущ месец

&emsp;&ensp; $m$ &emsp;&ensp; брой входни въздействия (exogenous inputs)

&emsp;&ensp; $n$ &emsp;&ensp; брой състояния

&emsp;&ensp; $p_{j,k}$ &emsp;&ensp; вероятност за добър платец (бинарна величина) според текущото
поведение на платеца по $j$-тия договор в месец $k$

&emsp;&ensp; ${\hat{p}}_{j,k}$ &emsp;&ensp; прогноза от модел на вероятността за добър платец по
$j$-тия договор в месец $k$

&emsp;&ensp; $r$ &emsp;&ensp; брой изходи (measurements/observations)

&emsp;&ensp; $x_{k}$ &emsp;&ensp; вектор на състоянието (*state vector*) в $k$-тия момент, $x_{k} \in {\mathbb{R}}^{n}$; неизмерими (истински) log-odds по зони описващи скрития поведенчески риск на клиентите в месец $k$

&emsp;&ensp; $x_{k + 1/k}$ &emsp;&ensp; прогнозирано състояние за месец $k + 1$ на базата
на информацията до $k$-тия момент, $x_{k+1/k} \in {\mathbb{R}}^{n}$

&emsp;&ensp; $x_{k/k}$ &emsp;&ensp; коригирано състояние в $k$-тия дискретен момент на
базата на постъпилите данни в $k$-тия момент, $x_{k/k} \in {\mathbb{R}}^{n}$

&emsp;&ensp; $u_{k}$ &emsp;&ensp; вектор на входните въздействия (exogenous input vector), $u_{k} \in {\mathbb{R}}^{m}$; в задачата не са въведени такива величини

&emsp;&ensp; $v_{k}$ &emsp;&ensp; шум в наблюдението (measurement/observation noise), $v_{k} \sim N\left( 0_{r \times 1},R \right)$; неопределеност зависеща от конкретните изтеглени заеми и обслужването им

&emsp;&ensp; $w_{k}$ &emsp;&ensp; системен шум (system/process noise) $w_{k} \sim N\left( 0_{n \times 1},Q \right)$; drift на log-odds

&emsp;&ensp; $y_{k}$ &emsp;&ensp; вектор на наблюдението (observation vector), $y_{k} \in {\mathbb{R}}^{r}$; наблюдавани (емпирични) log-odds за месец $k$, $y_{k} \in {\mathbb{R}}^{n}$

&emsp;&ensp; $y_{i,k}$ &emsp;&ensp; наблюдавани (емпирични) log-odds в $i$-тата рискова зона

&emsp;&ensp; $A$ &emsp;&ensp; преходна матрица на състоянието(state transition matrix), $A \in {\mathbb{R}}^{n \times n}$

&emsp;&ensp; $B$ &emsp;&ensp; матрица на входните въздействия (exogenous input matrix), $B \in {\mathbb{R}}^{n \times m}$

&emsp;&ensp; $C$ &emsp;&ensp; матрица на наблюдението (observation matrix),
$C \in {\mathbb{R}}^{r \times n}$

&emsp;&ensp; $D$ &emsp;&ensp; пряка матрица на входните въздействия (feedthrough matrix или direct
transmission matrix), $D \in {\mathbb{R}}^{r \times m}$

&emsp;&ensp; $N_{k}$ &emsp;&ensp; брой активни клиенти в месец $k$ ($N_{k} \approx 10^{5}$)

&emsp;&ensp; $N_{i,k}$ &emsp;&ensp; брой клиенти в зона $i$ в месец $k$

&emsp;&ensp; $Q$ &emsp;&ensp; матрица на системния шум (system/process noise covariance matrix) $Q \in {\mathbb{R}}^{n \times n}$
&emsp;&ensp; $R$ &emsp;&ensp; ковариационна матрица на шума в измерването (measurement noise covariance matrix) $Q \in R^{n \times n}$

