---

comments: true
---



# 测试页面

## Mathjax & KaTex 测试

$$
\operatorname{ker} f =\{g\in G: f(g)= e_{H}\}{\mbox{.}}
$$

The homomorphism $f$ is injective if and only if its kernel is only the
singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such
that $f(a)=f(b)$.

## 粗体斜体测试

**粗体**         _斜体_

## 标记测试

==标记我== 

^^下划线^^ 

上标^上^

- H~2~O
- A^T^A

## 增删建议

文本可以是 {--已删除--} 和替换文本 {++增加++}。 这也可以
组合成 {~~一个~> 另一个~~} 操作。 {==突出显示==}也是
可能的{>> 并且可以内联添加注释 <<}。

{==

格式化也可以通过将开始和结束应用于块
将标签放在单独的行上，并在标签和内容之间添加新行。

==}

- ==This was marked==
- ^^This was inserted^^
- ~~This was deleted~~

## 代码高亮

```python
import foo.bar
```

```{.python linenums="1"}
import foo.bar
```

```{.python linenums="2"}
import foo.bar
```

``` {.python linenums="1 2"}
    """Some file."""
import foo.bar
import boo.baz
import foo.bar.baz
```

``` {linenums="1 1 2"}
"""Some file."""
import foo.bar
import boo.baz
import foo.bar.baz
```

```{.python hl_lines="1 3"}
"""Some file."""
import foo.bar
import boo.baz
import foo.bar.baz
```

```{.py3 hl_lines="1 3" linenums="2"}
"""Some file."""
import foo.bar
import boo.baz
import foo.bar.baz
```

```{.py3 hl_lines="1-2 5 7-8"}
import foo
import boo.baz
import foo.bar.baz

class Foo:
   def __init__(self):
       self.foo = None
       self.bar = None
       self.baz = None
```

```{.py3 title="My Cool Header"}
import foo.bar
import boo.baz
import foo.bar.baz
```

```python
import foo.bar
import boo.baz
import foo.bar.baz
```

```pycon
>>> 3 + 3
6
```

## 内联代码块

The `#!python range()` function is used to generate a sequence of numbers.

## 键盘按键

++ctrl+alt+del++

## 智能符号

(tm)

(c)

(r)

c/o

+/-

-->

<--

<-->

=/=

1/4, etc.

1st 2nd etc.

## 术语表

The HTML specification is maintained by the W3C.

## 嵌入外部文件

--8<-- "docs/嵌入测试.md"

--8<--
docs/嵌入测试.md
--8<--

## 图

### 流程图

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

### 序列图

``` mermaid
sequenceDiagram
  autonumber
  Alice->>John: Hello John, how are you?
  loop Healthcheck
      John->>John: Fight against hypochondria
  end
  Note right of John: Rational thoughts!
  John-->>Alice: Great!
  John->>Bob: How about you?
  Bob-->>John: Jolly good!
```

### 状态图

``` mermaid
stateDiagram-v2
  state fork_state <<fork>>
    [*] --> fork_state
    fork_state --> State2
    fork_state --> State3

    state join_state <<join>>
    State2 --> join_state
    State3 --> join_state
    join_state --> State4
    State4 --> [*]
```

### 类图

``` mermaid
classDiagram
  Person <|-- Student
  Person <|-- Professor
  Person : +String name
  Person : +String phoneNumber
  Person : +String emailAddress
  Person: +purchaseParkingPass()
  Address "1" <-- "0..1" Person:lives at
  class Student{
    +int studentNumber
    +int averageMark
    +isEligibleToEnrol()
    +getSeminarsTaken()
  }
  class Professor{
    +int salary
  }
  class Address{
    +String street
    +String city
    +String state
    +int postalCode
    +String country
    -validate()
    +outputAsLabel()  
  }
```

### 实体关系图

``` mermaid
erDiagram
  CUSTOMER ||--o{ ORDER : places
  ORDER ||--|{ LINE-ITEM : contains
  LINE-ITEM {
    string name
    int pricePerUnit
  }
  CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

除了上面列出的图表类型之外，Mermaid.js 还提供对饼图、甘特图、用户旅程、git 图和需求图的支持，所有这些都未得到 Material for MkDocs 的正式支持。 这些图表应该仍然像 Mermaid.js 所宣传的那样工作，但我们不认为它们是一个好的选择，主要是因为它们在移动设备上工作得不好。

## 选项卡

### 常见的

=== "Tab 1"
    Markdown **content**.

    Multiple paragraphs.

=== "Tab 2"
    More Markdown **content**.

    - list item a
    - list item b

### 连续两个

=== "Tab 1"
    Markdown **content**.

    Multiple paragraphs.

=== "Tab 2"
    More Markdown **content**.

    - list item a
    - list item b

===! "Tab A"
    Different tab set.

=== "Tab B"
    ```
    More content.
    ```

### 指定指定默认选择

=== "Not Me"
    Markdown **content**.

    Multiple paragraphs.

===+ "Select Me"
    More Markdown **content**.

    - list item a
    - list item b

=== "Not Me Either"
    Another Tab

### 选项卡ID

ID

=== "tab"
    content

## 任务列表

Task List

-   [X] item 1
    *   [X] item A
    *   [ ] item B
        more text
        +   [x] item a
        +   [ ] item b
        +   [x] item c
    *   [X] item C
-   [ ] item 2
-   [ ] item 3

## 云上曲园

云上曲园
