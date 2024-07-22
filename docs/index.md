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
<!-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— -->

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
                <span id="announcement" class="content" style="display: none;">欢迎访问Easy-QFNU！</span>
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

![Easy-QFNU](https://socialify.git.ci/W1ndys/Easy-QFNU/image?description=1&font=Inter&forks=1&issues=1&language=1&logo=https%3A%2F%2Feasy-qfnu.top%2Fassets%2Flogo%2Ffavico.png&owner=1&pattern=Signal&pulls=1&stargazers=1&theme=Auto)

欢迎你找到这里，[Easy-QFNU](https://Easy-QFNU.top) 是免费、开源、共建、共享的曲师大学生手册，隶属于 [W1ndys](https://github.com/W1ndys) ，打破你的信息差，致力于让你的 QFNU 更简单~

<!-- Easy-QFNU 的前身是 [曲阜师范大学选课指北](https://blog.w1ndys.top/posts/216d9006#/){target ="\_blank "} 和 [曲阜师范大学速通指南](https://blog.w1ndys.top/posts/8f8bbaa8){target ="\_blank "} -->

## Easy-QFNU

<div class="grid cards" markdown>
- **[快速了解本站](/Start/)**-Easy-QFNU，让你的 QFNU 更简单
</div>

### Easy-校园

Easy-校园的前身是 [曲阜师范大学速通指南](https://blog.w1ndys.top/posts/8f8bbaa8){target ="\_blank "}，是一个收集汇总校园生活常用信息的 wiki ，帮助你快速找到适合自己的信息。现已合并到 Easy-QFNU 项目中，并增加更多内容。

<div class="grid cards" markdown>
- **[Easy-校园](/Easy-School/)**-校园生活常用信息汇总
</div>

### Easy-选课

Easy-选课的前身是 [曲阜师范大学选课指北](https://blog.w1ndys.top/posts/216d9006#/){target ="\_blank "}，是一个收集汇总选课推荐的 wiki ，帮助你快速找到适合自己的课程。现已合并到 Easy-QFNU 项目中，并增加更多内容。

<div class="grid cards" markdown>

- **[Easy-选课](/Easy-SelectCourse/)**-选课指北
- **[培养方案](/Easy-SelectCourse/Curriculum/)**-内含各年级培养方案文件
- **[选课指北](/Easy-SelectCourse/Selection-Guide/)**-手把手教你选课
- **[选课推荐](/Easy-SelectCourse/Curriculum-Recommend/)**-推荐优质课程
</div>

### Easy-学院

<div class="grid cards" markdown>
- **[Easy-学院](/Easy-College/)**-是 Easy-QFNU 项目产生后新建的一部分，旨在为各学院提供更细致的知识库，帮助同学们更好地了解各学院。欢迎各位学院同学投稿，共建知识库。
</div>

### 赞助我们

如果您觉得 Easy-QFNU 帮助到了你，想通过赞助支持我，欢迎赞助。

<div class="grid cards" markdown>
- **[赞助计划](https://easy-qfnu.top/Start/Sponsor/)**-本站开启了赞助计划，赞助的金额将用于服务器维护、网站建设、内容更新、以及其他相关事宜。
</div>
