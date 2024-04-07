---
comments: true
# template: home.html ## 留给后期
# tags:
#   - 首页
#   - 首页集
hide:
  - tags
  - navigation
  - footer
  - toc
  - actions
---

<!-- 下面是随机诗句和公告的切换全部配置 -->
<!-- ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— -->

<style>
/* CSS样式 */
.shijuannounce {
    display: flex;
    align-items: center; /* 垂直居中 */
    justify-content: center; /* 水平居中 */
}

.content-container {
    position: relative;
    height: 23px; /* 根据内容高度调整 */
    overflow: hidden;
}

.content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    transition: transform 0.5s ease; /* 调整过渡时间和缓动函数 */
}
</style>

<!-- 诗词一言接口，来自https://www.jinrishici.com/#/ -->
<!-- 生产环境请注释掉，以免过高的访问次数导致封禁IP -->
<!-- 又加了公告切换功能 -->
<div class="grid cards shijuannounce" style="text-align: center">
    <ul>
        <li>
            <div id="content" class="content-container">
                <!-- 随机诗句 -->
                <span id="jinrishici-sentence" class="content">随机诗句加载中</span>
                <script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
                <!-- 公告 -->
                <span id="announcement" class="content" style="display: none;">呜呜呜废了很长时间才做出来个切换设计😭...</span>
            </div>
        </li>
    </ul>
</div>

<script>
// 切换显示内容
function toggleContent() {
    const jinrishiciSentence = document.getElementById('jinrishici-sentence');
    const announcement = document.getElementById('announcement');

    if (jinrishiciSentence.style.display === 'block') {
        jinrishiciSentence.style.transform = 'translateY(-100%)';
        announcement.style.display = 'block';
        setTimeout(() => {
            announcement.style.transform = 'translateY(0)';
            jinrishiciSentence.style.display = 'none';
        }, 500); // 根据你的过渡时间调整
    } else {
        announcement.style.transform = 'translateY(-100%)';
        jinrishiciSentence.style.display = 'block';
        setTimeout(() => {
            jinrishiciSentence.style.transform = 'translateY(0)';
            announcement.style.display = 'none';
        }, 500); // 根据你的过渡时间调整
    }
}

// 定时切换内容
setInterval(() => {
    toggleContent();
}, 3200); // 调整切换间隔时间
</script>

<!-- 上面是随机诗句和公告的切换全部配置 -->
<!-- ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— -->

<div class="grid cards" markdown>

<div class="grid cards" markdown>
-   :fontawesome-solid-newspaper: **NEWS**

    ---

    在开始之前,请先了解本站[用户协议](/start/agreement/){:target="\_blank"},浏览本站即代表您同意此协议

    梦开始的地方，点击快速开始-->[快速开始](/start/)

    加急更新中………………

</div>

</div>

<div class="grid cards" markdown>

<div class="grid cards" markdown>
-   :octicons-alert-16: **公告**

    ---

    欢迎给[本项目](https://github.com/W1ndys/Easy-QFNU/){:target="\_blank"}点个star⭐

</div>

<div class="grid cards" markdown>
-   :material-battery-charging-wireless-outline: **使用须知**

    ---

    请善用搜索功能来寻找你想要的内容！！

    [如何发表评论](/start/tutorial/#how-to-comment){:target="\_blank"}

    [如何参与编辑](/start/Data-submission/){:target="\_blank"}

    [联系作者](){:target="\_blank"}

    [Github开源地址](https://github.com/W1ndys/Easy-QFNU/tree/gh-pages){:target="\_blank"}

</div>

</div>

<div class="grid cards" markdown>

<div class="grid cards" markdown>
-   :octicons-repo-16: **源代码仓库概览**

    [![本仓库](https://stats.deeptrain.net/repo/W1ndys/ezqfnu.w1ndys.top?theme=light)](https://github.com/W1ndys/Easy-QFNU)

</div>

<div class="grid cards" markdown>
-   :material-hand-heart: **源代码贡献者**

    [![源代码贡献者](https://stats.deeptrain.net/contributor/W1ndys/Easy-QFNU/?column=7&theme=light)](https://github.com/W1ndys/Easy-QFNU/graphs/contributors){:target="\_blank"}

    **向每一个为开源项目做出努力和贡献的人，致以崇高的敬意！！！**

</div>

</div>

<br><br><br><br><br><br>

<font color="red">下面是以前的 index.md</font>

---

# Easy-QFNU

## **选课指北**

<span style="color:#FF0000;">该网站正在建设中,选课指北的运行地址为：</span>[https://blog.w1ndys.top/posts/216d9006.html](https://blog.w1ndys.top/posts/216d9006.html){:target="\_blank"}

下面是关于选课指北的小背景

---

有不少人知道,W1ndys 师傅在 2023 年 8 月做了一个选课指北网站,随着时间的推移,网站的服务人数越来越多,W1ndys 师傅发现地址太长了,肯定都记不住,所以 W1ndys 师傅打算迁移站点,设置一个好记的独立域名

于是有了这个域名：[https://xkzb.qfnu.w1ndys.top](https://xkzb.qfnu.w1ndys.top)

但是这个域名的页面内容还在设计中,你现在看到的是一个开发中页面

提前透漏一波：

选课指北未来的计划包括了以下内容：

- 体育课
- 公选课
- 选什么
- 怎么选
- 怎么查
- 鉴赏课
- 学分规定
- 培养计划

等方面陆续讲解上传

## **速通指南**

大家比较耳熟能详的是选课指北,然而少有人知道,W1ndys 师傅的另一个公益项目“**曲阜师范大学速通指南**”。

速通指南的宗旨是：尽可能提到你在学校可能遇到的各种问题,并给出相关解释或解决办法。

传送门：[https://stzn.qfnu.w1ndys.top](https://stzn.qfnu.w1ndys.top){:target="\_blank"}

但是现在也是初步完善阶段,许许多多的内容等待完善。

我们已经提到的问题有：

- 称呼问题
- 军训问题
- 宿舍问题
- 快递问题
- 药店问题
- 作息时间表
- 校区地图
- 化学与化工学院培养方案讲解
- 数学科学学院速通指南

我们欢迎你提供各种有效信息,期待你的加入

---

:material-clock-edit-outline:{ title="修改日期" } 2024-04-07
:material-clock-plus-outline:{ title="创建日期" } 2024-02-29
