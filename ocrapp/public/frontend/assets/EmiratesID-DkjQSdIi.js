import{g as c,h as D,i as _,c as n,b as e,j as d,F as h,k as S,l as C,o,t as I,m as E,v as U}from"./index-BQUyCr_P.js";const V={class:"file-container"},B=["src"],R={key:0,class:"flex flex-wrap gap-5"},F=["onUpdate:modelValue"],L={__name:"EmiratesID",setup(j){const u=c({mime:"",content:""}),v=c(),s=c(),a=c(),m=r=>{var l=r.target.files[0];l&&C(l).then(t=>{t=t.split(","),v.value=t,u.value.mime=t[0],u.value.content=t[1]})},p=()=>{b.submit().then(r=>{a.value=r,s.value=a.value})},g=()=>{if(!a.value){console.log("empty");return}k.insert.submit(a.value)},x=()=>{console.log("Image Data:"),console.log(u.value),console.log("Receive Data:"),console.log(a.value),console.log("Unsaved Data:"),console.log(s.value)},b=D({url:"ocrapp.api.eid.getEid",params:{str:u.value}}),f=()=>{console.log("Saved!")},k=_({doctype:"Emirates ID",fields:["*"],auto:!0});return(r,l)=>(o(),n("div",null,[l[2]||(l[2]=e("h1",null,"Hello",-1)),e("div",null,[l[1]||(l[1]=e("h1",{class:"container"},"Image Upload Vue.js",-1)),e("div",null,[e("div",V,[e("div",null,[e("form",null,[e("input",{type:"file",id:"media",accept:"image/png",onChange:l[0]||(l[0]=t=>m(t))},null,32)])])]),e("div",null,[v.value?(o(),n("img",{key:0,src:v.value},null,8,B)):d("",!0)]),e("button",{class:"bg-gray-500 rounded-2xl px-5 mt-2",onClick:p},"Send?"),e("button",{class:"bg-gray-500 rounded-2xl px-5 mt-2",onClick:x},"Print"),e("div",null,[s.value?(o(),n("div",R,[(o(!0),n(h,null,S(s.value,(t,i)=>(o(),n("div",{key:i},[e("p",null,I(i),1),E(e("input",{"onUpdate:modelValue":y=>s.value[i]=y,type:"text"},null,8,F),[[U,s.value[i]]])]))),128))])):d("",!0),a.value?(o(),n("button",{key:1,class:"bg-red-300 rounded-2xl px-5 mt-5",onClick:f},"Save?")):d("",!0),a.value?(o(),n("button",{key:2,class:"bg-red-300 rounded-2xl px-5 mt-5",onClick:g},"Submit?")):d("",!0)])])])]))}};export{L as default};
