$(document).ready(function() {

	$('#submitRequest').click(function() {
		$.post("/", JSON.stringify({
			url: $("#requestUrl").val()
		}),
		function(response) {
			$('#response').text(response);
		});
	});

});

