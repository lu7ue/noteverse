# Bootstrap 5

## 1. 介绍
本文档总结了 Bootstrap 5 的基础知识，仅涵盖常用功能和组件，便于快速开发和入门学习。\
示例代码仓库：<https://github.com/lu7ue/noteverse/tree/main/what_i_learnt/Bootstrap5/example-codes/html>

> **一、基础部分（Basics）**
>> 1. 布局系统（Layout）  
>> 2. 排版与文本样式（Typography）
>> 3. 间距与尺寸（Spacing & Sizing）  
>> 4. Flex 与对齐（Flex & Alignment）  

> **二、组件类（Utilities / Components）**
>> 1. 按钮（Buttons）  
>> 2. 导航栏（Navbar）  
>> 3. 卡片（Cards） 
>> 4. 表单（Forms）  
>> 5. 弹窗与折叠（Modal, Collapse）  
>> 6. 提示框（Alert）  
>> 7. 徽章（Badge）  
>> 8. 面包屑导航（Breadcrumb）  
>> 9. 列表组（List group）  
>> 10. 进度条（Progress）  
>> 11. 手风琴折叠（Accordion）  
>> 12. 加载动画（Spinner）   
>> 13. 图片辅助类（Image）  

更多高级用法需参考官方文档：<https://getbootstrap.com/docs/5.3/getting-started/introduction/>

**下载与安装：**

1. 从 [Bootstrap 官方 GitHub](https://github.com/twbs/bootstrap/releases) 下载最新源码，将 `dist` 文件夹整个复制到项目目录（可重命名为 `bootstrap`或其他名称）。  
2. 在顶部引入 CSS（放在`<title>`标签下方）：
    ```html
   <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
   ```
3. 在底部引入 JS（放在`<body>`标签内的最下方）：
    ```html
    <script src="bootstrap/js/bootstrap.bundle.min.js"></script>
    ```

## 2. 基础部分（Basics）内容

### 1. 布局系统

#### 1.1 容器 Container

Bootstrap 的布局都必须放在容器里，它控制页面宽度和响应式断点。
- `.container`
- `.container-fluid`

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <div class="row bg-secondary p-2">
        <div class="col-6 bg-primary text-white text-center p-2">左半部分</div>
        <div class="col-6 bg-success text-white text-center p-2">右半部分</div>
    </div>
</div>

<div class="container-fluid bg-light p-3 mb-3">
    <div class="row bg-secondary p-2">
        <div class="col-4 bg-info text-dark p-2">列 1</div>
        <div class="col-4 bg-success text-dark text-center p-2">列 2</div>
        <div class="col-4 bg-danger text-dark text-center p-2">列 3</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/1.png)

#### 1.2 行 Row + 列 Col

- 行用来水平排列列（col）：`.row` 自动去除列间的负边距，使列对齐正确。
- 列必须放在 `.row` 里，`.col` 默认等分。也可以使用 `.col-{n}` 指定列宽，`n` 取值 1-12，表示 12 栅格系统中的份额。

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p>基础 Row + Col：三列平分宽度，每列等宽。</p>
    <div class="row bg-secondary p-2">
        <div class="col bg-info text-dark text-center p-2">列 1</div>
        <div class="col bg-success text-dark text-center p-2">列 2</div>
        <div class="col bg-warning text-dark text-center p-2">列 3</div>
    </div>
</div>

<div class="container bg-light p-3 mb-3">
    <p>指定列宽：左右各占 6 栅格。</p>
    <div class="row bg-secondary p-2">
        <div class="col-6 bg-info text-dark text-center p-2">col-6 左半</div>
        <div class="col-6 bg-success text-dark text-center p-2">col-6 右半</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/2.png)

#### 1.3 响应式列

Bootstrap 提供断点类，让列在不同屏幕尺寸下自适应：
- sm: ≥576px; 
- md: ≥768px; 
- lg: ≥992px; 
- xl: ≥1200px; 
- xxl: ≥1400px

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <div class="row bg-secondary p-2">
        <div class="col-12 col-sm-6 col-md-4 bg-info text-dark text-center p-2 mb-2">col-12/sm-6/md-4</div>
        <div class="col-12 col-sm-6 col-md-4 bg-success text-dark text-center p-2 mb-2">col-12/sm-6/md-4</div>
        <div class="col-12 col-sm-12 col-md-4 bg-warning text-dark text-center p-2 mb-2">col-12/sm-12/md-4</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/3.png)

