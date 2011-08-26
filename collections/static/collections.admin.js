$(document).ready(function() {
	$("#collection_form").prepend("<div id='tabs'></div>");
	
	$("#tabs").append("<ul>" +
		"<li><a href='#tabs-1'>Content</a></li>" +
		"<li><a href='#tabs-2'>Metadata</a></li>" +
		"<li><a href='#tabs-3'>Schedule</a></li>" +
	"</ul>");
	var counter = 0;
	$("#collection_form fieldset").each(function(){
		counter++;
		$(this).attr("id", "tabs-" + counter)
	});
	$("#tabs").append($("#collection_form fieldset"));
	
	$("#tabs").tabs();
});
