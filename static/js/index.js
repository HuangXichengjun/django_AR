// 获取各个变量
// 需要改变的
var p_text1_1_h2=document.querySelector(".p-text1-1 h2")
var p_text1_1_p=document.querySelector(".p-text1-1 p")
var p_text1_1_a=document.querySelector(".p-text1-1 a")
var p_img1=document.querySelector(".p-img1 img")
// 获取事件的
var p_name=document.querySelectorAll(".produce-name")
var p_names=document.querySelector(".produce-names")
var edit=[{
        title:"AR眼镜",
        content:"这些设备通常直接戴在用户的眼睛上，提供信息提示、导航、翻译等功能。",
        link:"../static/html/AR眼镜.html",
        img:"http://www.fly-tech.com.cn/uploads/allimg/191128/1139495062-3.jpg",
    },{
        title:"分体式AR眼镜",
        content:"与一体式AR眼镜不同，分体式AR眼镜通常需要连接到外部设备，如智能手机或专用的主机盒子，以提供更强大的计算能力和更长的使用时间。",
        link:"../static/html/分体式AR眼镜.html",
        img:"https://file.abvr360.com/105/uploads/2022/05/202205180320362797.png!a",
    },{
        title:"AR头显",
        content:"这些设备通常比AR眼镜更大，提供更沉浸式的体验，适用于游戏、教育和专业培训等领域。",
        link:"../static/html/AR头显.html",
        img:"http://www.fly-tech.com.cn/uploads/allimg/191128/11394960N-0.jpg",
    },{
        title:"AR应用",
        content:"许多智能手机和平板电脑上都有AR应用，用户可以通过摄像头看到叠加在现实世界中的虚拟图像",
        link:"../static/html/AR应用.html",
        img:"http://www.fly-tech.com.cn/uploads/allimg/191128/1139493500-2.jpg",
    },{
        title:"专业级AR设备",
        content:"这些设备通常用于工业、医疗或军事领域，提供高级的AR功能，如3D模型叠加、远程专家指导等。",
        link:"../static/html/专业级AR设备.html",
        img:"https://ar-scene-source.nosdn.127.net/b6cec1cb6e42f8ea3704f9d702682a91.png",
    }
]


// 获取鼠标事件
var ii=0;
p_name[0].className="produce-name nav-choose";
// 函数：鼠标选中后改变ii的值
p_name[0].onclick=function(){
    p_name[ii].className="produce-name";
    ii=0;
    p_name[0].className="produce-name nav-choose";
    p_text1_1_h2.innerHTML=edit[0].title;
    p_text1_1_p.innerHTML=edit[0].content;
    p_text1_1_a.href=edit[0].link;
    p_img1.src=edit[0].img;
}
p_name[1].onclick=function(){
    p_name[ii].className="produce-name";
    ii=1;
    p_name[1].className="produce-name nav-choose";
    p_text1_1_h2.innerHTML=edit[1].title;
    p_text1_1_p.innerHTML=edit[1].content;
    p_text1_1_a.href=edit[1].link;
     p_img1.src=edit[1].img;
}
p_name[2].onclick=function(){
    p_name[ii].className="produce-name";
    ii=2;
    p_name[2].className="produce-name nav-choose";
    p_text1_1_h2.innerHTML=edit[2].title;
    p_text1_1_p.innerHTML=edit[2].content;
    p_text1_1_a.href=edit[2].link;
    p_img1.src=edit[2].img;
}
p_name[3].onclick=function(){
    p_name[ii].className="produce-name";
    ii=3;
    p_name[3].className="produce-name nav-choose";
    p_text1_1_h2.innerHTML=edit[3].title;
    p_text1_1_p.innerHTML=edit[3].content;
    p_text1_1_a.href=edit[3].link;
    p_img1.src=edit[3].img;
}
p_name[4].onclick=function(){
    p_name[ii].className="produce-name";
    ii=4;
    p_name[4].className="produce-name nav-choose";
    p_text1_1_h2.innerHTML=edit[4].title;
    p_text1_1_p.innerHTML=edit[4].content;
    p_text1_1_a.href=edit[4].link;
    p_img1.src=edit[4].img;
}

