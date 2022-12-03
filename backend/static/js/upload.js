const image_drop_area = document.querySelector("#image_drop_area");
var uploaded_image = 'none';

image_drop_area.addEventListener('dragover', (event) => {
    event.stopPropagation();
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy';
});

image_drop_area.addEventListener('drop', (event) => {
    event.stopPropagation();
    event.preventDefault();
    const [file] = event.dataTransfer.files;
    check(file);
});

const add_box = (node, name) => {
    let el = document.createElement('div');
    let str = document.createElement('div');
    let x = document.createElement('div');

    el.setAttribute("id","file_name");
    str.setAttribute("id", "text");
    x.setAttribute("id","X");
    x.setAttribute("onclick",`reset()`);
    
    str.textContent = name;
    x.textContent = 'X';
    
    el.appendChild(str);
    el.appendChild(x);

    node.appendChild(el);
}

const remove_box = (node) => {
    let box = document.getElementById("file_name");
    node.removeChild(file_name);
}

const readImage = (file) => {
    const url = URL.createObjectURL(file);
    uploaded_image = url;
    document.querySelector("#image_drop_area").style.backgroundImage = `url(${uploaded_image})`;
    // const reader = new FileReader();
    // reader.addEventListener('load', (event) => {
    //     uploaded_image = event.target.result;
    //     document.querySelector("#image_drop_area").style.backgroundImage = `url(${uploaded_image})`;
    // });
    // reader.readAsDataURL(file);
};

const upload = ()=>{
    let button = document.getElementById('file-input');
    button.addEventListener("change",(event)=>{
        let [file] = event.currentTarget.files;
        if(file!==undefined)
            check(file);
    })
    button.click();
}

const check = (file)=>{
    if(file.type.includes('image')){
        let file_name = document.querySelector(".file_name");
        if(file_name.childElementCount !== 0)
            remove_box(file_name);
        add_box(file_name,file.name);
        readImage(file);
    }
    else
        alert("This is not image file!");
}

const reset = (node)=>{
    uploaded_image = 'none';
    document.querySelector("#image_drop_area").style.backgroundImage = uploaded_image;
    remove_box(document.querySelector(".file_name"));
}