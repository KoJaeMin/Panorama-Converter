async function submit(url){
    let height = Number(document.getElementById('height').value);
    let width = Number(document.getElementById('width').value);
    if(!Number.isInteger(height) || !Number.isInteger(width)){
        alert("Please enter integers!")
        return;
    }
    height = parseInt(height);
    width = parseInt(width);
    if(height < 0 || width < 0){
        alert("Please enter positive numbers!")
        return;
    }
    const password = document.getElementById('password').value;
    const username = String(Math.floor(Math.random() * Math.sqrt(height * width))).padStart(4,0);
    const index = upload_file.name.indexOf('.');
    const filename = upload_file.name.slice(0,index);

    const image = new FormData();
    image.append(`img`,upload_file)
    ///height : int , width : int, username : str, password : str
    const train_uri = `${url}?username=${username}&password=${password}&height=${height}&width=${width}`;
    const TrainResponse = await Training(train_uri,image);
    const TrainResponseJSON = await TrainResponse.json();
    
}

function download(image,name){
    const link = document.createElement('a');
    let encodedUri = window.URL.createObjectURL(image);
    link.style = 'display : none';
    link.href = encodedUri;
    link.download = `${name}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

const Training = async (uri, img)=> await fetch(uri,{method : 'POST',body : img})
function Checking(){}
function GetPanorama(){}