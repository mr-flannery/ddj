var player;

function onYouTubeIframeAPIReady() {
	console.log("yt api ready.");
	initVideoPlayer();
}

function getVideoIdFromQueue() {
	console.log("asking server for videoId...")
	$.get("/videoids", function(data) {
		console.log(data);
		if (data['videoId'] == '') {
			console.log("nope");
			setTimeout(getVideoIdFromQueue, 5000);
		} else {
			console.log("trying to load new video...");
			player.loadVideoById(data['videoId']);
		}
	});
}

function initVideoPlayer() {
	player = new YT.Player('player', {
        width: 600,
        height: 400,
        events: {
        	'onReady' : getVideoIdFromQueue,
            'onStateChange' : onPlayerStateChange,
            'onError' : onPlayerError,
        }
    });
}

function playVideo() {
	player.playVideo();
}

function onPlayerError(e) {
 console.log('An error occurred: ' + e.data);
}

function onPlayerStateChange(event) {
	console.log("player state change " + event.data);
    if(event.data === 0) {
    	console.log("video has ended");
        getVideoIdFromQueue();
    }
}