



const textarea = document.getElementById('comentario'); 
const boton_comentario = document.querySelector('.form_button'); 
let contador = document.querySelector(".contador");

textarea.addEventListener('input', () => {
    const cantidadCaracteres = textarea.value.length;
    console.log(cantidadCaracteres);
    contador.innerHTML = cantidadCaracteres;

    if(cantidadCaracteres <= 0){
        boton_comentario.disabled = true;
        boton_comentario.style.pointerEvents="auto";
        boton_comentario.style.cursor="not-allowed";
        boton_comentario.style.backgroundColor ="grey";

    }else if(cantidadCaracteres >= 15 && cantidadCaracteres <= 253){
        boton_comentario.disabled = false;
        boton_comentario.style.backgroundColor ="green";
        boton_comentario.style.cursor="pointer"; 

    }else{
        boton_comentario.disabled = true;
        boton_comentario.style.pointerEvents="auto";
        boton_comentario.style.cursor="not-allowed";
        boton_comentario.style.backgroundColor ="grey";
    }
    
});

//Funcion que se auto ejecuta al iniciar la pagina
document.addEventListener("DOMContentLoaded",()=>{
    boton_comentario.disabled = true;
    boton_comentario.style.pointerEvents="auto";
    boton_comentario.style.cursor="not-allowed";
    boton_comentario.style.backgroundColor ="grey";

});

