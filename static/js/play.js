var player;

function onYouTubeIframeAPIReady() {
	initVideoPlayer();
}

function getUrlFromQueue() {
	console.log("asking server for url...")
	$.get("/url", function(data) {
		console.log(data);
		if (data['videoId'] == '') {
			console.log("nope");
			setTimeout(getUrlFromQueue, 5000);
		} else {
			player.loadVideoById(data['videoId'])
		}
	});
}

function initVideoPlayer() {
	player = new YT.Player('video-placeholder', {
        width: 600,
        height: 400,
        videoId: '',
        events: {
        	'onReady' : getUrlFromQueue,
            'onStateChange' : onPlayerStateChange,
        }
    });
}

function playVideo() {
	player.playVideo();
}

function loadVideo(videoId) {
	player.loadVideoById(videoId);
}

function onPlayerStateChange(event) {        
    if(event.data === 0) {          
        getUrlFromQueue();
    }
}
// function initialize(){

//     // Update the controls on load
//     updateTimerDisplay();
//     updateProgressBar();

//     // Clear any old interval.
//     clearInterval(time_update_interval);

//     // Start interval to update elapsed time display and
//     // the elapsed part of the progress bar every second.
//     time_update_interval = setInterval(function () {
//         updateTimerDisplay();
//         updateProgressBar();
//     }, 1000)

// }

// // This function is called by initialize()
// function updateTimerDisplay(){
//     // Update current time text display.
//     $('#current-time').text(formatTime( player.getCurrentTime() ));
//     $('#duration').text(formatTime( player.getDuration() ));
// }

// function formatTime(time){
//     time = Math.round(time);

//     var minutes = Math.floor(time / 60),
//     seconds = time - minutes * 60;

//     seconds = seconds < 10 ? '0' + seconds : seconds;

//     return minutes + ":" + seconds;
// }

// // This function is called by initialize()
// function updateProgressBar(){
//     // Update the value of our progress bar accordingly.
//     $('#progress-bar').val((player.getCurrentTime() / player.getDuration()) * 100);
// }

// $(document).ready(function() {

// });