function onDragStart(event) {
    event
      .dataTransfer
      .setData('text/plain', event.target.id);

    // cuando se empice a arrastrar el elemento
    // event
    // .currentTarget
    // .style
    // .backgroundColor = 'black';
  }

function onDragOver(event) {
    event.preventDefault();
}

function onDrop(event) {
    const id = event
      .dataTransfer
      .getData('text');
    
    const draggableElement = document.getElementById(id);
    const dropzone = event.target; // el evento se genera en el dropzone
    dropzone.appendChild(draggableElement); // agregarle el elemento que estamos arrastrando

    event  // borrar la transferencia
    .dataTransfer
    .clearData();
  }