function submit(url){
    const height = parseInt(document.getElementById('height').value);
    const width = parseInt(document.getElementById('width').value);
    const password = document.getElementById('password').value;
    const username = String(Math.floor(Math.random() * Math.sqrt(height * width))).padStart(4,0);
    const index = upload_file.name.indexOf('.');
    const filename = upload_file.name.slice(0,index);
    if(height && width){
        const image = new FormData();
        image.append(`img`,upload_file)
        fetch(`${url}?username=${username}&password=${password}&opt_h=${height}&opt_w=${width}`,{
            method : "POST",
            body: image
        }).then(response=>{
            response.blob().then(f=>{
                console.log(f);
                download(f, filename);
            })
        })
    }
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