### 2. 排版与文本样式（Typography）
Bootstrap 提供内置类来控制文字的样式、对齐、大小写、行高、字号和颜色。

#### 2.1 样式
**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p class="fw-bold text-dark p-2">fw-bold：加粗文字</p>
    <p class="fw-semibold text-dark p-2">fw-semibold：半粗文字</p>
    <p class="fw-normal text-dark p-2">fw-normal：正常文字</p>
    <p class="fw-light text-dark p-2">fw-light：细字体</p>
    <p class="fw-bold text-dark p-2">fw-bold：加粗文字</p>
    <p class="fst-italic text-dark p-2">fst-italic：斜体文字</p>
    <p class="fw-normal text-dark p-2">fw-normal：正常文字</p>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/4.png)

#### 2.2 对齐
**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p class="text-start text-dark p-2">text-start：左对齐</p>
    <p class="text-center text-dark p-2">text-center：居中</p>
    <p class="text-end text-dark p-2">text-end：右对齐</p>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/5.png)

#### 2.3 转换
**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p class="text-uppercase text-dark p-2">text-uppercase：全部大写</p>
    <p class="text-lowercase text-dark p-2">TEXT-LOWERCASE：全部小写</p>
    <p class="text-capitalize text-dark p-2">text-capitalize：每个单词首字母大写</p>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/6.png)

#### 2.4 行高
**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p class="lh-1 bg-secondary text-white p-2">lh-1：行高 1</p>
</div>
<div class="container bg-light p-3 mb-3">
    <p class="lh-sm bg-secondary text-white p-2">lh-sm：行高稍小</p>
</div>
<div class="container bg-light p-3 mb-3">
    <p class="lh-base bg-secondary text-white p-2">lh-base：默认行高</p>
</div>
<div class="container bg-light p-3 mb-3">
    <p class="lh-lg bg-secondary text-white p-2">lh-lg：行高稍大</p>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/7.png)

#### 2.5 字号
**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p class="fs-1 text-dark p-2">fs-1：最大字号</p>
    <p class="fs-2 text-dark p-2">fs-2</p>
    <p class="fs-3 text-dark p-2">fs-3</p>
    <p class="fs-4 text-dark p-2">fs-4</p>
    <p class="fs-5 text-dark p-2">fs-5</p>
    <p class="fs-6 text-dark p-2">fs-6：最小字号</p>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/8.png)

#### 2.6 字体颜色与背景
**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p class="text-primary p-2">text-primary：蓝色文字</p>
    <p class="text-secondary p-2">text-secondary：灰色文字</p>
    <p class="text-success p-2">text-success：绿色文字</p>
    <p class="text-danger p-2">text-danger：红色文字</p>
    <p class="text-warning p-2">text-warning：黄色文字</p>
    <p class="text-info p-2">text-info：青色文字</p>
    <p class="text-light bg-dark p-2">text-light：浅色文字</p>
    <p class="text-dark p-2">text-dark：深色文字</p>
    <p class="text-muted p-2">text-muted：浅灰色文字</p>
</div>

<div class="container bg-light p-3 mb-3">
    <p class="bg-primary text-white p-2">bg-primary + text-white：蓝色背景白色文字</p>
    <p class="bg-success text-white p-2">bg-success + text-white：绿色背景白色文字</p>
    <p class="bg-warning text-dark p-2">bg-warning + text-dark：黄色背景深色文字</p>
    <p class="bg-dark text-white p-2">bg-dark + text-white：深色背景白色文字</p>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/9.png)

