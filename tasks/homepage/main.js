let addButton = document.getElementById('addToDo');
let todocontainer = document.getElementById('todocontainer');
let todoinput = document.getElementById('todoinput');

addButton.addEventListener('click',function(){
    var paragraph = document.createElement('p');
    paragraph.classList.add('paragraph-style');
    paragraph.innerText = todoinput.value;
    todocontainer.appendChild(paragraph);
    todoinput.value = "";
    paragraph.addEventListener('click',function(){
        paragraph.style.textDecoration = "line-through";
    })
    paragraph.addEventListener('dblclick', function(){
        todocontainer.removeChild(paragraph);
    })
})
