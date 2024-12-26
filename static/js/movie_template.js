

const buttonPlay = document.querySelector(".main__hero_template_content_button");
const videoShow = document.querySelector(".video");
const buttonClose = document.querySelector(".video_close");
const videoFrame = document.querySelector("iframe");
const fondoAnterior = document.querySelector(".main__hero_template_content")
const changeBG = document.querySelector("#url_bg").value;


function agregarIframe(source) {
    const iframe = document.createElement('iframe');    
    iframe.src = source;
    iframe.width = '560';
    iframe.height = '315';
    const contenedor = document.querySelector(".video-container");
    contenedor.appendChild(iframe);
  }

  function removerIframe() {
    const iframe = document.querySelector(".video-container").querySelector('iframe');
    iframe.remove();
  }


      buttonPlay.addEventListener("click",reproducir);
      buttonClose.addEventListener("click",cerrar);
      document.addEventListener("DOMContentLoaded",cambiar_fondo);


      function reproducir(e){
         videoShow.style.display ="block";
         source = document.getElementById("pelicula_video").value;         
         agregarIframe(source);
         cambiar_fondo();
      }

      function cerrar(event){
        videoShow.style.display ="none";
        removerIframe();
      }
      function cambiar_fondo(){        
        fondoAnterior.style.backgroundImage = 'url("'+changeBG+'")';
        
      }
      