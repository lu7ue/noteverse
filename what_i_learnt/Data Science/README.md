## 1. Introduction to Data Science & AI (数据科学与AI导论)
### 1.1 Analytics Types (分析类型)
- **Descriptive & Diagnostic (描述性与诊断性)**: Describe the **past**  
  描述**过去**
- **Predictive & Prescriptive (预测性与规范性)**: Describe the **future**  
  描述**未来**

### 1.2 AI Objectives (AI目标)
#### Narrow AI (狭义AI)
- Automates processes (流程自动化)
- Improves decision-making (优化决策)
- Builds productivity tools (生产力工具)
- Works with **available data** (使用已有数据)
- Focused on **specific tasks** (专注于特定任务)
- Core functions: 
  - Pattern recognition (模式识别)：Recommendation systems (推荐系统), facial recognition (人脸识别)
  - Prediction (预测)：maintenance (维护), demand forecasting (需求预测)
  - Content generation (内容生成)：ChatGPT, Copilot, DALL·E

#### AGI (通用人工智能)
- Performs any human task (执行人类级任务)
- Solves novel problems (解决新问题)
- Shows creativity/common sense (创造力/常识)
- Matches/exceeds human flexibility (匹敌或超越人类的灵活性)

| Narrow AI 狭义AI | AGI 通用AI |
|---|---|
| Task-specific (特定任务) | Cross-domain (跨领域任务) |
| Based on past data (基于历史数据) | Can handle novelty (能处理新情况) |
| Pattern recognition (模式识别) | Pattern interpretation & reasoning (模式解释与推理) |
| Increases efficiency (提高效率) | Matches/exceeds human flexibility (匹敌或超越人类的灵活性) |

> Adding complexity or data ≠ more intelligence  增加复杂性或数据 ≠ 增强智能  
> Intelligence requires reasoning beyond seen data  智能需要超越已知数据的推理能力  

## 2. Business Understanding (业务理解)
### 2.1 Core Elements (核心要素)
| Concept | Description 描述 |
|---|---|
| Business Objective | Organization's primary goal 商业目标 (e.g., 提高客户满意度) |
| Business Success Criteria | KPIs for objective achievement 商业目标成功标准 (e.g., 满意度提升10%) |
| Data Mining Goal | Technical objectives for data scientists 数据挖掘目标 (e.g., 预测电影受欢迎度) |
| Data Mining Success Criteria | Metrics for model performance 数据挖掘成功标准 (e.g., 准确率90%) |

#### Key Questions (关键问题)
- **Business Objective**: What is the organization trying to achieve?  
  组织试图实现什么？
- **Business Success Criteria**: When is that considered successful?  
  什么情况下认为目标达成？（明确KPI）
- **Data Mining Goal**: How can data science help?  
  数据科学如何提供帮助？
- **Data Mining Success Criteria**: When is the data science effort successful?  
  如何判断数据科学工作是否成功？（明确准确率或RMSE等）

### 2.2 Baseline Models & Success Criteria (基线模型与成功标准)
#### Why use a baseline model? (为何需要基线模型)
- Understand your data performance (了解数据的基本表现)
- Identify data or modeling issues (发现数据或建模中存在的问题)
- Faster iterations with simpler models (使用简单模型可以更快速地迭代)
- Interpretable results for stakeholders (提供可解释的结果给相关方参考)
- Provide a fair benchmark for advanced models (为高级模型提供一个公平的对比基准)

#### How to define Data Mining Success Criteria? (如何定义数据挖掘成功标准)
Use one or more of the following methods:  
使用以下一种或多种方法：
- **Relative improvement over baseline** (相对基线改进): "15% improvement over mean prediction"  
  "比均值预测提升15%"
- **Business impact as a metric** (业务影响指标): "10% waste reduction = €500 savings/month"  
  "减少10%浪费=每月节省500欧元"
- **Industry/regulatory benchmarks** (行业或法规标准): "False negatives < 5% when predicting disease"  
  "疾病预测中漏报率<5%"
- **Statistical significance** (统计显著性标准): "Improve math scores by +6 points to be beyond ±3 point fluctuation"  
  "数学成绩提高6分以超出±3的自然波动范围"

## 3. Data Understanding (数据理解)
### 3.1 Data Fundamentals (数据基础)
- **Data Definition**: Facts/statistics conveying information, structured or unstructured  
  事实/统计数据，结构化或非结构化
- **Dataset Structure**:  
  Rows = observations/target (行=观察值/目标)  
  Columns = variables/features (列=变量/特征)

> Facts / Statistics 事实 / 统计数据：Basic pieces of information or measurements collected from observations. 从观察或测量中收集到的基本信息，比如温度、销售额、浏览次数等。
> Structured data 结构化数据：Organized in a clear format like rows and columns (e.g., Excel, databases). 以固定格式组织的数据，如表格、数据库中的行列数据，容易存储和分析。
> Unstructured data 非结构化数据：Not organized in a predefined way, harder to analyze (e.g., text, images, videos). 没有固定格式的数据，比较难直接分析，比如一篇文章、一张照片、一个视频等。

### 3.2 Preliminary Data Inspection (初步数据检查)
- Data types and structure (e.g., numerical, categorical)  
  数据类型与结构（数值型、分类型等）
- Variable distributions (check for normality)  
  变量分布（是否符合正态分布）
- Correlations between variables  
  变量之间的相关性
- Missing values  
  缺失值
- Is the dataset suitable for modeling? What are the potential issues?  
  是否适合建模？有哪些潜在问题？