### 3. 间距与尺寸（Spacing & Sizing）  
在 Bootstrap 中，控制间距的工具类分为 margin（外边距）和 padding（内边距）。\
所有类后面的数字从 0 到 5，表示间距大小递增，0 是没有间距。
#### 3.1 外边距 Margin
对于 margin，可以用 m- 给元素四周都加外边距，用 mt- 给上方加，用 mb- 给下方加。\
为了适应不同的文字方向（LTR 或 RTL），Bootstrap 使用逻辑方向的类：ms- 是起始边（左侧在 LTR，右侧在 RTL），me- 是结束边（右侧在 LTR，左侧在 RTL）。\
如果想同时控制水平的左右，可以用 mx-；控制垂直的上下可以用 my-。

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <div class="bg-primary text-white m-0 p-2">m-0</div>
</div>
<div class="container bg-light p-3 mb-3">
    <div class="bg-secondary text-white m-1 p-2">m-1</div>
</div>
<div class="container bg-light p-3 mb-3">
    <div class="bg-success text-white m-2 p-2">m-2</div>
</div>
<div class="container bg-light p-3 mb-3">
    <div class="bg-warning text-white m-3 p-2">m-3</div>
</div>
<div class="container bg-light p-3 mb-3">
    <div class="bg-info text-white m-4 p-2">m-4</div>
</div>
<div class="container bg-light p-3 mb-3">
    <div class="bg-danger text-white m-5 p-2">m-5</div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/10.png)

#### 3.2 内边距 Padding
padding 是同样的规则，只是前缀换成 p：p- 是四周，pt- 上内边距，pb- 下内边距，ps- 起始边，pe- 结束边，px- 水平，py- 垂直。

**示例代码：**
```html
<div class="container bg-light mb-3">
    <div class="bg-primary text-white p-0">p-0</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-secondary text-white p-1">p-1</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-success text-white p-2">p-2</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-warning text-white p-3">p-3</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-info text-white p-4">p-4</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-danger text-white p-5">p-5</div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/11.png)

#### 3.3 单方向间距 & 水平居中
**示例代码：**
```html
<div class="container bg-light mb-3">
    <div class="bg-primary text-white mt-3 mb-4 p-2">mt-3 + mb-4</div>
</div>
<div class="container d-flex justify-content-center mb-3">
    <div class="bg-success text-white p-2 w-50">mx-auto：水平居中</div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/12.png)

