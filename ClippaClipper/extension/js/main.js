document
.getElementById("ping")
.addEventListener("click", async ()=>{

    try{

        const response=await fetch("http://127.0.0.1:5000/ping");

        const json=await response.json();

        document.getElementById("status").innerHTML=json.message;

    }

    catch(e){

        document.getElementById("status").innerHTML="Backend Offline";

    }

});