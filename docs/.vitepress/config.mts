import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'zh-CN',
  title: '曲阜师范大学选课指北',
  //titleTemplate: '另起标题覆盖title'
  description: '由W1ndys运营维护的公益项目',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    //导航
    nav: [
      { text: 'Home', link: '/' }, 
      { text: 'Examples', link: '/markdown-examples' }
    ],
    //侧边栏
    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],
    //社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})