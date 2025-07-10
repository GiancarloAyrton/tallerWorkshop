from behave import *
from todo_list import todo_manager

@given('el sistema tiene una lista de tareas vacía')
def step_impl(context):
    todo_manager.clear_tasks()

@when('agrego la tarea "{task}" con prioridad "{priority}"')
def step_impl(context, task, priority):
    todo_manager.add_task(task, priority)

@then('la lista debe mostrar "{task}" como {status}')
def step_impl(context, task, status):
    tasks = todo_manager.list_tasks()
    task_found = next((t for t in tasks if t["name"] == task), None)
    assert task_found, f"Tarea '{task}' no encontrada"
    if "pendiente" in status.lower():
        assert not task_found["completed"], f"La tarea está completada"
    else:
        assert task_found["completed"], f"La tarea está pendiente"

@given('existe la tarea "{task}" pendiente')
def step_impl(context, task):
    todo_manager.add_task(task)
    assert not todo_manager.list_tasks()[-1]["completed"]

@when('marco "{task}" como completada')
def step_impl(context, task):
    assert todo_manager.complete_task(task), f"No se pudo completar '{task}'"

@given('existen las siguientes tareas')
def step_impl(context):
    for row in context.table:
        todo_manager.add_task(row["Tarea"])
        if row.get("Estado", "").lower() == "completada":
            todo_manager.complete_task(row["Tarea"])

@when('listo todas las tareas')
def step_impl(context):
    context.task_list = todo_manager.list_tasks()

@then('veo {count:d} tareas en la lista')
def step_impl(context, count):
    assert len(context.task_list) == count, \
        f"Esperaba {count} tareas, hay {len(context.task_list)}"

@when('elimino la tarea "{task}"')
def step_impl(context, task):
    assert todo_manager.delete_task(task), f"No se pudo eliminar '{task}'"

@then('la tarea "{task}" no debe aparecer')
def step_impl(context, task):
    assert task not in [t["name"] for t in todo_manager.list_tasks()]

@given('existen {count:d} tareas en la lista')
def step_impl(context, count):
    for i in range(count):
        todo_manager.add_task(f"Tarea dummy {i+1}")
    assert len(todo_manager.list_tasks()) == count

@when('limpio toda la lista')
def step_impl(context):
    todo_manager.clear_tasks()

@then('la lista debe estar vacía')
def step_impl(context):
    assert len(todo_manager.list_tasks()) == 0

@when('filtro las tareas pendientes')
def step_impl(context):
    context.pending_tasks = todo_manager.get_pending_tasks()

@then('obtengo solo "{task}"')
def step_impl(context, task):
    assert len(context.pending_tasks) == 1, \
        f"Esperaba 1 tarea, obtuve {len(context.pending_tasks)}"
    assert context.pending_tasks[0]["name"] == task