> How to judge if a dataset is suitable for modeling? 如何判断数据是否适合建模？
>> 1. Data completeness 数据完整性: Too many missing values can harm model accuracy. 缺失值太多会严重影响模型的准确性。
>> 2. Data quality 数据质量: Are there errors, duplicates, or unrealistic values? 是否有错误、重复、或不合理的数值？比如“年龄 = -5”就是异常。
>> 3. Variable types and structure 变量类型与结构: Are variable types correct? (e.g., no numbers stored as text) 变量类型是否正确？比如不要把数字当成文字存储。
>> 4. Sufficient data volume 数据量是否够: Too few samples can lead to overfitting or unstable results. 样本太少容易导致过拟合或结果不稳定。
>> 5. Variable distribution 变量分布: Highly skewed or non-normal distributions may need transformation. 偏斜严重或不符合正态分布的变量可能需要转换（如对数转换）。
>> 6. Correlation and multicollinearity 相关性与多重共线性: Too much correlation between predictors can confuse the model. 如果自变量之间高度相关，模型可能难以判断哪个更重要。
>> 7. Target variable balance 目标变量的平衡性: In classification tasks, check if classes are balanced. 分类问题中，如果某一类远多于其他类，模型可能偏向多数类。

> Potential issues 潜在问题总结：
>> Too many missing values 缺失值太多
>> Wrong data types 数据类型错误
>> Outliers 异常值
>> Class imbalance 类别不平衡
>> Multicollinearity 多重共线性
>> Low variance features 特征无变化（没信息）
>> Irrelevant features 无关特征

### 3.3 Distributions & Transformation (分布与变换)
#### Purpose (目的)
Understand the shape, skewness, and normality of variables.  了解变量的形状、偏态、是否符合正态分布

#### Visualization methods (可视化方法)
- Histogram (直方图): shows frequency of numerical variables  展示数值型变量的频率分布
- Bar plot (柱状图): compares grouped categorical values  分组（分类变量）与其数值比较
- Boxplot (箱线图): shows central tendency, distribution, and outliers  展示集中趋势、分布、离群值

#### Handling Non-Normal Distributions (非正态分布处理)
- Apply **log transformation**: suitable for right-skewed data, reduces tail length and outlier influence  采用对数变换：适用于右偏变量，拉近尾部，减少极端值影响
- Consider using **non-linear models**  或者使用非线性模型

> Why handle non-normal distributions? 为什么要处理非正态分布？ 
>> Because some models assume normality, and non-normal data can hurt performance. 因为某些模型假设数据是正态分布的，非正态数据可能影响模型效果。

> Do variables have to be normally distributed? 建模时变量一定要正态分布吗？
>> Not always. It depends on the model. 不一定，要看用什么模型。

> 为什么对数变换（Log transformation）常用？
>> Reduces right skew 减少右偏
>> Compresses large values 压缩极端大值
>> Improves linearity 更容易建立线性关系

<div align="center">
  <img src="https://github.com/user-attachments/assets/5cc5a3e7-8b79-4c4e-a759-8fa7e32cfab4" width="600"><br>
  <p><a href="https://medium.com/geekculture/what-are-right-skewed-and-left-skewed-distributions-a29b3def7598">数据分布图</a></p>
</div>

> 右偏（正偏）数据分布尾部在右侧，极大值拉高了均值，导致分布不对称。对数变换可压缩大值，拉近极大值与其他值，从而使分布更对称。
> 左偏（负偏）分布尾部在左侧，数据集中在高值区域，对数变换会放大差异，反而可能使分布更偏。因此通常不对左偏做对数变换。对于左偏，可以考虑反转后再对数变换或使用其他变换（如平方或 Box-Cox 变换）。

### 3.4 Outlier Detection (异常值检测)
#### Purpose (目的)
Identify and handle extreme values that may bias the model.  识别和处理异常点，避免其对模型产生不当影响

#### Detection methods (检测方法)
- **Boxplot method**:  
  Lower bound = Q1 - 1.5 × IQR  
  Upper bound = Q3 + 1.5 × IQR
- **Z-score method**:  
  Z = (x - mean) / standard deviation  
  Z < -3 or Z > 3 is considered an outlier

> x = A specific data point (observation) 某个样本数据点

```
如果你有一个变量「身高」，比如：
mean = 170 cm
std = 10 cm
一个人的身高 x = 190 cm

那么他的 Z-score 就是：
Z = (190 - 170) / 10 = 2 → 表示比平均值高了2个标准差。
```

#### Handling strategies (处理策略)
- Investigate cause: data entry error or device malfunction?  调查原因：是否为录入错误或设备异常
- Delete: only if clearly erroneous  删除：仅限于明确为错误数据
- Retain: if it's a meaningful extreme value  保留：如果是有意义的极端值
- Important: document all changes to avoid introducing bias  重要：记录所有修改操作，避免引入偏差

> Outlier ≠ Error — always investigate the reason.  
> 离群值 ≠ 错误，一定要调查原因

### 3.5 Feature Scaling (特征缩放)
#### Purpose (目的)
Bring variables to a similar scale for better convergence and fair influence in models.  让变量在相似尺度上，有利于建模收敛、避免某变量主导模型

#### Common scaling methods (常用缩放方法)
| Method | Description 描述 | Suitable scenarios 适用场景 |
|:---:|:---:|:---:|
| StandardScaler | Mean = 0, Std = 1 (Z-score standardization)<br>均值为0，标准差为1（Z-score标准化） | Linear models, neural networks<br>线性模型、神经网络 |
| MinMaxScaler | Rescales values to [0, 1] range<br>所有值压缩到[0,1]区间 | Image processing, interpretable scales<br>图像处理、需要恢复业务单位的模型 |
| RobustScaler | Based on IQR, resistant to outliers<br>基于IQR，抗离群点 | Data with many outliers<br>数据有大量离群值时 |