#### 3.4 宽高控制
**示例代码：**
```html
<div class="container bg-light mb-3">
    <div class="bg-primary text-white w-25 p-2">w-25</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-success text-white w-50 p-2">w-50</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-warning text-white w-75 p-2">w-75</div>
</div>
<div class="container bg-light mb-3">
    <div class="bg-danger text-white w-100 p-2">w-100</div>
</div>
<div class="container bg-light" style="height:200px;">
    <div class="bg-dark text-white w-50 h-100 d-flex align-items-center justify-content-center">h-100：占满父容器高度
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/13.png)

### 4. Flex 与对齐（Flex & Alignment）
Bootstrap 提供 flex 工具类，让布局快速实现水平、垂直排列和间距控制。

#### 4.1 d-flex
d-flex：将容器设置为 flex 布局，子元素水平排列（默认 flex-row）

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <div class="d-flex bg-secondary p-2">
        <div class="bg-primary text-white p-2 me-2">子元素 1</div>
        <div class="bg-success text-white p-2 me-2">子元素 2</div>
        <div class="bg-warning text-white p-2">子元素 3</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/14.png)

#### 4.2 justify-content-*
justify-content-*：控制子元素在主轴（水平方向）上的对齐方式

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p>start：靠左</p>
    <div class="d-flex justify-content-start bg-secondary p-2 mb-2">
        <div class="bg-primary text-white p-2">start</div>
        <div class="bg-success text-white p-2">start</div>
    </div>
    <p>center：居中</p>
    <div class="d-flex justify-content-center bg-secondary p-2 mb-2">
        <div class="bg-primary text-white p-2">center</div>
        <div class="bg-success text-white p-2">center</div>
    </div>
    <p>between：两端对齐，中间平均分布</p>
    <div class="d-flex justify-content-between bg-secondary p-2">
        <div class="bg-primary text-white p-2">between 1</div>
        <div class="bg-success text-white p-2">between 2</div>
        <div class="bg-warning text-white p-2">between 3</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/15.png)

#### 4.3 align-items-*
align-items-*：控制子元素在交叉轴（垂直方向）上的对齐方式

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p>start：靠上</p>
    <div class="d-flex align-items-start bg-secondary p-2 mb-2" style="height:100px;">
        <div class="bg-primary text-white p-2">start</div>
        <div class="bg-success text-white p-2">start</div>
    </div>
    <p>center：垂直居中</p>
    <div class="d-flex align-items-center bg-secondary p-2 mb-2" style="height:100px;">
        <div class="bg-primary text-white p-2">center</div>
        <div class="bg-success text-white p-2">center</div>
    </div>
    <p>end：靠下</p>
    <div class="d-flex align-items-end bg-secondary p-2" style="height:100px;">
        <div class="bg-primary text-white p-2">end</div>
        <div class="bg-success text-white p-2">end</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/16.png)

#### 4.4 flex-row / flex-column
flex-row / flex-column：控制子元素排列方向

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p>flex-row（默认水平排列）</p>
    <div class="d-flex flex-row bg-secondary p-2 mb-2">
        <div class="bg-primary text-white p-2 me-2">row 1</div>
        <div class="bg-success text-white p-2 me-2">row 2</div>
        <div class="bg-warning text-white p-2">row 3</div>
    </div>
    <p>flex-column（垂直排列）</p>
    <div class="d-flex flex-column bg-secondary p-2">
        <div class="bg-primary text-white p-2 mb-2">col 1</div>
        <div class="bg-success text-white p-2 mb-2">col 2</div>
        <div class="bg-warning text-white p-2">col 3</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/17.png)

#### 4.5 gap-*
gap-*：控制 flex 子元素之间的间距

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <p>gap-2：间距小</p>
    <div class="d-flex gap-2 bg-secondary p-2 mb-2">
        <div class="bg-primary text-white p-2">1</div>
        <div class="bg-success text-white p-2">2</div>
        <div class="bg-warning text-white p-2">3</div>
    </div>
    <p>gap-3：间距大</p>
    <div class="d-flex gap-3 bg-secondary p-2">
        <div class="bg-primary text-white p-2">1</div>
        <div class="bg-success text-white p-2">2</div>
        <div class="bg-warning text-white p-2">3</div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/1-basics/18.png)

## 3. 组件类（Utilities / Components）内容

### 3.1 按钮（Buttons） 
Bootstrap 提供丰富的按钮样式，通过类名控制颜色、边框和大小。

#### 3.1.1 基础按钮颜色

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <button class="btn btn-primary me-2 mb-2">Primary</button>
    <button class="btn btn-secondary me-2 mb-2">Secondary</button>
    <button class="btn btn-success me-2 mb-2">Success</button>
    <button class="btn btn-danger me-2 mb-2">Danger</button>
    <button class="btn btn-warning me-2 mb-2">Warning</button>
    <button class="btn btn-info me-2 mb-2">Info</button>
    <button class="btn btn-light me-2 mb-2">Light</button>
    <button class="btn btn-dark me-2 mb-2">Dark</button>
</div>
```

#### 3.1.2 轮廓按钮（Outline）

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <button class="btn btn-outline-primary me-2 mb-2">Outline Primary</button>
    <button class="btn btn-outline-secondary me-2 mb-2">Outline Secondary</button>
    <button class="btn btn-outline-success me-2 mb-2">Outline Success</button>
    <button class="btn btn-outline-danger me-2 mb-2">Outline Danger</button>
    <button class="btn btn-outline-warning me-2 mb-2">Outline Warning</button>
    <button class="btn btn-outline-info me-2 mb-2">Outline Info</button>
    <button class="btn btn-outline-light me-2 mb-2">Outline Light</button>
    <button class="btn btn-outline-dark me-2 mb-2">Outline Dark</button>
</div>
```

#### 3.1.3 按钮大小

**示例代码：**
```html
<div class="container bg-light p-3 mb-3">
    <button class="btn btn-primary btn-sm me-2 mb-2">Small</button>
    <button class="btn btn-primary btn-lg me-2 mb-2">Large</button>
    <button class="btn btn-primary me-2 mb-2">默认</button>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/1.png)

### 3.2 导航栏（Navbar） 
Bootstrap 的导航栏由 <code>navbar</code> 类控制，通常包含品牌、折叠按钮和菜单项。
<ul>
    <li><code>navbar-expand-lg</code>：在大屏以上显示横向菜单，小屏时折叠成汉堡按钮。</li>
    <li>折叠按钮 <code>navbar-toggler</code> 配合 <code>collapse navbar-collapse</code> 使用，实现响应式折叠菜单。</li>
    <li><code>ms-auto</code>：将菜单项靠右对齐。</li>
