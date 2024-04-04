// 检测用户设备是否为移动设备
function isMobileDevice() {
    return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
}

// 如果不是移动设备，并且在首页，则显示图像
if (!isMobileDevice() && window.location.pathname === '/') {
    // 创建图像元素
    var img = document.createElement("img");
    img.src = "https://tool.lu/netcard/"; // 设置图像的源
    img.alt = "IP Image"; // 图像的替代文本
    img.className = "IP-image"; // 添加自定义类名

    // 添加入场动画
    img.style.animationName = "slideIn"; // 应用入场动画

    // 将图像添加到 body 中
    document.body.appendChild(img);

    // 设置定时器，在10秒后自动隐藏图片
    setTimeout(function () {
        // 添加出场动画
        img.style.animationName = "slideOut"; // 应用消失动画
        // 监听动画结束事件，触发消失动画
        img.addEventListener("animationend", function () {
            img.style.display = "none"; // 隐藏图片
        });
    }, 10000); // 10000毫秒 = 10秒
}
