import{s as p,C as r,I as d,a,b as c,c as v,w as E,P as N,d as T}from"./app-mDV3zSEr.js";var m=(l,o)=>{p({app:l,id:T,label:N,packageName:"@vuepress/client",homepage:"https://vuepress.vuejs.org",logo:"https://vuepress.vuejs.org/images/hero.png",componentStateTypes:[r]},n=>{const u=Object.entries(o),i=Object.keys(o),I=Object.values(o);n.on.inspectComponent(e=>{e.instanceData.state.push(...u.map(([s,t])=>({type:r,editable:!1,key:s,value:t.value})))}),n.addInspector({id:a,label:d,icon:"article"}),n.on.getInspectorTree(e=>{e.inspectorId===a&&(e.rootNodes=Object.values(c).map(s=>({id:s.id,label:s.label,children:s.keys.map(t=>({id:t,label:t}))})))}),n.on.getInspectorState(e=>{if(e.inspectorId!==a)return;const s=c[e.nodeId];if(s){e.state={[s.label]:s.keys.map(t=>({key:t,value:o[t].value}))};return}i.includes(e.nodeId)&&(e.state={[v]:[{key:e.nodeId,value:o[e.nodeId].value}]})}),E(I,()=>{n.notifyComponentUpdate(),n.sendInspectorState(a)})})};export{m as setupDevtools};