```
[10, 20, 30, 40, 1000]（最后一个是离群值）

1. StandardScaler（标准化）：数据变成以0为中心，但离群值影响很大
Z-score：每个值减去均值，再除以标准差
mean = 220
std ≈ 429.7
结果（近似）：[-0.49, -0.47, -0.44, -0.42, 1.81]

2. MinMaxScaler（最小最大缩放）：所有数据在 0 到 1 之间，但小数据差异很小，容易被忽略
压缩到 [0, 1] 区间
min = 10, max = 1000
结果：[0, 0.010, 0.021, 0.032, 1]

3. RobustScaler（稳健缩放）：中间的值被很好压缩，离群值不会拉偏整个缩放
用中位数和IQR（Q3 - Q1）代替均值和标准差，减少离群值影响
median = 30
Q1 = 20, Q3 = 40 → IQR = 20
结果：[-1.0, 0.0, 0.5, 1.0, 48.5]
```

#### Important Notes (重要注意事项)
- Always scale based on **training set only** to avoid data leakage  缩放应仅基于训练集，以防数据泄露
- Do **not** scale binary variables or categorical variables  不要对二元变量或分类变量缩放
- Scaling is **not needed** for tree-based models  树模型不需要缩放

### 3.6 Correlation & Multicollinearity (相关性与多重共线性)
#### Purpose (目的)
Understand relationships between variables and identify redundancy.  理解变量之间的关系，判断模型输入是否冗余

#### Correlation metrics (相关性指标)
| Metric | Description | Notes |
|:---:|:---:|:---:|
| Pearson's r | Measures linear correlation [-1, 1]<br>线性相关性，值在[-1,1]之间 | Most common; for continuous variables<br>最常用，适用于数值型变量 |
| Spearman's ρ | Measures monotonic rank correlation<br>单调关系的秩相关 | Captures non-linear monotonic patterns<br>可捕捉非线性单调关系 |
| Distance corr. | Captures all types of dependencies<br>衡量所有类型的相关性 | Powerful but harder to interpret<br>更强但不易解释 |

> Tip: Always use scatter plots to visually confirm correlation.  总是可视化（如散点图）来验证相关性是否合理

#### Multicollinearity (多重共线性)
**Problems (问题)**:
- Unstable coefficients, difficult to interpret  系数不稳定，解释困难
- Poor generalization  模型泛化能力下降

> Coefficient 系数：在回归模型中，系数表示每个变量对结果的影响大小。In regression, a coefficient shows how much a variable affects the output. 即每个变量对预测结果的影响程度。
>> 例如：如果“工资 = 2000 + 500 × 年龄”，那 500 就是年龄的系数。

> Generalization 泛化能力: 模型在新数据上的表现能力，而不是只在训练数据上好看。How well a model performs on new, unseen data — not just training data.
>> 如果模型在训练集上100分，但新数据只有60分，那就是泛化能力差。

**Detection (检测)**:
- Correlation heatmap  相关系数热图
- Variance Inflation Factor (VIF): VIF > 5 or 10 indicates high multicollinearity  方差膨胀因子：VIF>5或10表示高度多重共线性

> Variance Inflation Factor (VIF) 方差膨胀因子: 用来发现变量间的重复性，VIF高说明共线性严重。Measures how much a variable is correlated with other predictors. 
>> VIF > 5（或10）说明这个变量和其他变量高度重复，信息冗余。
>> VIF 越大，说明模型对这个变量的“信心”越不稳定。

**Solutions (解决方案)**:
- Drop one variable (choose less relevant or meaningful)  删除其中一个变量（选择更弱相关、含义更弱者）
- Combine variables (e.g., average or use PCA)  合并变量（例如平均值、主成分分析等）
- Apply regularization methods (e.g., Ridge or Lasso regression)  使用正则化方法（如Ridge或Lasso回归）

> Principal Component Analysis (PCA) 主成分分析：把多个相关变量合并为少量代表性变量，减少维度。Combines several correlated variables into fewer, uncorrelated components.
>> 比如你有“身高、腿长、胳膊长”三个相关变量，PCA 可以合成一个“体型因子”。

> Regularization 正则化：A method to prevent overfitting by shrinking large coefficients. 防止模型过拟合的一种方法，惩罚“太大”的系数。降低过拟合，提升模型稳定性和解释性。具体解释可以查看 ch5.5 多重共线性。
>> Ridge Regression (L2 正则化)：Penalizes the square of coefficients, keeping all but shrinking them. 惩罚系数的平方，倾向于让每个变量“都保留，但变小”。
>> Lasso Regression (L1 正则化)：Penalizes the absolute value, some coefficients shrink to zero — good for feature selection. 惩罚系数的绝对值，可以让一些系数变成0，实现变量选择。

## 4. Data Preparation (数据准备)
### 4.1 Data Cleaning (数据清洗)
| Error Type | Examples | Handling 处理 |
|---|---|---|
| Typos | "Asmterdam" → "Amsterdam" | `str.replace()` 字符串替换 |
| Duplicates | Same data in multiple rows | `drop_duplicates()` 删除重复值 |
| Missing Values | NaN/Null entries | Imputation techniques 填补技术 |
| Inconsistent Formats | DD-MM-YYYY vs MM-DD-YYYY | Standardization 标准化 |
| Unit Mismatches | Meters vs kilometers | Recalculation 重新计算 |

### 4.2 Missing Value Handling (缺失值处理)
#### Types of Missingness (缺失类型)
| Type | Description | Example 示例 |
|---|---|---|
| MCAR | Missing Completely at Random | Hardware failure 硬件故障导致数据丢失 |
| MAR | Missing At Random (related to other variables) | Young people hide screen time 年轻人不愿报告屏幕时间 |
| MNAR | Missing Not At Random (related to itself) | Heavy drug users hide usage 重度吸毒者隐瞒使用频率 |

