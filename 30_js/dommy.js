// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!

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
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML= "WORD";
    list.appendChild(item);
 // ??? = "WORD";
 // ???
 // ...
 // ???
 // list.???( item );
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e){
    console.log(e);
 ???
 ...
 ???
};

// var addFib2 = function(e){
//     console.log(e);
//  ???
//  ...see QAF re: DYNAMIC PROGRAMMING...
//  ???
// };

// var fb = document.getElementById("fb");
// fb.addEventListener("click", addFib);
