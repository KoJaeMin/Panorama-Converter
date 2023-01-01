async function submit(url){
    const DELAY_MILLISECOND = 6000;

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
    const INDEXofDOT = upload_file.name.indexOf('.');
    const FILENAME = upload_file.name.slice(0,INDEXofDOT);

    let inputImage = new FormData();
    inputImage.append(`img`,upload_file)
    ///height : int , width : int, username : str, password : str
    const URIforTRAIN = `${url}?username=${USERID}&password=${PASSWORD}&height=${inputImageHeight}&width=${inputImageWidth}`;
    const RESPONSEofTRAIN = await requestForTrain(URIforTRAIN,inputImage);
    const TrainResponseJSON = await RESPONSEofTRAIN.json();
    
}

function downloadImage(image,name){
    const link = document.createElement('a');
    let encodedUri = window.URL.createObjectURL(image);
    link.style = 'display : none';
    link.href = encodedUri;
    link.download = `${name}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

const requestForTrain = async (uri, img) => {await fetch(uri,{method : 'POST',body : img})};
const requestForCheck = async () => {};
const requestForGetPanorama = async () => {};