#### Why It Matters (为何重要)
- May introduce bias (会引入偏差)
- Reduces statistical power (降低统计效能)
- Affects model training (影响模型训练)

#### Imputation Methods (填补方法)
| Method | When to Use | Advantages | Disadvantages | 优缺点 |
|---|---|---|---|---|
| Deletion (`dropna`) | MCAR | Simple | Information loss | 简单但丢失信息 |
| Mean/median imputation | MCAR/MAR | Fast | Distorts distribution | 快速但扭曲分布 |
| Forward/backward fill | Time series | Preserves trends | Not for abrupt changes | 保持趋势但不适用突变 |
| Hot/cold deck imputation 热/冷计算 | Similar values available | Preserves distribution | May introduce bias | 保持分布但可能引入偏差 |
| Interpolation 插值 | Trend data | Multiple methods | Not for jumpy data | 多种方法但不适用跳跃数据 |

### 4.3 Feature Engineering (特征工程)
Feature engineering = 提取或转换变量，让模型更容易学到规律  Feature engineering means creating or modifying variables to help models learn better.
只要原始数据不能直接用于建模，或者建模效果不好，就要考虑做特征工程。If raw features don’t work well in models, or need transformation to be useful—do feature engineering.

#### Binning (分箱)
Convert continuous to categorical  连续变量→分类变量  
连续变量对模型影响不线性，或模型用分类变量更稳定时（如决策树、逻辑回归） Use when continuous variables have unclear effect or we want easier interpretation
举例：把年龄分成“青年、中年、老年”三类；把风速分成“低、中、高”

#### Lag Features (滞后特征)
Use past observations as new features  将过去的观测值作为新特征  
- Lag 1 = yesterday's value (昨天的值)  
- Lag 7 = same day last week (上周同一天的值)

时间序列数据中，过去的值会影响当前值时使用 Use when past values affect the current value (typical in time series)
举例：今天的气温可能受到昨天或一周前气温的影响；特征股市、天气、销售额常用

#### Encoding (编码)
分类变量（字符串）不能直接喂进模型，要先“变成数字”。编码使模型能处理字符串。
| Method | Usage 适用模型 | Python Tools |
|---|---|---|
| One-hot | Non-linear models 非线性模型 | `pd.get_dummies(df['颜色'])` |
| Dummy | Linear models 线性模型 | `pd.get_dummies(df['颜色'], drop_first=True)` |

```
颜色: 红，绿，蓝  

1. One-hot 编码（用于非线性模型）：每个颜色变成一个独立的列，用 1 表示该样本是这个颜色，0 表示不是。
颜色 | 红列 | 绿列 | 蓝列
红 | 1 | 0 | 0
绿 | 0 | 1 | 0
蓝 | 0 | 0 | 1
使用场景：决策树、随机森林、神经网络；
缺点：维度变多（尤其类别多时）

2. Dummy 编码（用于线性模型）：和 One-hot 类似，但会丢掉一个列（比如“蓝”），防止虚拟变量陷阱（dummy variable trap）——也就是多重共线性。蓝色是“基准组”，它不需要列，模型把它当作默认状态。
颜色 | 红列 | 绿列
红 | 1 | 0
绿 | 0 | 1
蓝 | 0 | 0
使用场景：线性回归、逻辑回归等
```

> 为什么one-hot不适合线性？因为从例子中可以看出，三列之和恒等于 1（1+0+0=1） → 线性相关 → 多重共线性 → 回归模型出错或不稳定。而dummy因为丢弃了一列，使蓝列不会等于1，这就没有线性依赖关系了，因此dummy适合线性模型。

### 4.4 Data Merging (数据合并)
| Join Type | Description | Use Case |
|---|---|---|
| Inner | Only matching keys | Key intersection 键值交集 |
| Left | All left + matching right | Keep all left table 保留左表全量 |
| Right | All right + matching left | Keep all right table 保留右表全量 |
| Full | All rows + NaN | Full data 全量数据 |

<div align="center">
  <img src="https://github.com/user-attachments/assets/85ea1431-f5fa-43ff-926b-edc48f24c5f1" width="600"><br>
  <p><a href="https://datacomy.com/data_analysis/pandas/merge/">合并策略</a></p>
</div>

### 4.5 Data Quality Principles (数据质量原则)
- **Independence (独立性)**: Observations not influencing each other  观测值相互独立 (e.g., 避免重复行)
- **Representativity (代表性)**: Dataset reflects population  数据集代表总体 (e.g., 检查子群体缺失)

## 5. Modeling (建模)
> **Note**: For unsupervised learning (clustering, dimensionality reduction), see Chapter 7.  无监督学习内容（聚类、降维等）详见第7章。

### 5.1 Model Selection Framework (模型选择框架)
- **Supervised Learning (监督学习)**:
  - Regression (回归): Continuous target (连续目标值)
  - Classification (分类): Categorical target (分类目标值)
- **Unsupervised Learning (无监督学习)**:
  - Clustering (聚类): Group similar observations (分组相似观测值)

#### Machine Learning Flow (机器学习流程)
**Question**: Is labeled data available or can a target value be generated?  是否有标注数据或可以生成目标值？

**Yes → Supervised Learning (监督学习)**  
- **Regression**: Predict continuous values (e.g., housing price)  预测连续数值（如房价）
- **Classification**: Predict categories (e.g., spam detection)  预测类别（如垃圾邮件识别）

**No → Unsupervised Learning (无监督学习)**  
- **Clustering**: Grouping data without target values (e.g., customer segmentation)  将数据分组，无需目标值（如客户分群）

### 5.2 Modeling Assumptions & Feature Selection (建模假设与特征选择)