</ul>

**示例代码：**
```html
<div class="container mb-3">
    <p>基础导航栏示例</p>
    <nav class="navbar navbar-expand-lg navbar-light bg-light mb-3">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">LOGO</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navExample">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navExample">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link active" href="#">首页</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">关于</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">服务</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">联系</a></li>
                </ul>
            </div>
        </div>
    </nav>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/2.png)
![title](../../img/what_i_learnt/Bootstrap5/2-utilities/3.png)

### 3.3 卡片（Cards） 
Bootstrap 的卡片组件可以显示图片、标题、文本和按钮，常用于内容展示。
<p>
    <code>card</code>：整体卡片容器<br>
    <code>card-img-top 或 card-img-bottom</code>：卡片顶部或底部图片(需要调整 img 标签内容的放置位置)<br>
    <code>card-body</code>：卡片内容区域<br>
    <code>card-title</code>：标题<br>
    <code>card-text</code>：文本内容<br>
    卡片内可以放置 <code>btn</code> 等其他组件
</p>

**示例代码：**
```html
<div class="container mb-3 d-flex gap-4">
        <div>
            <p>基础卡片示例 - 图片在上面</p>
            <div class="card" style="width: 18rem;">
                <img src="../../../../img/what_i_learnt/Bootstrap5/placeholder-image.png" class="card-img-top"
                    alt="示例图片">
                <div class="card-body">
                    <h5 class="card-title">卡片标题</h5>
                    <p class="card-text">这里是卡片内容示例，可以放文字、说明或摘要。</p>
                    <a href="#" class="btn btn-primary">按钮</a>
                </div>
            </div>
        </div>
        <div>
            <p>基础卡片示例 - 图片在下面</p>
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">卡片标题</h5>
                    <p class="card-text">这里是卡片内容示例，可以放文字、说明或摘要。</p>
                    <a href="#" class="btn btn-primary">按钮</a>
                </div>
                <img src="../../../../img/what_i_learnt/Bootstrap5/placeholder-image.png" class="card-img-bottom"
                    alt="示例图片">
            </div>
        </div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/4.png)

### 3.4 表单（Forms） 
涵盖输入框、下拉框、单复选框、文本区、按钮和输入组。
<p>
    文本输入框/文本区都使用 <code>form-control</code>，下拉框使用 <code>form-select</code>。<br>
    单选和复选框使用 <code>form-check</code> 容器，<code>form-check-input</code> 是控件，<code>form-check-label</code> 是文字。<br>
    输入组 <code>input-group</code> 可组合按钮或文本附加元素，<code>input-group-text</code> 是附加文本。<br>
    <code>mb-3</code> 为控件增加下边距，搭配 <code>row</code> 和 <code>col</code> 可实现整齐布局。
</p>

