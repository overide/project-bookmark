function mybookmarklet(){
	var jQuery_version = '3.1.1';
	var site_url = 'http://127.0.0.1:8000/'; //this is only for development environment!
	var static_url = site_url + 'static/';
	var min_width = 100;
	var min_height = 100;

	function bookmarklet(msg){
		//load css
		var $css = $("<link>");
		$css.attr({
			rel:'stylesheet',
			type:'text/css',
			href:static_url+'/css/bookmarklet.css?r='
			+Math.floor(Math.random()*999999999999999999999)
		});
		$('head').append($css);

		//load HTML
		var box_html = "<div id='bookmarklet'><a href='#' id='close'>&times;"+
		"</a><h1>Select an image to bookmark:</h1><div class='images'></div></div>";
		$('body').append(box_html);

		//close event
		$('#bookmarklet #close').click(function(){
			$('#bookmarklet').remove();
		});

		//find images as display
		$('img[src$="jpg"]').each(function(){
			if ($(this).height() >= min_height && $(this).width() >= min_width){
				var $image_url = $(this).attr('src');
				$('#bookmarklet .images').append("<a href='#'><img src='"+
					$image_url+"'/></a>");
			}
		});

		//when an image is selected open url with it
		$('#bookmarklet .images a').click(function(){
			var $selected_image = $(this).children('img').attr('src');
			//hide bookmarklet
			$('#bookmarklet').hide();
			//open new window to submit the image
			window.open(site_url+'images/create/?url='
				+encodeURIComponent($selected_image)
				+'&title='
				+encodeURIComponent($('title').text()),
				'_blank');
		});
	};

	//check if jQuery is loaded
	if (typeof window.jQuery != 'undefined'){
		bookmarklet();
	}else{
		//check for conflicts
		var conflict = typeof window.$ != 'undefined';

		//create a script to point to the google APIs
		var  jscript = document.createElement('script');
		jscript.setAttribute('src',
			'//ajax.googleapis.com/ajax/libs/jquery/'+
			jQuery_version+'/jquery.min.js');
		document.head.appendChild(jscript);

		//attempts to load jQuery script
		var attempts = 15;
		(function(){
			if(typeof window.jQuery == 'undefined'){
				if (--attempts > 0){
					//arguments.callee for anonymous function to call itself recursively.
					window.setTimeout(arguments.callee,1000); 
				}else{
					jscript.setAttribute('src',
						static_url+'js/jquery-3.1.1.min.js?r='
						+Math.floor(Math.random()*999999999999999999));
				}
			}else{
				bookmarklet();
			}
		})();
	}
}