#### Modeling Assumptions (建模假设)
建模前要确保：样本能代表整体（不偏），每行数据互不影响，来自同样规律。Ensure the sample is representative, rows are independent, and follow the same underlying pattern.
- **Representative (代表性)**: Samples should represent the overall population  样本应能代表总体
- **IID (Independent and Identically Distributed)**: Each row should be independent and from the same distribution  每行数据应独立，且来自相同分布

> 什么是样本？What is a sample?
>> 样本 = 从总体（Population）中抽出来的一小部分数据，用来做分析和建模。A sample is a subset of the population, used for analysis and modeling.
>> 举例：你要研究“荷兰所有超市的销售情况”，但拿不到全部数据，你就抽100家超市的数据，这100家就是“样本”。

> 为什么样本要有代表性？Why must the sample be representative?
>> 因为我们用样本来“推测”总体，如果样本偏了，模型学到的规律就不准确。If the sample is biased, the model won’t reflect the real-world patterns in the population.
>> 比如只采集阿姆斯特丹的超市 → 无法代表荷兰全国 → 模型预测会偏差

> 异常值（Outliers）是个别极端情况，代表性是整体样本是否覆盖全面 Outliers are rare/extreme values, while representativeness is about overall coverage of population.

> 什么是 IID？(Independent and Identically Distributed)
>> 每一行数据必须是彼此独立的，而且都来自相同的规律或分布。Each row must be independent and follow the same distribution/rules.

| 数据              | 是否 IID | 为什么         |
| --------------- | ------ | ----------- |
| 顾客每天独立下单        | 是    | 每一单之间没有影响   |
| 同一个人连续下单        | 否    | 不独立，一个人行为相关 |
| 一半数据来自超市，一半来自工厂 | 否    | 不是同一分布，规律不同 |

#### Row-Level (行层面)
- **Measurement Level (测量水平)**: Types of variables (e.g., numerical, categorical)  变量类型（数值型、类别型等）
- **Distribution (分布)**: Variable distribution (e.g., skewness, outliers)  变量的分布形态（是否偏态、是否有异常值）

#### Column-Level (列层面)
- **Relationships (变量关系)**: Correlations between features and with target  特征之间、特征与目标之间的相关性

### 5.3 Data Type Recognition (数据类型识别)
识别数据的“结构类型”，判断它们是否独立、有自相关，还是分组相关。不同的数据结构，需要用不同的建模方法。

> Detection: Combine dataset purpose + visualization
>> 散点图 scatterplot：看变量间趋势
>> 自相关图 autocorrelation plot：看是否“前后相关”

- **Independent Data (独立数据)**: Observations are unrelated (e.g., random sampling)  观测值之间无关联（如随机抽样）
- **Autocorrelation (自相关)**: Nearby data in time or space are more similar (e.g., temperature)  时间或空间上相近的数据更相似（如温度）
- **Intraclass Correlation (类内相关)**: Correlation within groups (e.g., experimental groups)  组内数据相关（如实验组）

| 类型                      | 举例           | 建模方法要注意              |
| --------------------------| ------------ | -------------------- |
| **Independent** 独立数据            | 顾客满意度调查，每人一次 | 可直接使用普通回归            |
| **Autocorrelation** 自相关（时间或空间）| 今天和昨天温度      | 需用时间序列模型，如ARIMA      |
| **Intraclass Correlation** 类内相关（分组）| 学生 → 按班级分组   | 需用分层模型（mixed models） |

> 类内相关系数（Intraclass Correlation, ICC）到底是什么？ICC 衡量的是：同一组内的数据相比于组间差异的“相似程度”。
>> 通俗讲：同一组里的观测值是否“很像”？如果组内差异小、组间差异大 → ICC 高（接近 1）；如果组内差异大、组间差异小 → ICC 低（接近 0）
>> 它的取值范围是0～1，越接近 1 组内越一致。ICC 是判断“同一组”成员是否一致的指标，它是专门用于“组”的“相关性”。

### 5.4 Autocorrelation & Trend Visualization (自相关与趋势可视化)
#### Autocorrelation (自相关)
- Measures similarity between time series and its lagged version  衡量时间序列与其滞后版本的相似性
- Bars outside confidence interval → Significant autocorrelation exists  条形图落在置信区间外 → 存在显著自相关

#### Trend Visualization (趋势可视化)
| Visualization | Purpose 用途 |
|---|---|
| Histogram 直方图 | Shows frequency of numerical variables 展示数值型变量的频率分布 |
| Bar plot 条形图 | Compares grouped categorical values 比较分类变量组的数值 |
| Box plot 箱型图 | Visualizes distribution and outliers 可视化分布形态及异常值 |
| Scatterplot 散点图 | Shows relationship between two variables 展示两个变量之间的关系 |
| Line plot 折线图 | Suitable for time series 适用于时间序列分析 |
| Heatmap 热力图 | Displays correlation or matrix values 展示相关性或矩阵数值 |

<div align="center">
  <img src="https://github.com/user-attachments/assets/249f5ee4-5fce-4a42-91f3-a5f62ff8480e" width="600"><br>
  <p><a href="https://keydifferences.com/difference-between-histogram-and-bar-graph.html/">直方图 vs. 条形图</a></p>
</div>

> 直方图主要用于显示数值型数据的分布，而条形图主要用于比较不同类别的数据。﻿

### 5.5 Regression Models (回归模型)
#### 5.5.1 Linear Regression (线性回归)
**Core Concept (核心原理)**:
- Finds best-fit line minimizing prediction errors  寻找最小化预测误差的最佳拟合直线
- Equation 方程: $y = \beta_0 + \beta_1X_1 + \cdots + \beta_nX_n + \epsilon$  

