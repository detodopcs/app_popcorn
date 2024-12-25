
document.addEventListener("DOMContentLoaded",()=>{
    email = document.querySelector("#email").value;
    contrasena = document.querySelector("#contrasena").value;
    comentarios = document.querySelector(".area_comments"); 
    comentarios.style.display = email ? "block":"none"; 
});