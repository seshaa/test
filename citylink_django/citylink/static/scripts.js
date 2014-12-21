function statusBox(){
	jQuery('<div id="loading">Loading...</div>')
	.prependTo("#main")
	.ajaxStart(function(){jQuery(this).show();})
	.ajaxStop(function(){jQuery(this).hide();})
}

function prepareDocument(){
	//prepare the search box
	jQuery("form#search").submit(function(){
		text = jQuery("#id_q").val();
		if (text == "" || text == "Search"){
			alert("Enter a State.");
			return false;
		}
	});
	statusBox();
}

jQuery(document).ready(prepareDocument);
