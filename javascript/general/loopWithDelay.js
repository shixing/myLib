var stop = true;
var stop = false;
var finished = true;


function get_cids()
{
    ass = document.getElementsByTagName("a");
    cids = [];
    for (var i = 0; i< ass.length; i+=1)
    {
	h = ass[i].href;
	if (h.startsWith("https://www.capitaliq.com/CIQDotNet/company.aspx?companyId=")){
	    cid = h.substring(59,h.length);
	    cids.push(cid);
	}
    }
    return cids;
}



function openw(k,m,p){
    timeout = 200;
    setTimeout(function (){
	window.open(m[k]);
	//console.log(m[k]);
	k = k + 1;
	if (k<m.length){
	    openw(k,m,p);
	}
	else
	{
	    //alert("finished!");
	    //download_page(p+1);
	    finished = true;
	}
    },timeout);
}

function download_all(p){
    cids = get_cids();
    urls = [];
    for (var i = 0;i<cids.length;i+=1){
	url = "https://www.capitaliq.com/CIQDotNet/Company/BoardMembers.aspx?CompanyId="+cids[i];
	urls.push(url);
    }
    var k = 0;
    setTimeout(openw(k,urls,p),1000);
}

function download_page(i){
	if (stop){
	    console.log("stopped!");
	    stop = false;
	} else {
	    __doPostBack('_gridView$_gridView','Page$'+i);
	    nto = 10000;
	    setTimeout(function(){
		var tid = setInterval(function(){
		    a = document.getElementById("ctl14");
		    if (a.style["display"] == "none"){
			console.log("loading page "+i+" finished!");
			clearInterval(tid);
			download_all(i);
		    }
		},500);
	    },nto);
	}
    
}

function download_page2(i){
    interval = 1000;
    var looper = setInterval(function(){
	if (stop){
	    console.log("stopped!");
	    stop = false;
	    clearInterval(looper);
	}
	if (finished){
	    finished = false;
	    __doPostBack('_gridView$_gridView','Page$'+i);
	    nto = 10000;
	    setTimeout(function(){
		var tid = setInterval(function(){
		    a = document.getElementById("ctl14");
		    if (a.style["display"] == "none"){
			console.log("loading page "+i+" finished!");
			clearInterval(tid);
			download_all(i);
			i+=1;
		    }
		},500);
	    },nto);
	}

    },interval);
}
