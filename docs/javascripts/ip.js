// 检测用户设备是否为移动设备
function isMobileDevice() {
    return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
}

// 如果不是移动设备，则显示图像
if (!isMobileDevice()) {
    // 创建图像元素
    var img = document.createElement("img");
    img.src = "https://tool.lu/netcard/"; // 设置图像的源
    img.alt = "Your Image"; // 图像的替代文本

    // 设置图像样式
    img.style.position = "fixed";
    img.style.bottom = "0";
    img.style.right = "0";
    img.style.zIndex = "999"; // 确保图片在最上层
    img.style.animationName = "slideIn"; // 应用入场动画
    img.style.animationDuration = "1s";
    img.style.animationTimingFunction = "ease-in-out";

    // 设置图片大小
    img.style.width = "350px"; // 设置图片宽度
    img.style.height = "auto"; // 设置高度自动调整，保持宽高比

    // 将图像添加到 body 中
    document.body.appendChild(img);
}