**Assumptions (假设)**:
| Assumption | Description | Violation Consequence 违背后果 |
|---|---|---|
| Linearity 线性 | Linear feature-target relationship | Poor model performance 模型性能差 |
| Independence 独立 | Observations not influencing each other | Biased estimates 估计偏差 |
| No Multicollinearity 无多重共线性 | Features not highly correlated | Unstable coefficients 系数不稳定 |
| Homoscedasticity 同方差性 | Constant error variance | Inefficient predictions 预测效率低 |

> 多重共线性 = 特征之间高度相关（比如“身高”和“腿长”几乎一样）。特征太像，模型难判断它们谁在起作用 → 系数不稳定。
> 同方差性 = 预测误差要稳定，不能忽大忽小（预测小值很准，预测大值很不准）。

**Regularization Types (正则化类型)**:
| Model | Best For | Key Features 关键特性 |
|---|---|---|
| Lasso Regression (L1) | Few useful features | Compresses coefficients to 0 将不重要特征系数压缩为0 |
| Ridge Regression (L2) | All features potentially useful | Shrinks coefficients 缩小系数但不压为0 |

**Implementation Steps (实现步骤)**:
1. Split data (train-test)
2. Initialize model
3. Fit model to training data
4. Predict on test set
5. Evaluate using MAE/MSE/R²

#### 5.5.2 Advanced Regression (进阶回归)
| Model | Best For | Key Features 关键特性 |
|---|---|---|
| **Decision Tree Regressor** | Non-linear data 非线性数据 | Splits data based on feature thresholds; Prone to overfitting 基于特征阈值分割数据; 易过拟合 |
| **Random Forest Regressor** | Complex patterns 复杂模式 | Ensemble of decision trees; Reduces overfitting 决策树集成; 减少过拟合 |
| **Time Series Models** | Temporal data 时序数据 | Moving averages for smoothing; ARIMA for trends/seasonality 移动平均平滑数据; ARIMA处理趋势/季节性 |

### 5.6 Classification Models (分类模型)
#### 5.6.1 Fundamental Classifiers (基础分类器)
**Logistic Regression (逻辑回归)**: 
- Sigmoid function outputs probabilities (S型函数输出概率)
- Decision boundary at 0.5 (默认决策边界0.5)
- Sensitive to feature scaling (对特征缩放敏感)

比如，预测邮件是不是垃圾邮件（是/否）

| 项目           | 中文解释                            |
| ------------ | ------------------------------- |
| **是做什么的？**   | 判断一件事是“是”还是“否”                  |
| **怎么判断？**    | 用一个“S型函数”（sigmoid）把结果变成0到1之间的概率 |
| **决策方法？**    | 如果概率 > 0.5 → 预测是；否则 → 否         |
| **对特征缩放敏感？** | 特征数值差距大 → 会影响模型判断准确性            |

**Decision Trees (决策树)**:
- **Splitting Criteria (分裂标准)**:
  - Gini impurity (基尼不纯度): Measures node purity (衡量节点纯度)
  - Entropy (熵): Information gain maximization (最大化信息增益)
- **Visualization (可视化)**: Plot tree structure

比如，是否贷款？第一问“收入高吗？”→再问“是否有房？”...

| 项目            | 中文解释               |
| ------------- | ------------------ |
| **是做什么的？**    | 用“问问题”的方式，一步步分类    |
| **怎么分？**      | 根据“纯度”决定怎么切分数据     |
| **Gini不纯度**   | 分得越“纯”，Gini越小      |
| **Entropy 熵** | 类似于信息混乱度 → 希望越分越清晰 |


**决策树 vs 逻辑回归区别对比：** 逻辑回归是用公式算出概率，决策树是一步步问问题分类。
| 项目     | 逻辑回归 Logistic | 决策树 Decision Tree |
| ------ | ------------- | ----------------- |
| 输出     | 概率（0\~1）      | 类别（是/否）           |
| 是否线性   | 是线性模型         | 非线性模型             |
| 是否需要缩放 | 需要缩放          | 不需要               |
| 是否易理解  | 一般            | 可画图，非常直观          |

#### 5.6.2 Ensemble Methods (集成方法)
“集成”就是：多个模型一起投票，提高准确率。Combine many weak models to make a strong model.
| Model | Mechanism | Hyperparameters | 
|---|---|---|
| **Random Forest** | Parallel tree building | `n_estimators` (决策树数量) |  
|  | Majority voting | `max_depth` (树深度限制) |  
| **Gradient Boosting** | Sequential tree building | `n_estimators` (总迭代次数) |  
|  | Error correction |  `learning_rate` (学习率) 每棵树贡献度 |  

**随机森林：**
| 概念       | 中文解释           |
| -------- | -------------- |
| **是什么？** | 很多决策树一起做决定（投票）Many decision trees vote together |
| **优点**   | 稳定、不容易过拟合、抗异常值 Stable, robust, handles outliers well |
|**超参数**| `n_estimators`: 树的数量（越多越稳）<br>`n_estimators`: number of trees<br> `max_depth`: 每棵树最多几层<br>`max_depth`: max depth of trees|

**Gradient Boosting（梯度提升）：**
| 概念       | 中文解释              |
| -------- | ----------------- |
| **是什么？** | 树一个接一个建，每棵树修正前面错误 Trees built sequentially to fix past mistakes |
| **优点**   | 精度高（但更慢）Very accurate (but slower)          |
| **超参数**  | `n_estimators`: 树的总数<br> `n_estimators`: total number of trees<br>`learning_rate`: 每棵树“纠错”的强度<br> `learning_rate`: how much each tree corrects |


