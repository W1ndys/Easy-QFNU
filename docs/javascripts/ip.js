// 检测用户设备是否为移动设备
function isMobileDevice() {
    return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
}

// 如果不是移动设备，则显示图像
if (!isMobileDevice()) {
    // 创建图像元素
    var img = document.createElement("img");
    img.src = "https://tool.lu/netcard/"; // 设置图像的源
    img.alt = "IP image"; // 图像的替代文本
    img.className = "custom-image"; // 添加自定义类名

    // 将图像添加到 body 中
    document.body.appendChild(img);
}
