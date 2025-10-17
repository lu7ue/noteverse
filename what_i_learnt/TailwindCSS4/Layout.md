# Layout 布局
> 点击**蓝色字体**标题，可跳转至该章节的TailwindCSS4官方文档查看详情。
> 或，到我的[仓库](https://github.com/own-place/self-study-and-uni-courses/tree/main/00_Self_Study/tailwindcss4-notes)看代码（注：超混乱，最好还是去看官方文档跟问gpt...

## [基础尺寸](https://tailwindcss.com/docs/width)
h-screen(整个视口高度)适用于PC端，h-dvh(动态视口高度)适用于移动端。  
w-和h-后面都可以用数字(w-96)、分数(w-1/2)、full(占满父容器可用宽/高度)、screen(占满整个视口宽/高度)、auto(只包裹内容)，或指定数值(w-[32rem]) 
除此之外，还有max-w-*和min-w-*、max-h-*和min-h-*设置最大和最小宽/高度，确保在不同屏幕或布局下不影响显示的元素。
```html
<div class="w-80 h-24 bg-gray-200">
    <div class="w-full bg-blue-300">w-full：占满父容器可用宽度</div>
</div>

<div class="w-80 h-24 bg-gray-200">
    <div class="w-auto bg-green-300">w-auto：只包裹内容</div>
</div>

<div class="w-80 h-24 bg-gray-200">
    <div class="w-screen bg-red-300">w-screen：占满整个视口宽度</div>
</div>

<div class="w-80 h-24 bg-gray-300">
    <div class="w-2/3 bg-yellow-300">w-2/3：占满父容器的 2/3 宽度</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/0a749c1b-ed02-4075-ad49-104829f5ac66" />

## [距离](https://tailwindcss.com/docs/padding)
Padding和margin的区别在于，Padding是元素内容与边框之间的空间(向内)，而Margin是元素边框与其他元素之间的空间(向外)。
它们都使用相同的设置方法，比如：p-8(四个方向), pl-8(左), pr-8(右), pt-8(上), pb-8(下)，px-8(左右), py-8(上下)；或者用p-[2px]指定数值。

## 背景
[背景附着](https://tailwindcss.com/docs/background-attachment) -> 有三种形式：背景固定在屏幕上；文字移动时背景一起滚动；文字移动时背景不动。
[背景图像](https://tailwindcss.com/docs/background-image) -> 有两种形式：引入图片作为背景，或使用渐变色作为背景。
[背景重复](https://tailwindcss.com/docs/background-repeat) -> 平铺某个图像作为背景。
[背景尺寸](https://tailwindcss.com/docs/background-size) -> 设置背景图像的尺寸：cover(放大到完全适应容器)、contain(放大到适应容器的高/宽)、auto(使用图片默认尺寸)。

## [显示](https://tailwindcss.com/docs/display)
block 块级元素：每个元素独占一整行。
```html
<div class="border p-2 bg-blue-100">
    <span class="block bg-blue-300">我是 block 1</span>
    <span class="block bg-blue-300">我是 block 2</span>
    <span class="block bg-blue-300">我是 block 3</span>
</div>
```  
inline 行内元素：元素在一行里显示，不会换行，但无法设置宽高。
```html
<div class="border p-2 bg-green-100">
    <span class="inline bg-green-300">我是 inline 1</span>
    <span class="inline bg-green-300">我是 inline 2</span>
    <span class="inline bg-green-300">我是 inline 3</span>
</div>
``` 
inline-block 行内块：像 inline 一样在一行，但可设置宽高。
inline-block 默认是基线对齐，所以常常出现“不在一条线上”的情况。用 align-top、align-middle、align-bottom 就能控制对齐方式。
```html
<div class="border p-2 bg-yellow-100">
    <span class="inline-block align-top bg-yellow-300 w-24 h-10 text-center">inline-block 11</span>
    <span class="inline-block align-top bg-yellow-300 w-24 h-10 text-center">inline-block 22</span>
    <span class="inline-block align-top bg-yellow-300 w-24 h-10 text-center">inline-block 33</span>
</div>
``` 
hidden 隐藏元素：hidden 的元素不会渲染，占位也消失。
```html
<div class="border p-2 bg-red-100">
    <span class="bg-red-300">可见 1</span>
    <span class="hidden bg-red-300">我是 hidden 你看不到我</span>
    <span class="bg-red-300">可见 2</span>
</div>
``` 
<img width="1000" src="https://github.com/user-attachments/assets/2f7cd8dc-bd2b-48c4-a954-e6fa738b86b8" />

## Flexbox
Flexbox 是一种一维布局模型，适用于在一个方向上（行或列）分配空间和对齐内容。
要使用 Flexbox，只需在父元素上添加 flex 类，然后可以使用各种子类来控制子元素的对齐和分布。

### [排列](https://tailwindcss.com/docs/flex-direction)
正方向排列(横) flex-row
```html
<div class="flex flex-row bg-gray-300 w-[800px] h-[80px] mt-4">
    <div class="basis-1/4 bg-red-500 h-[50px] mr-1">01</div>
    <div class="basis-1/4 bg-orange-500 h-[50px] mr-1">02</div>
    <div class="basis-2/4 bg-yellow-500 h-[50px] mr-1">03</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/a2170e3e-0048-4866-87d5-6bb1f3d0f920" />

反方向排列(横) flex-row-reverse
```html
<div class="flex flex-row-reverse bg-gray-300 w-[800px] h-[80px] mt-4">
    <div class="basis-1/4 bg-red-500 h-[50px] mr-1">01</div>
    <div class="basis-1/4 bg-orange-500 h-[50px] mr-1">02</div>
    <div class="basis-2/4 bg-yellow-500 h-[50px] mr-1">03</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/bafe6ca3-f5de-4bd1-a3bd-299d534580fd" />

正方向排列(竖) flex-col
```html
<div class="flex flex-col bg-gray-300 w-[120px] h-[100px] mt-4">
    <div class="basis-1/4 bg-red-500 w-[100px] mb-1">01</div>
    <div class="basis-1/4 bg-orange-500 w-[100px] mb-1">02</div>
    <div class="basis-2/4 bg-yellow-500 w-[100px] mb-1">03</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/15d7c285-cb65-463b-be7a-49332fd1cb20" />

反方向排列(竖) flex-col-reverse  
```html
<div class="flex flex-col-reverse bg-gray-300 w-[120px] h-[100px] mt-4">
    <div class="basis-1/4 bg-red-500 w-[100px] mb-1">01</div>
    <div class="basis-1/4 bg-orange-500 w-[100px] mb-1">02</div>
    <div class="basis-2/4 bg-yellow-500 w-[100px] mb-1">03</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/0a9250df-b08c-459d-926e-55ae4fa43ced" />

### [换行](https://tailwindcss.com/docs/flex-wrap)
父容器只有 500px，但每个子元素固定 200px，三个一行就需要 600px → 超出，于是触发换行。h-auto使高度可以随内容变化。  
```html
<div class="flex flex-row flex-wrap bg-gray-300 w-[500px] h-auto mt-4">
    <div class="w-[200px] h-[50px] bg-red-500 mr-1 mb-1">01</div>
    <div class="w-[200px] h-[50px] bg-orange-500 mr-1 mb-1">02</div>
    <div class="w-[200px] h-[50px] bg-yellow-500 mr-1 mb-1">03</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/6f53f6fd-cd15-4485-a49b-a9e11281ba85" />

### [Flex伸缩](https://tailwindcss.com/docs/flex)
flex-1 均分剩余空间
```html
<div class="flex bg-gray-200 w-[600px] h-[80px]">
    <div class="flex-1 bg-red-300 flex items-center justify-center">短</div>
    <div class="flex-1 bg-blue-300 flex items-center justify-center">中等文字</div>
    <div class="flex-1 bg-green-300 flex items-center justify-center">很长很长很长的文字</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/5241bdba-cf6e-46cf-ba62-497f755fd5bb" />

flex-auto 根据内容伸缩  
```html
<div class="flex bg-gray-200 w-[600px] h-[80px]">
    <div class="flex-auto bg-red-300 flex items-center justify-center">短</div>
    <div class="flex-auto bg-blue-300 flex items-center justify-center">中等文字</div>
    <div class="flex-auto bg-green-300 flex items-center justify-center">很长很长很长的文字</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/b00047c1-8c8a-464a-b1ff-3311be7ee99a" />

### [排列顺序](https://tailwindcss.com/docs/order)
order-1：给子元素排序：01在最后(order-3)， 02在最前(order-1)，03在中间(order-2)
```html
<div class="flex justify-between bg-gray-200 w-[300px] h-[80px]">
    <div class="order-3 bg-red-300 flex items-center justify-center">01</div>
    <div class="order-1 bg-blue-300 flex items-center justify-center">02</div>
    <div class="order-2 bg-green-300 flex items-center justify-center">03</div>
</div>
```
<img width="300" src="https://github.com/user-attachments/assets/54d55677-55a0-470c-8791-b277a074e762" />

order-last：给子元素排序：01在最后(order-last)， 02在最前(order-first)，03在中间 
```html
<div class="flex justify-between bg-gray-200 w-[300px] h-[80px]">
    <div class="order-last bg-red-300 flex items-center justify-center">01</div>
    <div class="order-first bg-blue-300 flex items-center justify-center">02</div>
    <div class="bg-green-300 flex items-center justify-center">03</div>
</div>
```
<img width="300" src="https://github.com/user-attachments/assets/da5af741-4c34-4d82-9760-896f478e28f6" />

## Grid
Grid 是一种二维布局模型，适用于在行和列上分配空间和对齐内容。
要使用 Grid，只需在父元素上添加 grid 类，然后可以使用各种子类来控制子元素的对齐和分布。
### [列](https://tailwindcss.com/docs/grid-template-columns)
```html
<div class="grid grid-cols-3 gap-4 bg-gray-200 w-[300px] h-[80px]">
    <div class="bg-red-300 flex items-center justify-center">01</div>
    <div class="bg-blue-300 flex items-center justify-center">02</div>
    <div class="bg-green-300 flex items-center justify-center">03</div>
    <div class="bg-orange-300 flex items-center justify-center">04</div>
    <div class="bg-purple-300 flex items-center justify-center">05</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/d8befbac-a981-4ab1-8a23-652cb24a97be" />

### [列延展](https://tailwindcss.com/docs/grid-column)
在想延展的子元素上使用col-span-*，col-span-2代表延展成两格 
```html
<div class="grid grid-cols-3 gap-4 bg-gray-200 w-[300px] h-[80px]">
    <div class="bg-red-300 flex items-center justify-center">01</div>
    <div class="bg-blue-300 flex items-center justify-center">02</div>
    <div class="bg-green-300 flex items-center justify-center">03</div>
    <div class="col-span-2 bg-orange-300 flex items-center justify-center">04</div>
    <div class="bg-purple-300 flex items-center justify-center">05</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/66e4fe62-369a-4009-8ec6-d6ea951c397c" />

col-start-n = 从 第 n 条网格线 开始，col-end-n = 到 第 n 条网格线 结束（但不包含该线本身右边的列）
<img width="300" src="https://github.com/user-attachments/assets/d939fe74-7cff-48f7-a2f1-cfe8e063bebe" />
```html
<div class="grid grid-cols-6 gap-4 bg-gray-200 w-[300px] h-[80px]">
    <div class="col-span-4 col-start-2 bg-red-300 flex items-center justify-center">01</div>
    <div class="col-start-1 col-end-3 bg-blue-300 flex items-center justify-center">02</div>
    <div class="col-span-2 col-end-7 bg-green-300 flex items-center justify-center">03</div>
    <div class="col-start-1 col-end-7 bg-orange-300 flex items-center justify-center">04</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/be008497-3ca9-4a71-8aeb-2b0cf6609ff8" />

### [行](https://tailwindcss.com/docs/grid-template-rows)
Grid Row 用于控制元素在网格的行方向上的跨度和位置。 
<img width="500" src="https://github.com/user-attachments/assets/48ed2de1-dfae-4af7-a482-d7ea791c09a4" />

### [行延展](https://tailwindcss.com/docs/grid-row)
```html
<div class="grid grid-flow-col grid-rows-3 gap-4">
  <div class="row-span-3 ...">01</div>
  <div class="col-span-2 ...">02</div>
  <div class="col-span-2 row-span-2 ...">03</div>
</div>
```
<img width="500" src="https://github.com/user-attachments/assets/aad1b42f-a700-45a6-a499-6f0c64eaf007" />

```html
<div class="grid grid-flow-col grid-rows-3 gap-4">
  <div class="row-span-2 row-start-2 ...">01</div>
  <div class="row-span-2 row-end-3 ...">02</div>
  <div class="row-start-1 row-end-4 ...">03</div>
</div>
```
<img width="622" height="211" alt="Image" src="https://github.com/user-attachments/assets/441ff35d-be49-40ed-8d1b-e43b44054196" />

### [间距](https://tailwindcss.com/docs/gap)
gap 用于设置网格行和列之间的间距。
- gap → 行和列的间距都设置
- gap-x → 只控制列与列之间的间距（水平间距）
- gap-y → 只控制行与行之间的间距（垂直间距）
<img width="300" src="https://github.com/user-attachments/assets/d149da33-28ff-4cbf-8eeb-504dc4b8e3db" />

## 对齐
在 flex 里，主轴可能是水平（flex-row）也可能是垂直（flex-col），所以 justify-* 控制的对齐是跟着主轴方向变化的，而此时  align-* 控制的对齐则刚好与 justify-* 相反。
在 grid 里，justify-* 控制水平方向，align-* 控制垂直方向。

| 方式       | Flex (横向 row)        | Flex (竖向 col)        | Grid              |
|------------|------------------------|------------------------|-------------------|
| justify-*  | 控制横向               | 控制竖向               | 控制横向          |
| align-*    | 控制竖向               | 控制横向               | 控制竖向          |
| place-*    | 同时控制横向+竖向      | 同时控制横向+竖向      | 同时控制横向+竖向 |

### [justify-*](https://tailwindcss.com/docs/justify-content)
控制主轴对齐（是水平还是垂直对齐，取决于 flex-row / flex-col） 

flex-row 下：justify-center → 横向居中
```html
<div class="flex flex-row justify-center bg-gray-200 w-[400px] h-[80px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/cd8aaec7-104f-4f21-88c6-fc03a6a251f3" />

flex-col 下：justify-center → 竖向居中
```html
<div class="flex flex-col justify-center bg-gray-200 w-[100px] h-[150px]">
    <div class="bg-blue-300 w-[60px] h-[40px]">B</div>
</div>
```
<img width="200" src="https://github.com/user-attachments/assets/7fabde6b-a9ed-43b7-add4-871258d3c97f" />

### [align-*](https://tailwindcss.com/docs/align-items)
items-start: 竖向排列时 → 顶部对齐 
```html
<div class="flex items-start bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[70px]">B</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/8e607402-15ec-430d-94cb-87a02fd693b8" />

items-center: 竖向排列时 → 垂直居中
```html
<div class="flex items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[70px]">B</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/5c58f2ed-75d1-4600-b9ed-8c85d2c4f3dd" />

### [place-*](https://tailwindcss.com/docs/place-content)
同时控制主轴和交叉轴对齐 

place-items-center: 横向 + 竖向 居中
```html
<div class="grid place-items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/790f371b-dda8-45d2-8830-717452da7029" />

place-items-start: 横向 + 竖向 都在起始位置
```html
<div class="grid place-items-start bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/891efb2c-369b-4d5c-8fbc-8f4a50a077aa" />

### [items-* 与 self-*](https://tailwindcss.com/docs/align-items)
- items-* ：控制容器内所有子项  
- self-* ：控制单个子项（会覆盖父级的 items-* 设置）

### [justify-items-* 与 justify-self-*](https://tailwindcss.com/docs/justify-items)
justify-items-* 控制所有子项水平对齐   
```html
<div class="grid grid-cols-3 justify-items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[40px]">B</div>
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>

<div class="grid grid-cols-3 justify-items-end bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[40px]">B</div>
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/35dca699-dde2-4389-b518-1829eecae492" />

justify-self-* 单独控制子项水平对齐 
```html
<div class="grid grid-cols-3 justify-items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[40px] justify-self-end">B</div>
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/e845021d-bc3a-4710-91f7-379f123c1097" />

### [align-items-* 与 align-self-*](https://tailwindcss.com/docs/align-self)
align-items-* 控制所有子项垂直对齐  
```html
<div class="grid grid-cols-3 align-items-start bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[60px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[60px]">B</div>
    <div class="bg-green-300 w-[60px] h-[60px]">C</div>
</div>

<div class="grid grid-cols-3 items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[60px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[60px]">B</div>
    <div class="bg-green-300 w-[60px] h-[60px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/e9399bdb-9a29-4b0c-bb1c-cf0a16ee5161" />

align-self-* 单独控制子项垂直对齐  
```html
<div class="grid grid-cols-3 items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[60px]">A</div>
    <div class="self-end bg-blue-300 w-[60px] h-[60px]">B</div>
    <div class="bg-green-300 w-[60px] h-[60px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/cf0f3eaa-18c8-4b3c-b2a8-1d948c2aa310" />

### [place-items-* 与 place-self-*](https://tailwindcss.com/docs/place-self)
place-items-* 控制所有子项水平+垂直对齐
```html
<div class="grid grid-cols-3 place-items-center bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px]">A</div>
    <div class="bg-blue-300 w-[60px] h-[40px]">B</div>
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/8fa0b5f9-af41-4bac-b07f-3956c5fb8f51" />

place-self-* 单独覆盖子项对齐  
```html
<div class="grid grid-cols-3 place-items-start bg-gray-200 w-[400px] h-[100px]">
    <div class="bg-red-300 w-[60px] h-[40px] place-self-center">A</div>
    <div class="bg-blue-300 w-[60px] h-[40px]">B</div>
    <div class="bg-green-300 w-[60px] h-[40px]">C</div>
</div>
```
<img width="600" src="https://github.com/user-attachments/assets/ee21f63f-ebec-4b95-a338-aaaaae0d2576" />
