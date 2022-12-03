function submit(){
    const height = document.getElementById('height').value;
    const width = document.getElementById('width').value;
    // const file = ;
    // const reader = new FileReader();
    // const fileObject = document.getElementById('file-input');
    console.log(uploaded_image);
    const image = new Image();
    if((height < 200 && width <200)){
        fetch('localhost:3000/img/img',{
            method : "POST",
            header : {}
        })
    }
}