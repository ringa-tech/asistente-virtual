let blobs = [];
let stream;
let rec;
let recordUrl;
let audioResponseHandler;

//Solo grabo el URL a llamar (e.g. /audio) y el 'handler'
//o 'callback' a llamar cuando termine la grabacion
function recorder(url, handler) {
    recordUrl = url;
    if (typeof handler !== "undefined") {
        audioResponseHandler = handler;
    }
}

/**
 * Al ser un proyecto pequeño uso doc.getById como maniaco
 * Si no te gusta, puedes cambiarlo ;)
 */
async function record() {
    try {
        document.getElementById("text").innerHTML = "<i>Grabando...</i>";
        document.getElementById("record").style.display="none";
        document.getElementById("stop").style.display="";
        document.getElementById("record-stop-label").style.display="block"
        document.getElementById("record-stop-loading").style.display="none"
        document.getElementById("stop").disabled=false

        blobs = [];

        //Grabar audio, blabla
        stream = await navigator.mediaDevices.getUserMedia({audio:true, video:false})
        rec = new MediaRecorder(stream);
        rec.ondataavailable = e => {
            if (e.data) {
                blobs.push(e.data);
            }
        }
        
        rec.onstop = doPreview;
        
        rec.start();
    } catch (e) {
        alert("No fue posible iniciar el grabador de audio! Favor de verificar que se tenga el permiso adecuado, estar en HTTPS, etc...");
    }
}

function doPreview() {
    if (!blobs.length) {
        console.log("No hay blobios!");
    } else {
        console.log("Tenemos blobios!");
        const blob = new Blob(blobs);

        //Usar fetch para enviar el audio grabado a Pythonio
        var fd = new FormData();
        fd.append("audio", blob, "audio");

        fetch(recordUrl, {
            method: "POST",
            body: fd,
        })
        .then((response) => response.json())
        .then(audioResponseHandler)
        .catch(err => {
            //Puedes hacer algo más inteligente aquí
            console.log("Oops: Ocurrió un error", err);
        });
    }
}

function stop() {
    document.getElementById("record-stop-label").style.display="none";
    document.getElementById("record-stop-loading").style.display="block";
    document.getElementById("stop").disabled=true;
    
    rec.stop();
}

//Llamar al handler en caso que exista
function handleAudioResponse(response){
    if (!response || response == null) {
        //TODO subscribe you thief
        console.log("No response");
        return;
    }

    document.getElementById("record").style.display="";
    document.getElementById("stop").style.display="none";
    
    if (audioResponseHandler != null) {
        audioResponseHandler(response);
    }
}