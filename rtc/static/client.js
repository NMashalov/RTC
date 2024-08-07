var dataChannelLog = document.getElementById('data-channel'),
    iceConnectionLog = document.getElementById('ice-connection-state'),
    iceGatheringLog = document.getElementById('ice-gathering-state'),
    signalingLog = document.getElementById('signaling-state');


    pc = new RTCPeerConnection(config);

    // register some listeners to help debugging
    pc.addEventListener('icegatheringstatechange', () => {
        iceGatheringLog.textContent += ' -> ' + pc.iceGatheringState;
    }, false);
    iceGatheringLog.textContent = pc.iceGatheringState;


    dc = pc.createDataChannel('chat', parameters);
    dc.addEventListener('close', () => {
        clearInterval(dcInterval);
        dataChannelLog.textContent += '- close\n';
    });
    dc.addEventListener('open', () => {
        dataChannelLog.textContent += '- open\n';
        dcInterval = setInterval(() => {
            var message = 'ping ' + current_stamp();
            dataChannelLog.textContent += '> ' + message + '\n';
            dc.send(message);
        }, 1000);
    });
    dc.addEventListener('message', (evt) => {
        dataChannelLog.textContent += '< ' + evt.data + '\n';

        if (evt.data.substring(0, 4) === 'pong') {
            var elapsed_ms = current_stamp() - parseInt(evt.data.substring(5), 10);
            dataChannelLog.textContent += ' RTT ' + elapsed_ms + ' ms\n';
        }
    });

function createConnection(){
    pc = new RTCPeerConnection( {
        sdpSemantics: 'unified-plan'
    });
    return pc.createOffer().then((offer) => {
        return pc.setLocalDescription(offer);
    })
}