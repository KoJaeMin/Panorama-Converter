async function submit(url){
    let inputImageHeight = Number(document.getElementById('height').value);
    let inputImageWidth = Number(document.getElementById('width').value);
    if(!Number.isInteger(inputImageHeight) || !Number.isInteger(inputImageWidth)){
        alert("Please enter integers!")
        return;
    }
    inputImageHeight = parseInt(inputImageHeight);
    inputImageWidth = parseInt(inputImageWidth);
    if(inputImageHeight < 0 || inputImageWidth < 0){
        alert("Please enter positive numbers!")
        return;
    }
    const PASSWORD = document.getElementById('password').value;
    const USERID = String(Math.floor(Math.random() * Math.sqrt(inputImageHeight * inputImageWidth))).padStart(4,0);
    const FILEFULLNAME = upload_file.name;
    const INDEXofDOT = FILEFULLNAME.indexOf('.');
    const FILENAME = FILEFULLNAME.slice(0,INDEXofDOT);

    let inputImage = new FormData();
    inputImage.append(`img`,upload_file)
    ///height : int , width : int, username : str, password : str
    const URIforTRAIN = `${url}/training?username=${USERID}&password=${PASSWORD}&height=${inputImageHeight}&width=${inputImageWidth}`;
    const URIforCHECK = `${url}/check?username=${USERID}&password=${PASSWORD}`;
    const URIforDOWNLOAD = `${url}/download?filename=${FILEFULLNAME}&username=${USERID}&password=${PASSWORD}`;
    const RESPONSEofTRAIN = await requestForTrain(URIforTRAIN,inputImage);

    if(RESPONSEofTRAIN.status !== 201){
        const RESPONSEMESSAGE = await RESPONSEofTRAIN.json();
        alert(`${RESPONSEofTRAIN.status}\nMESSAGE : ${RESPONSEMESSAGE['message']}`);
        return;
    }
    const RESPONSEofCHECK = await requestForCheck(URIforCHECK);
    if(RESPONSEofCHECK !== 200){
        alert('Fail to make download');
        return;
    }
    await requestForGetPanorama(URIforDOWNLOAD,FILENAME);
}

async function downloadImage(image,name){
    const link = document.createElement('a');
    let encodedUri = window.URL.createObjectURL(image);
    link.style = 'display : none';
    link.href = encodedUri;
    link.download = `${name}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

const requestForTrain = async (uri, img) => await fetch(uri,{method : 'POST',body : img});

const requestForCheck = async (uri) => {
    let count = 0;
    let status = -1;
    const MAXIMUM_COUNT = 100;
    const DELAY_MILLISECOND = 60 * 1000;
    let CheckPolling = setInterval(async ()=>{
        const response = await fetch(uri,{method : 'GET'});
        status = response.status;
        if(status === 202){
            clearInterval(CheckPolling);
            return;
        }
        if(count===MAXIMUM_COUNT){
            clearInterval(CheckPolling);
            alert("TimeOut");
            return;
        }
        count++;
    },DELAY_MILLISECOND)
    return Promise.resolve(status);
};

const requestForGetPanorama = async (uri, filename) => {
    const HTTPRESPONSE = await fetch(uri);
    const ImageBlob = await HTTPRESPONSE.blob();
    await downloadImage(ImageBlob,filename);
};