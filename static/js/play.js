var player;

function onYouTubeIframeAPIReady() {
	//initVideoPlayer
	console.log("starting youtube stuff")
	getUrlFromQueue();
}

function getUrlFromQueue() {
	console.log("asking server for url...")
	$.get("/url", function(data) {
		console.log(data)
		if (data['url'] == '') {
			console.log("nope")
			setTimeout(getUrlFromQueue, 5000)
			// then ask again
		} else {
			// put url in player
		}
	});
}

$(document).ready(function() {

	

	// player = new YT.Player('video-placeholder', {
	    //     width: 600,
	    //     height: 400,
	    //     videoId: 'Xa0Q0J5tOP0',
	    //     playerVars: {
	    //         color: 'white',
	    //         playlist: 'taJ60kskkns,FG0fTKAqZ5g'
	    //     },
	    //     events: {
	    //         onReady: initialize
	    //     }
	    // });

});