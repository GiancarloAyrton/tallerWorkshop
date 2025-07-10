from todo_list import TodoList

def main():
    manager = TodoList()
    while True:
        print("\n1. Añadir tarea\n2. Listar tareas\n3. Completar tarea\n4. Salir")
        choice = input("Selecciona una opción: ")
        if choice == "1":
            task = input("Nombre de la tarea: ")
            manager.add_task(task)
        elif choice == "2":
            for task in manager.list_tasks():
                print(f"- {task['name']} ({'Completada' if task['completed'] else 'Pendiente'})")
        elif choice == "3":
            task = input("Tarea a completar: ")
            if manager.complete_task(task):
                print("✓ Tarea completada")
            else:
                print("✗ Tarea no encontrada")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()