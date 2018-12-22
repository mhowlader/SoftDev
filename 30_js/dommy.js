// team Whirlpool -- Mohtasim Howlader, Soojin Choi
// SoftDev pd7
// K30 -- sequential regression III: Season of the Witch
// 2018-12-21

var list = document.getElementById("thelist");


var changeHeading = function(e) {
    var h = document.getElementById("h")
    //console.log(ele);
    h.innerHTML = e;
};

var removeItem = function(e) {
    e.remove();
};

var lis = document.getElementsByTagName("li");


for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', function(){ changeHeading(this.innerHTML)} );
    lis[i].addEventListener('mouseout', function(){ changeHeading("Hello World!")});
    lis[i].addEventListener('click', function(){removeItem(this)});
};

var addItem = function(e) {
    var item = document.createElement("li");
    item.innerHTML= "WORD";
    list.appendChild(item);
    item.addEventListener('mouseover', function(){ changeHeading(this.innerHTML)} );
    item.addEventListener('mouseout', function(){ changeHeading("Hello World!")});
    item.addEventListener('click', function(){removeItem(this)});
 // ??? = "WORD";
 // ???
 // ...
 // ???
 // list.???( item );
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

//index of fibonacci
var indFib = 1;

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e){
    var item = document.createElement("li");
    item.innerHTML= fib(indFib);
    //console.log(fib(indFib));
    list.appendChild(item);
    indFib++;

    item.addEventListener('mouseover', function(){ changeHeading(this.innerHTML)} );
    item.addEventListener('mouseout', function(){ changeHeading("Hello World!")});
    item.addEventListener('click', function(){removeItem(this)});
};

// var fib2 = function(n) {
//     var window = [0, 1, 1];
//
//     if(n < 3){
//         return window[n];
//     }else{
//         var inc = 3;
//         while(inc <= n){
//             window[inc % 3] = window[(inc + 1) % 3] + window[(inc + 2) % 3];
//             inc++;
//         }
//         return window[(inc - 1) % 3];
//     }
//
// }
//
// var addFib2 = function(e){
//     var item = document.createElement("li");
//     item.innerHTML= fib2(indFib);
//     list.appendChild(item);
//     indFib++;
//
//     item.addEventListener('mouseover', function(){ changeHeading(this.innerHTML)} );
//     item.addEventListener('mouseout', function(){ changeHeading("Hello World!")});
//     item.addEventListener('click', function(){removeItem(this)});
// };

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
