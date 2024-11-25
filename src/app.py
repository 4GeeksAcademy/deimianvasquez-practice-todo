from flask import Flask, jsonify


playground = {
    "users":[
        {
            "id":1,
            "name": "deimian",
            "todos": [
                {
                    "label": "una tarea",
                    "is_done": False,
                    "id": 2
                }
            ]
        },
        {
            "id":2,
            "name": "Juana",
            "todos": [
                {
                    "label": "Otra tarea",
                    "is_done": False,
                    "id": 3
                }
            ]
        }
    ]
}


app = Flask(__name__)


@app.route("/todo/users")
def get_all_task():
    result=[]

    for user in playground["users"]:
        result.append({
            "id":user["id"],
            "name":user["name"],
        })

    return jsonify({
        "users":result
    }), 200


@app.route("/todo/users/<string:user_name>")
def get_one_user(user_name=None):
    user_name = user_name

    result = list(filter(lambda item: item["name"] == user_name, playground["users"]))

    
    return jsonify(result[0]), 200
 

 
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



#     const urlBase = "https://playground.4geeks.com/todo"





#     // necesito todas mis tareas, en caso de tener
#     const getAllTask = async () => {
#         try {
#             // fetching de datos
#             const responde = await fetch(`${urlBase}/users/deimian`)
#             const data = await responde.json()

#             if (responde.ok) {
#                 setTaskList(data.todos)
#             } else {
#                 createNewUser()
#             }


#         } catch (error) {
#             console.log(error)
#         }
#     }


#     // funcion que crea un usuario nuevo
#     const createNewUser = async () => {
#         try {
#             const response = await fetch(`${urlBase}/users/deimian`, {
#                 method: "POST"
#             })

#         } catch (error) {
#             console.log(error)
#         }
#     }


#     const addTask = async (event) => {
#         if (event.key == "Enter") {
#             try {
#                 const response = await fetch(`${urlBase}/todos/deimian`, {
#                     method: "POST",
#                     headers: {
#                         "Content-Type": "application/json"
#                     },
#                     body: JSON.stringify(task)
#                 })
#                 if (response.ok) {
#                     getAllTask()
#                     setTask(initialTask)
#                 }
#             } catch (error) {
#                 console.log(error)
#             }
#         }
#     }

#     const deleteTask = async (id) => {
#         try {
#             const responde = await fetch(`${urlBase}/todos/${id}`, {
#                 method: "DELETE"
#             })
#             if (responde.ok) {
#                 getAllTask()
#             }
#         } catch (error) {
#             console.log(error)
#         }
#     }

#     const editTask = async (item) => {
#         try {
#             const response = await fetch(`${urlBase}/todos/${item.id}`, {
#                 method: "PUT",
#                 headers: {
#                     "Content-Type": "application/json"
#                 },
#                 body: JSON.stringify({
#                     label: item.label,
#                     is_done: !item.is_done
#                 })
#             })
#             if (response.ok) {
#                 getAllTask()
#             }
#         } catch (error) {
#             console.log(error)
#         }
#     }
