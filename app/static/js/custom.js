//selectors, methods, functions, and variables

jQuery(".sidebar").hover(function(){
		jQuery(this).css("background-color","#262626");
	}, function() {
		jQuery(this).css("background-color","");
	});
	
$("p").on("tap",function(){
		jQuery(this).css("background-color","#262626");
});