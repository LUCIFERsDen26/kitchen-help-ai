

const fileName = document.querySelector(".file-name");
const customBtn = document.querySelector("#custom-btn");
const cancelBtn = document.querySelector("#cancel-btn i");

const imgform=document.querySelector("#foodimgform");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;


function showloader(){
    document.getElementById("loading").style.display = "block";
    document.getElementById("info").style.display = "none";
}
function hideloader(){
    document.getElementById("loading").style.display = "none !important";
    document.getElementById("info").style.display = "block";
}


window.onload = function() {
    console.log("loaded");
    document.getElementById("custom-btn").addEventListener("click", function() {
        // Trigger file input click        
        document.getElementById("default-btn").click();
        console.log("clicked");
        
    });
}

function defaultBtnActive(input) {
    var file = input.files[0];
    if (file) {
        showloader();
        var reader = new FileReader();
        reader.onload = function() {
            var result = reader.result;
            var img = document.getElementById("foodimage");
            img.src = result;
            console.log(result);

            // Show loading and submit form
            document.querySelector(".content .text").textContent = "File loaded!";
            
            // document.getElementById("loading").style.display = "block";
            document.getElementById("foodimgform").submit();
        };

        reader.readAsDataURL(file);
    }

    if (input.value) {
        var fileName = document.querySelector(".file-name");
        fileName.textContent = input.value.split("\\").pop();  // Show file name
    }
}




function select(filename){
    const img = document.querySelector("#foodimage");
    const wrapper = document.querySelector(".wrapper");

    img.src = "/static/images/"+filename

    wrapper.classList.add("active");
    showloader();
    ctx = document.getElementById("close").click()
  
}
    
