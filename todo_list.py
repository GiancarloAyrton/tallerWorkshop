class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="medium", due_date=None):
        self.tasks.append({
            "name": name,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        })
        return True

    def list_tasks(self):
        return self.tasks.copy()

    def complete_task(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                return True
        return False

    def clear_tasks(self):
        self.tasks.clear()
        return True

    def delete_task(self, task_name):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["name"] != task_name]
        return len(self.tasks) < initial_count

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["completed"]]

# Instancia global para testing
todo_manager = TodoList()