#### 5.6.3 Model Comparison (模型对比)
回归 vs 决策树 = 回归看线性关系，树更灵活但解释方式不同。
| | Linear Regression 线性回归 | Decision Tree 决策树 |  
|---|---|---|
| **Data Compatibility** 适合数据 | Linear relationships 线性关系 | Non-linear patterns 非线性模式 |  
|  | Continuous data 连续数据 | Numerical/categorical data 数值/分类数据 |  
| **Interpretability** 解释性 | Coefficients show feature impact 系数显示特征影响 | IF-THEN rules explain decisions IF-THEN规则解释决策 |  
| **Robustness** 抗异常值能力 | Sensitive to outliers 对异常值敏感 | Robust to outliers 对异常值稳健 |  

### 5.7 Model Training & Validation (模型训练与验证)
#### Data Splitting (数据划分)
| Strategy | Usage |
|---|---|
| Train-Test Split (80-20) | General datasets 通用数据集 |
| TimeSeriesSplit | Temporal data 时间序列数据 |
| Stratified Split | Imbalanced classes 类别不平衡数据 |

#### Cross-Validation Techniques (交叉验证技术)
| Type | Mechanism | Advantages 优势 |
|---|---|---|
| K-Fold | Rotating test folds | Reduces variance 降低方差 |
| Leave-One-Out | Each sample as test set | Maximizes training data 最大化训练数据 |

#### Hyperparameter Tuning (超参数调优)
超参数 = 你手动设置的模型配置，比如树的数量、学习率等；调优 = 尝试不同设置，看哪一组效果最好。
- **GridSearchCV（网格搜索）:** 穷举所有可能组合 Try every possible combination of parameters，比如：尝试所有 n_estimators = [100, 200, 300] 和 max_depth = [3, 5, 7] 的组合 -> Tries all (100,3), (100,5)...(300,7)。优点是结果全面，缺点是非常慢，尤其参数多时。
- **RandomizedSearchCV（随机搜索）:** 随机尝试部分组合 Randomly try some combinations (not all)。节省时间，但可能错过最优解 Faster, but may miss the best one

GridSearch 是“全部试一遍”，RandomSearch 是“随机试几种”。都可以帮你找出哪个超参数组合效果最好。

## 6. Evaluation (评估)
### 6.1 Regression Metrics (回归指标)
| Metric | Calculation | Interpretation |
|---|---|---|
| **MAE** 平均绝对误差 | $\frac{1}{n}\sum\|y-\hat{y}\|$ | Average prediction error 平均预测误差 <br>Robust to outliers 对异常值稳健 |
| **RMSE** 均方根误差 | $\sqrt{\frac{1}{n}\sum(y-\hat{y})^2}$ | Punishes large errors 惩罚大误差<br>Sensitive to outliers 对异常值敏感 |
| **R²** 决定系数 | $1 - \frac{SS_{res}}{SS_{tot}}$ | % variance explained 解释方差百分比<br>1.0 = perfect fit 完美拟合 |

### 6.2 Classification Metrics (分类指标)
#### Confusion Matrix Components (混淆矩阵要素)
| Term | Description | Impact | 影响 |
|---|---|---|---|
| TP 真阳性 | Correct positive predictions 正确预测为正类 | Increases precision/recall | 提升精确率/召回率 |
| FP 假阳性 | False alarms 错误预测为正类 | Reduces precision | 降低精确率 |
| FN 假阴性 | Missed positives 错误预测为负类 | Reduces recall | 降低召回率 |

#### Key Metrics (核心指标)
| Metric | Formula | Business Use Case | 业务场景 |
|---|---|---|---|
| Precision 精确率 | $\frac{TP}{TP+FP}$ | Fraud detection (minimize false alarms) | 欺诈检测(减少误报) |
| Recall 召回率 | $\frac{TP}{TP+FN}$ | Disease screening (miss no cases) | 疾病筛查(不漏诊) |
| F1-score F1分数 | $2\times\frac{P\times R}{P+R}$ | Balanced performance | 平衡精确率与召回率 |

### 6.3 Special Scenarios (特殊场景)
#### Imbalanced Classes (类别不平衡)
什么叫不平衡？一个分类很少（如：诈骗邮件=5%，正常邮件=95%） → 模型容易只学多数类。

**常用处理方法：**
| Technique | Mechanism | Best For 适用场景 |
|---|---|---|
| SMOTE | Synthetic minority oversampling 用已有少数样本“生成”假样本，补充少数类 | Small minority classes 少数类样本少 |
| Class Weighting | Penalize majority class errors 给“错分少数类”更高惩罚，让模型重视它 | Moderate imbalance 中度不平衡 |

#### Threshold Optimization (阈值优化)
默认分类标准是 概率 > 0.5 就是正类，你可以改这个“阈值”，让模型偏向更保守或更大胆。
- Precision-Recall Tradeoff (精确率-召回率权衡):
  - Higher threshold → higher precision (高阈值→高精确率)
  - Lower threshold → higher recall (低阈值→高召回率)
- ROC Curve Analysis 曲线分析: AUC > 0.9 = excellent separation 模型区分正负样本的能力非常好

**Precision-Recall Tradeoff 精确率 vs 召回率：**
| 阈值调整       | 效果               | 解释                     |
| ---------- | ---------------- | ---------------------- |
| 阈值高 → 精确率高 | 模型更保守，只挑最有把握的当正类 | 少报错（FP ↓）但会漏掉一些（FN ↑）  |
| 阈值低 → 召回率高 | 模型更宽松，能多抓正类      | 多抓住（FN ↓）但也更容易报错（FP ↑） |

### 6.4 Model Diagnostics (模型诊断)
#### Overfitting Detection (过拟合检测)
| Sign | Solution 解决方案 |
|---|---|
| High train accuracy, low test accuracy | Increase regularization 增强正则化 |
| Complex tree structures | Prune trees (reduce depth) 剪枝(降低深度) |

