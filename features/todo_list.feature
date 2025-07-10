Feature: Gestor de Lista de Tareas
  Como usuario
  Quiero gestionar mis tareas
  Para organizar mi trabajo diario

  Background:
    Given el sistema tiene una lista de tareas vacía

  Scenario: Añadir una nueva tarea
    When agrego la tarea "Comprar leche" con prioridad "alta"
    Then la lista debe mostrar "Comprar leche" como pendiente

  Scenario: Marcar tarea como completada
    Given existe la tarea "Hacer ejercicio" pendiente
    When marco "Hacer ejercicio" como completada
    Then la tarea "Hacer ejercicio" debe aparecer como completada

  Scenario: Listar todas las tareas
    Given existen las siguientes tareas:
      | Tarea           | Estado     |
      | Revisar email   | Pendiente  |
      | Preparar informe | Completada |
    When listo todas las tareas
    Then veo 2 tareas en la lista

  Scenario: Eliminar una tarea
    Given existe la tarea "Llamar a Juan" pendiente
    When elimino la tarea "Llamar a Juan"
    Then la tarea "Llamar a Juan" no debe aparecer

  Scenario: Limpiar toda la lista
    Given existen 3 tareas en la lista
    When limpio toda la lista
    Then la lista debe estar vacía

  Scenario: Filtrar tareas pendientes
    Given existen las siguientes tareas:
      | Tarea          | Estado     |
      | Leer libro     | Pendiente  |
      | Ir al gimnasio | Completada |
    When filtro las tareas pendientes
    Then obtengo solo "Leer libro"