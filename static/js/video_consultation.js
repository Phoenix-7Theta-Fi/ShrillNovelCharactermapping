// This file will contain the JavaScript code for handling the video consultation feature

let session;
let publisher;
let subscriber;

function initializeSession(apiKey, sessionId, token) {
    session = OT.initSession(apiKey, sessionId);

    session.on('streamCreated', function(event) {
        subscriber = session.subscribe(event.stream, 'remote-video', {
            insertMode: 'append',
            width: '100%',
            height: '100%'
        });
    });

    session.on('sessionDisconnected', function(event) {
        console.log('You were disconnected from the session.', event.reason);
    });

    // Initialize the publisher
    publisher = OT.initPublisher('local-video', {
        insertMode: 'append',
        width: '100%',
        height: '100%'
    });

    // Connect to the session
    session.connect(token, function(error) {
        if (error) {
            console.error('Error connecting to the session:', error.name, error.message);
        } else {
            session.publish(publisher);
        }
    });
}

// Add event listeners for the control buttons
document.getElementById('mute-audio').addEventListener('click', function() {
    publisher.publishAudio(!publisher.stream.hasAudio);
});

document.getElementById('mute-video').addEventListener('click', function() {
    publisher.publishVideo(!publisher.stream.hasVideo);
});

document.getElementById('end-call').addEventListener('click', function() {
    session.disconnect();
    window.location.href = '/doctor/appointments/';  // Redirect to appointments page
});

// You would call initializeSession with the appropriate credentials when the page loads
// For example:
// initializeSession('YOUR_API_KEY', 'YOUR_SESSION_ID', 'YOUR_TOKEN');