**示例代码：**
```html
<div class="container mb-3">
        <div class="mb-3">
            <label for="inputText" class="form-label">文本输入框</label>
            <input type="text" class="form-control" id="inputText" placeholder="请输入内容">
        </div>

        <div class="mb-3">
            <label for="inputPassword" class="form-label">密码</label>
            <input type="password" class="form-control" id="inputPassword" placeholder="密码">
        </div>

        <div class="mb-3">
            <label for="selectExample" class="form-label">选择框</label>
            <select class="form-select" id="selectExample">
                <option selected>请选择</option>
                <option value="1">选项 1</option>
                <option value="2">选项 2</option>
                <option value="3">选项 3</option>
            </select>
        </div>

        <div class="mb-3">
            <label for="textareaExample" class="form-label">文本区</label>
            <textarea class="form-control" id="textareaExample" rows="3"></textarea>
        </div>

        <div class="mb-3">
            <div class="form-check">
                <input class="form-check-input" type="radio" name="radioGroup" id="radio1">
                <label class="form-check-label" for="radio1">单选 1</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="radioGroup" id="radio2" checked>
                <label class="form-check-label" for="radio2">单选 2</label>
            </div>
        </div>

        <div class="mb-3">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="check1">
                <label class="form-check-label" for="check1">复选 1</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="check2">
                <label class="form-check-label" for="check2">复选 2</label>
            </div>
        </div>

        <div class="input-group mb-3">
            <span class="input-group-text">@</span>
            <input type="text" class="form-control" placeholder="用户名">
        </div>

        <button class="btn btn-primary">提交</button>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/5.png)

### 3.5 弹窗与折叠（Modal, Collapse）  
Bootstrap 提供 Modal 弹窗和 Collapse 折叠面板，需要引入 Bootstrap JS。
<p>
    Modal 使用 <code>data-bs-toggle="modal"</code> 和 <code>data-bs-target="#id"</code> 打开，<code>modal</code>
    容器内部包含
    <code>modal-dialog</code>、<code>modal-content</code>、<code>modal-header</code>、<code>modal-body</code>、<code>modal-footer</code>。<br>
    Collapse 使用 <code>data-bs-toggle="collapse"</code> 和 <code>data-bs-target="#id"</code> 控制显示隐藏，配合
    <code>collapse</code> 类即可。
</p>

**Modal 弹窗示例:**

**示例代码：**
```html
<div class="container mb-3">
    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalExample">打开弹窗</button>

    <div class="modal fade" id="modalExample">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">弹窗标题</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    这里是弹窗内容，可以放文字、图片、表单等。
                </div>
                <div class="modal-footer">
                    <button class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
                    <button class="btn btn-primary">确认</button>
                </div>
            </div>
        </div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/6.png)
![title](../../img/what_i_learnt/Bootstrap5/2-utilities/7.png)

**Collapse 折叠面板示例:**

**示例代码：**
```html
<button class="btn btn-info mb-2" data-bs-toggle="collapse" data-bs-target="#collapseExample">切换折叠内容</button>
<div class="collapse" id="collapseExample">
    <div class="card card-body">
        这是折叠面板的内容，可以显示隐藏信息。
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/8.png)

### 3.6 提示框（Alert）  
Bootstrap 提供内置提示框类，用于显示不同类型的消息或状态。
<p>
    使用 <code>alert</code> 类创建提示框，再加上颜色类 <code>alert-primary</code> ~ <code>alert-dark</code>。<br>
    <code>role="alert"</code> 用于辅助无障碍提示，屏幕阅读器会识别它。<br>
    可搭配 <code>alert-dismissible</code> 和按钮实现可关闭提示框。
</p>

**示例代码：**
```html
<div class="container mb-3">
    <p>基础提示框示例</p>
    <div class="alert alert-primary" role="alert">
        这是一个蓝色提示框！
    </div>
    <div class="alert alert-success" role="alert">
        这是一个绿色提示框！
    </div>
    <div class="alert alert-danger" role="alert">
        这是一个红色提示框！
    </div>
    <div class="alert alert-warning" role="alert">
        这是一个黄色提示框！
    </div>
    <div class="alert alert-info" role="alert">
        这是一个青色提示框！
    </div>
    <div class="alert alert-dark" role="alert">
        这是一个深色提示框！
    </div>
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        这是一个可关闭的黄色提示框！
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/9.png)

### 3.7 徽章（Badge）  
Bootstrap 徽章用于显示状态或数量，通常嵌入文字或按钮旁。
<p>
    <code>badge</code> 类创建徽章，颜色用 <code>bg-*</code> 控制，<code>text-dark</code> 可调文字颜色。<br>
    徽章一般用于标记状态或数量，不具备按钮交互。
</p>

**基础徽章示例:**

**示例代码：**
```html
<div class="container mb-3">
    <span class="badge bg-primary">Primary</span>
    <span class="badge bg-success">Success</span>
    <span class="badge bg-danger">Danger</span>
    <span class="badge bg-warning text-dark">Warning</span>
    <span class="badge bg-info text-dark">Info</span>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/10.png)

**嵌入按钮示例:**

**示例代码：**
```html
<button class="btn btn-primary">
    消息 <span class="badge bg-light text-dark">4</span>
</button>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/11.png)

