

document.addEventListener("DOMContentLoaded",()=>{
    email = document.querySelector("#email").value;
    contrasena = document.querySelector("#contrasena").value;

    iniciar_session = document.querySelector("#iniciar_session");
    cerrar_session = document.querySelector("#cerrar_session");
    registrarse = document.querySelector("#registrarse"); 
    menu_dashboard = document.querySelector("#menu_dashboard");

    if (email){
        iniciar_session.style.display="none";
        registrarse.style.display="none";

        menu_dashboard.style.display="block";
        cerrar_session.style.display="block";
    }else{
        iniciar_session.style.display="block";
        registrarse.style.display="block";

        menu_dashboard.style.display="none";
        cerrar_session.style.display="none";

    }   

});