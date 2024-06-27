var b = document.querySelector('#loginB');
var div_rgst = document.querySelector('.title-register');
var close2 = document.querySelector('#close2');
var bg2 = document.querySelector('.bg2');
var register = document.querySelector('.register');
// var username = document.querySelector('.username');
// var rusername = document.querySelector('.rusername');

b.onclick=function(){
    bg2.style.display = 'block';
    register.style.display='block';
}
close2.onclick=function(){
    bg2.style.display = 'none';
    register.style.display='none';
}

div_rgst.addEventListener('mousedown',function(e){
    var x = e.pageX-register.offsetLeft;
    var y = e.pageY-register.offsetTop;
function move(e){
    var newx=e.pageX-x;
    var newy=e.pageY-y;
register.style.left=newx+'px';
register.style.top=newy+'px';
}
document.addEventListener("mousemove",move)

document.addEventListener('mouseup',function(e){
    document.removeEventListener("mousemove",move);
})
})