### 3.8 面包屑导航（Breadcrumb）
Bootstrap 提供内置面包屑类，用于显示页面层级结构，帮助用户了解当前位置。面包屑本质是一个有序列表，内置样式自动添加分隔符 /。
<p>
    使用 <code>breadcrumb</code> 类创建面包屑容器，<code>breadcrumb-item</code> 创建每一层导航。<br>
    当前页添加 <code>active</code> 类并使用 <code>aria-current="page"</code>，屏幕阅读器可以识别当前页面。<br>
    适合用于多层页面结构，快速展示用户所在位置。
</p>

**示例代码：**
```html
<div class="container mb-3">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">首页</a></li>
            <li class="breadcrumb-item"><a href="#">分类</a></li>
            <li class="breadcrumb-item active" aria-current="page">当前页</li>
        </ol>
    </nav>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/12.png)

### 3.9 列表组（List group）  
Bootstrap 提供列表组组件，用于显示整齐的列表项，支持颜色类、激活状态（用 active 来标识“当前项”，视觉高亮）和可点击项（list-group-item-action 提供鼠标悬停和点击反馈，使列表项可交互），常用于菜单、状态列表、信息展示或导航。
<p>
    <code>list-group</code> 用于容器，<code>list-group-item</code> 用于每个列表项。<br>
    可加 <code>list-group-item-*</code> 颜色类显示不同状态信息。<br>
    列表组可嵌套链接或按钮，使列表可点击。
</p>

**示例代码：**
```html
<div class="container mb-3">
    <p>基础列表组示例</p>
    <ul class="list-group">
        <li class="list-group-item">第一项</li>
        <li class="list-group-item">第二项</li>
        <li class="list-group-item">第三项</li>
    </ul>

    <p class="mt-3">带颜色或状态的列表项</p>
    <ul class="list-group">
        <li class="list-group-item list-group-item-primary">蓝色项</li>
        <li class="list-group-item list-group-item-success">绿色项</li>
        <li class="list-group-item list-group-item-danger">红色项</li>
        <li class="list-group-item list-group-item-warning">黄色项</li>
    </ul>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/13.png)

### 3.10 进度条（Progress）  
Bootstrap 提供内置进度条类，用于显示任务或操作的完成进度。\
内置样式自动显示带圆角轨道，支持多种颜色表示状态，可自定义宽度显示完成百分比，可叠加多条 progress-bar 显示复杂进度。
<p>
    <code>progress</code> 是外层容器，表示进度条轨道。<br>
    <code>progress-bar</code> 是实际进度条，<code>bg-*</code> 控制颜色。<br>
    通过 <code>style="width: %"</code> 设置进度值。<br>
    可叠加多个 <code>progress-bar</code> 创建分段进度条。
</p>

**示例代码：**
```html
<div class="container mb-3">
    <p>基础进度条示例</p>
    <div class="progress mb-2">
        <div class="progress-bar bg-success" role="progressbar" style="width: 50%"></div>
    </div>

    <p>不同颜色的进度条</p>
    <div class="progress mb-2">
        <div class="progress-bar bg-primary" role="progressbar" style="width: 70%"></div>
    </div>
    <div class="progress mb-2">
        <div class="progress-bar bg-danger" role="progressbar" style="width: 30%"></div>
    </div>
    <div class="progress mb-2">
        <div class="progress-bar bg-warning" role="progressbar" style="width: 60%"></div>
    </div>

    <p>多段进度条示例</p>
    <div class="container mb-3">
        <div class="progress" style="height: 30px;">
            <div class="progress-bar bg-success" role="progressbar" style="width: 10%">阶段 1</div>
            <div class="progress-bar bg-warning" role="progressbar" style="width: 20%">阶段 2</div>
            <div class="progress-bar bg-danger" role="progressbar" style="width: 15%">阶段 3</div>
        </div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/14.png)

### 3.11 手风琴折叠（Accordion） 
Accordion 是可折叠的内容面板，常用于FAQ或分组信息展示，需要 Bootstrap JS 支持。\
点击按钮可展开或折叠对应内容，collapsed 类表示初始折叠状态，data-bs-parent 保证手风琴效果，即同时只展开一项。
<p>
    <code>accordion</code> 是外层容器，<code>accordion-item</code> 是每个折叠项。<br>
    <code>accordion-header</code> 包含触发按钮 <code>accordion-button</code>，点击按钮折叠/展开内容。<br>
    <code>accordion-collapse collapse</code> 包含折叠内容，可用 <code>show</code> 默认展开。<br>
    <code>data-bs-parent="#id"</code> 保证同一时间只有一个折叠项展开。
</p>

**示例代码：**
```html
<div class="container mb-3">
    <p>基础手风琴示例</p>
    <div class="accordion" id="accordionExample">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseOne">
                    手风琴项 1
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
                <div class="accordion-body">这里是手风琴项 1 的内容。</div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseTwo">
                    手风琴项 2
                </button>
            </h2>
            <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                <div class="accordion-body">这里是手风琴项 2 的内容。</div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseThree">
                    手风琴项 3
                </button>
            </h2>
            <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                <div class="accordion-body">这里是手风琴项 3 的内容。</div>
            </div>
        </div>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/15.png)

