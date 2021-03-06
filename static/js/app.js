//js files goes here

//print year 

var body = document.querySelector('body');
var header = document.querySelector('header');
var togmenu = document.querySelector('.togglemenu');
var tsearch = document.querySelector('.search-icon');
var dateHolder = document.querySelector('#year');
var year = new Date().getFullYear();
var gototop = document.querySelector('.gototop');
var gotobottom = document.querySelector('.gotobottom');



//print year in footer

yearonly = () => {
   dateHolder.innerHTML = year;
}
yearonly();

togmenu.onclick = () => {
	body.classList.toggle('togmenu')
}
tsearch.onclick = (a) => {
	body.classList.toggle('togsearch');
}

// sticky
window.onscroll = () => {
 var stickyheader = () => {
    var sticky = header.offsetTop;
	if(window.pageYOffset > sticky){
		header.classList.add('sticky');
        gototop.classList.add('show');
        gotobottom.classList.add('hide')
	}
    else if(window.pageYOffset >= 200){
    }
	else{
		header.classList.remove('sticky');
        gototop.classList.remove('show');
        gotobottom.classList.remove('hide')
	}
}
stickyheader()};
