---
comments: true
hide:
  - tags
  - navigation
  - footer
  - toc
  - actions
icon: material/home
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

/* 取消统计跳转链接文字的默认链接蓝色*/
.md-typeset .custom-link {
    color: inherit; /* 继承父元素的颜色，即默认文本的颜色 */
    text-decoration: none; /* 取消下划线 */
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
                <span id="announcement" class="content" style="display: none;">欢迎各位曲园学子！欢迎访问Easy-QFNU！</span>
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
- :material-battery-charging-wireless-outline: **新手引导**

    ---

    <u>欢迎来到Easy-QFNU！**[点击这里](/Start/)快速开始**</u>

    请善用<u>**搜索**</u>功能来寻找你想要的内容！！

    在浏览本站前请先阅读 [用户协议](Start/Agreement/){:target="\_blank"}

    [如何发表评论](/Start/Tutorial/#how-to-comment){:target="\_blank"}

    [如何参与编辑](/Start/Data-Submission/){:target="\_blank"}

    [**联系作者**](/Start/#contact){:target="\_blank"}

    [Github开源地址](https://github.com/W1ndys/Easy-QFNU/tree/gh-pages){:target="\_blank"}

</div>

</div>

<div class="grid cards" markdown>
<div class="grid cards" markdown>
- :octicons-alert-16: **公告**

    ---

    欢迎给[本项目](https://github.com/W1ndys/Easy-QFNU/){:target="\_blank"}点个star⭐

    梦想是让每一位曲园学子都看过我的Easy-QFNU，希望大家能喜欢！也希望有越来越多的人参与编辑，一起完善这个项目！

</div>

<div class="grid cards" markdown>
- :fontawesome-solid-newspaper: **NEWS**

    ---

    在开始之前,请先了解本站[用户协议](Start/Agreement/){:target="\_blank"},浏览本站即代表您同意此协议

    加急更新中………………

</div>
<div class="grid cards" markdown>
- :material-advertisements: **广告位招租**

    ---

    联系方式：[w1ndys@outlook.com](mailto:w1ndys@outlook.com){:target="\_blank"}

</div>
</div>

<div class="grid cards" markdown>

<!-- <div class="grid cards" markdown>
- :octicons-repo-16: **源代码仓库概览**

    [![本仓库](https://stats.deeptrain.net/repo/W1ndys/Easy-QFNU?theme=light)](https://github.com/W1ndys/Easy-QFNU)

</div> -->

<div class="grid cards" markdown>
- :material-hand-heart: **源代码贡献者**

    <p align="left">
        <a href="https://github.com/W1ndys/Easy-QFNU/graphs/contributors">
            <img width="100" src="https://contrib.rocks/image?repo=W1ndys/Easy-QFNU" />
        </a>
    </p>

    **向每一个为开源项目做出努力和贡献的人，致以崇高的敬意！！！**

</div>

<div class="grid cards" markdown>
- :simple-simpleanalytics: <a class="custom-link" href="https://v6.51.la/report/overview?comId=416432" target="_blank"><strong>网站资讯</strong></a>

    <!-- 51.La数据挂件 -->
    <script id="LA-DATA-WIDGET" crossorigin="anonymous" charset="UTF-8" src="https://v6-widget.51.la/v6/3HxQRMoHKBJizCgs/quote.js?theme=#6D2424,#6D2424,#6D2424,#6D2424,#FFFFFF,#6D2424,12&col=true&f=14"></script>

</div>

</div>

<script>console.log(`欢迎来到Easy-QFNU!\nhttps://github.com/W1ndys/Easy-QFNU`);</script>