### 3.12 加载动画（Spinner）  
Bootstrap 提供内置 Spinner 类，用于显示加载状态或操作等待提示。\
提供旋转环和圆点(呼吸灯)两种类型，内置颜色类直接显示不同状态，可嵌入按钮或表单等界面，提示操作加载中。
<p>
    <code>spinner-border</code> 创建旋转圆环加载，<code>spinner-grow</code> 创建圆点加载。<br>
    <code>text-*</code> 控制颜色。<br>
    <code>role="status"</code> 和 <code>span.visually-hidden</code> 用于辅助无障碍访问。
</p>

**示例代码：**
```html
<div class="container mb-3">
    <p>基础旋转加载示例</p>
    <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">加载中...</span>
    </div>
    <div class="spinner-border text-success" role="status">
        <span class="visually-hidden">加载中...</span>
    </div>
    <div class="spinner-border text-danger" role="status">
        <span class="visually-hidden">加载中...</span>
    </div>

    <p class="mt-3">圆点加载示例</p>
    <div class="spinner-grow text-primary" role="status">
        <span class="visually-hidden">加载中...</span>
    </div>
    <div class="spinner-grow text-success" role="status">
        <span class="visually-hidden">加载中...</span>
    </div>
    <div class="spinner-grow text-danger" role="status">
        <span class="visually-hidden">加载中...</span>
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/16.png)

### 3.13 图片辅助类（Image） 
Bootstrap 提供内置图片辅助类，用于控制图片响应式、圆角或圆形效果。
<p>
    <code>img-fluid</code> 使图片宽度自适应父容器，高度按比例缩放。<br>
    <code>rounded</code> 给图片四个角添加圆角，变体有
    <code>rounded-top</code>、<code>rounded-bottom</code>、<code>rounded-start</code>、<code>rounded-end</code>、<code>rounded-circle</code>（圆形）、<code>rounded-pill</code>（椭圆）。<br>
    <code>img-thumbnail</code> 给图片添加边框和内边距，显示缩略图效果。
</p>

**示例代码：**
```html
<div class="container mb-3 d-flex gap-4">
    <p>演示不同效果，父容器宽度不同，便于观察响应式</p>

    <div class="mb-4" style="width: 300px; background-color: #f8f9fa; padding: 5px;">
        <p>img-fluid（自适应父容器）</p>
        <img src="../../../../img/what_i_learnt/Bootstrap5/placeholder-image.png" class="img-fluid" alt="响应式图片">
    </div>

    <div class="mb-4">
        <p>rounded（轻微圆角）</p>
        <img src="../../../../img/what_i_learnt/Bootstrap5/placeholder-image.png" class="rounded" width="300"
            height="150" alt="圆角矩形">
    </div>

    <div class="mb-4">
        <p>rounded-circle（圆形）</p>
        <img src="../../../../img/what_i_learnt/Bootstrap5/placeholder-image.png" class="rounded-circle"
            width="150" height="150" alt="圆形图片">
    </div>

    <div class="mb-4">
        <p>img-thumbnail（带边框缩略图）</p>
        <img src="../../../../img/what_i_learnt/Bootstrap5/placeholder-image.png" class="img-thumbnail"
            width="300" height="150" alt="缩略图">
    </div>
</div>
```

![title](../../img/what_i_learnt/Bootstrap5/2-utilities/17.png)
