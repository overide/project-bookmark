(function(){
	if (window.mybookmarklet !== undefined){
		mybookmarklet();
	}
	else{
		var script = document.createElement('script');
		script.setAttribute('src',
			'http://127.0.0.1:8000/static/js/bookmarklet.js?r='
			+Math.floor(Math.random()*999999999999999999));
		document.body.appendChild(script);
		window.setTimeout(arguments.callee,5000);
		mybookmarklet();
	}
})();