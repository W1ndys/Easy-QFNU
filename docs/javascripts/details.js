document.querySelectorAll('details').forEach(details => {
    details.addEventListener('toggle', () => {
        if (details.open) {
            // 获取 details 中内容的实际高度
            const contentHeight = Array.from(details.children)
                .filter(child => child.tagName !== 'SUMMARY')
                .reduce((acc, child) => acc + child.scrollHeight, 0);
            details.style.maxHeight = `${contentHeight + details.querySelector('summary').scrollHeight}px`;
        } else {
            details.style.maxHeight = '1.5em'; // 只显示 summary 的高度
        }
    });

    // 初始化：如果 details 默认是打开的，设置正确的 max-height
    if (details.open) {
        const contentHeight = Array.from(details.children)
            .filter(child => child.tagName !== 'SUMMARY')
            .reduce((acc, child) => acc + child.scrollHeight, 0);
        details.style.maxHeight = `${contentHeight + details.querySelector('summary').scrollHeight}px`;
    }
});
