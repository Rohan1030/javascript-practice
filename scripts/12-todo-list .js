const todoList = [{
      name:'make dinner',
      dueDate:'2022-12-22'
},
{
      name: 'wash dishes',
      dueDate:'2022-12-22'
}          
];

renderTodolist();

function renderTodolist()
{

let todoListHTML = '';

      todoList.forEach(function(todoObject,index)
{
      const {name,dueDate} = todoObject;
      

      const html = 
      `
      <div> ${name} </div>
      <div>${dueDate} </div>
            <button onclick = "

            todoList.splice(${index},1);
            renderTodolist();
            
            " class = "delete-todo-button">Delete</button>`;
      todoListHTML += html;
});


console.log(todoListHTML);

document.querySelector('.js-todo-list').innerHTML = todoListHTML;


}

function addtodo()
{
      const inputElement = document.querySelector('.js-name-input');
      const name = inputElement.value;

      const dateInputElement = document.querySelector('.js-due-date-input'); 

      const dueDate = dateInputElement.value;
       todoList.push({
            //name: name,
            //dueDate:dueDate
            name,
            dueDate
});
       console.log (todoList);


       inputElement.value = '';

       renderTodolist();
}