#### Bias-Variance Tradeoff (偏差-方差权衡)
| Condition | Diagnosis | Remedy 补救措施 |
|---|---|---|
| High training error | Underfitting (high bias) | Add features/reduce regularization 增加特征/减少正则化 |
| Large train-test gap | Overfitting (high variance) | More data/feature reduction 增加数据/特征降维 |

## 7. Unsupervised Learning & Clustering (无监督学习与聚类)
无监督学习就是让模型自己找规律。聚类是最常用的方法，比如 KMeans（分中心点），Hierarchical（像树一样合并），然后再用“肘部法”和“轮廓系数”来判断聚得好不好。

### 7.1 Unsupervised Learning (无监督学习)
- Used for unlabeled data to discover structure/patterns  用于无标签数据发现数据结构或模式，让算法自己去发现规律或分组
- Applications: document grouping, customer segmentation, species clustering  比如把文章自动分类、客户分群、物种聚类

### 7.2 Clustering Methods (聚类方法)
什么是聚类呢？把“相似的”样本放在一起，就形成“簇”。Group similar points into clusters.

**常见聚类方法 Clustering Methods：**
| 类型    | 方法               | 原理解释（简单版）          |
| ----- | ---------------- | ------------------ |
| 基于中心点 | KMeans           | 用“中心点”代表每个群，然后不断调整 |
| 基于连接性 | Hierarchical     | 谁离谁近就先连起来，像搭积木一样合并 |
| 基于密度  | DBSCAN           | 找“点多的地方”成群，稀疏的就当异常 |
| 基于分布  | Gaussian Mixture | 假设数据来自多个概率分布组成的混合  |

### 7.3 KMeans Clustering (K均值聚类)
**Steps (步骤)**:
1. Randomly pick k centroids (随机选择k个质心)
2. Assign points to nearest centroid (分配点到最近质心)
3. Recalculate centroids as mean of points (重新计算质心为点均值)
4. Repeat until convergence (重复直到收敛)

**Characteristics (特性)**:
- Sensitive to outliers/scaling (对异常值和缩放敏感，特征没缩放好也不准)
- Requires predefined k (需要预设k值 —— 聚几组)

### 7.4 Hierarchical Clustering (层次聚类)
像树一样一步步合并（或拆分）簇。
- Agglomerative (bottom-up)凝聚式 从下往上: Start with single points, merge clusters  从每个点开始，合并 → 越来越大
- Divisive (top-down)分裂式 从上向下: Start with all data, split clusters  先把所有数据当一群，再一点点拆开
- Visualized with dendrogram 用树状图展示这些合并过程，像族谱一样

### 7.5 Clustering Evaluation (聚类评估)
**Elbow Method (肘部法)**:
看不同 K 值时，组内误差（WSS）下降多少；哪个点开始“下降变缓”，就是合适的 K 值；画图时像“手肘”弯曲那儿，就是最佳值
- Plot WSS (Within-Cluster Sum of Squares) vs. k  绘制不同k值对应的组内平方和
- Choose k at "elbow" point where WSS stops decreasing significantly  在WSS停止显著下降的"肘部"选择k值

**Silhouette Score (轮廓系数)**:
数值在 -1 到 1 之间，越高表示分群越清晰；比较每个点：它跟自己群的像？跟别的群的不像？
- Measures similarity to own cluster vs other clusters  衡量点与自身簇和其他簇的相似度
- Range [-1, 1], higher is better (范围[-1,1]，越高越好)


## 8. Deployment & Recommendations (部署与建议)
### 8.1 CRISP-DM Evaluation Phase (CRISP-DM评估阶段)
**Critical Questions (关键问题)**:
1. Did model meet business objectives? (是否满足业务目标?)
2. What types of errors dominate? (主导错误类型?)
3. Are errors randomly distributed? (误差随机分布吗?)
4. Can model generalize to new data? (能否泛化到新数据?)
5. Key insights from results? (结果的核心洞见?)

### 8.2 Actionable Recommendations (可执行建议)
**SMART Framework (SMART框架)**:
| Principle | Example | Avoid 反例 |
|---|---|---|
| Specific 具体 | "Apply log transform to feature X 对特征X应用对数变换" | "Try different models 尝试不同模型" |
| Measurable 可衡量 | "Improve MAE by 5% MAE提升5%" | "Make model better 改进模型" |
| Achievable 可达成 | "Add lag features from historical data 从历史数据添加滞后特征" | "Collect impossible data 收集不可能的数据" |
| Relevant 相关 | "Remove redundant features to simplify 删除冗余特征以简化" | "Change programming language 更换编程语言" |
| Time-bound 有时限 | "Implement by next quarter 下季度前实施" | "When possible 尽快" |

### 8.3 Hourglass Method for Conclusion (漏斗式结论结构)
- Zoom out from model results to overall project objectives  从具体模型结果逐步"放大"到整个项目目标
- Explicitly connect results to original hypotheses/business goals  明确地将结果与最初的假设或业务目标联系起来
- Reflect on modeling choices and their impact  反思建模过程中做出的选择及其影响

### 8.4 Metric Interpretation (指标解释)
- Explain metrics in layman's terms (e.g., "MAE=0.6 means average prediction error is 0.6 units")  用通俗语言解释指标含义（如"MAE=0.6表示平均预测误差0.6个单位"）
- Contextualize whether result is "good" based on domain knowledge  基于领域知识说明结果是否"良好"

### 8.5 Reflect on Data Preparation (回顾数据准备)
- How did data understanding/preparation steps impact modeling?  数据理解/准备中的步骤如何影响建模？
- Were there unintended side effects or overlooked factors?  是否有副作用或遗漏的因素？
- What would you do differently knowing what you know now?  你现在知道的知识，是否能帮助你做出更好的准备？