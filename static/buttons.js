var currentPageName = window.location.pathname.replace(/\/$/, '').split('/').pop();
function previousButton(){
    var zadaca = currentPageName.length-1;
    var page = currentPageName[zadaca]-1;
    var prevpage = `${window.location.protocol}//${window.location.host}/zadaca` + page;
    if(page != '0')
        location.href = prevpage; 
}
function nextButton(){
    var zadaca = currentPageName.length-1;
    var page = parseInt(currentPageName[zadaca])+1;
    var nextpage = `${window.location.protocol}//${window.location.host}/zadaca` + page;
    if(page != '4')
        location.href = nextpage; 
}