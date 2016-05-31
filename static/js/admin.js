var websocket;
var paused;

function openWS() {
	websocket = new WebSocket("ws://localhost:8088/adminwebsocket");
	websocket.onopen = function(e) {
		console.log("opened");
	}
	websocket.onmessage = function(e) {
		console.log("message");
	};
	websocket.onclose = function(e) {
	  console.log(e);
	};
}

$(document).ready( function() {
    openWS();

    $('#skipButton').click( function() {
        websocket.send("skip");
    });

	$('#pauseButton').click( function() {
        if (paused) {
			websocket.send("unpause");
			paused = !paused;
			$('#pauseButton').html("pause");
		} else {
			websocket.send("pause");
			paused = !paused;
			$('#pauseButton').html("unpause");
		}
    });
});
