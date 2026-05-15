# DSA_Final_Proyect---Linked_Pendulums

El proyecto trata acerca de círculos que actúan como péndulos cuando son el último círculo de una cadena de péndulos estáticos, pero cuando se añade un nuevo círculo, se guarda el último estado del círculo y se queda estático, haciendo que el siguiente actúe como péndulo. Cuando se elimina un círculo, el anterior actúa de nuevo como péndulo y continúa oscilando de un lado a otro en su último estado. Cuando el último péndulo se conecta al primer círculo, automáticamente todos quedan estáticos, haciendo que ya no se pueda ni insertar ni eliminar un nuevo círculo.

La estructura de datos que se implementó fue la Circular Doubly Linked List, cuyos atributos son head, tail, current_node, circulified y trasversed, mientras que sus métodos son los siguientes:

| Método | Complejidad |
| --- | --- |
| insert(data) | O(1) |
| delete() | 0(1) |
| circulify() | 0(1) |
| traverse() | 0(n) |
| move_next() | 0(1) |
| move_prev() | 0(1) |

Como se puede observar, casi todos los métodos son constantes. Esto se debe a que se añadió una pequeña optimización no vista en clase, que consiste de un puntero "tail" que apunta siempre al último elemento de una LL, lo que permite que se pueda insertar, eliminar o convertir en una lista circular sin necesidad de recorrer toda la lista. Cabe aclarar que los métodos insert(data) y delete() siempre afectan al último nodo de una lista ya que así lo amerita el proyecto. Se añadieron métodos que yo mismo inventé llamados circulify(), move_next() y move_prev(). Circulify() convierte a la lista en circular, move_next() y move_prev() como sugieren sus nombres permite movernos entre nodos siempre y cuando la lista sea circular y haya sido recorrida. Estos últimos dos métodos tienen una particularidad, y es que aunque casi siempre tienen una complejidad constante, la primera vez que se usa una de estas dos tiene una complejidad lineal ya que llama a la función traverse().

Aparte de estos métodos, también se usaron algoritmos de renderizado que valen la pena analizar:

| Método | Complejidad |
| --- | --- |
| generateCircle(segments) | O(n) |
| generateButton() | 0(1) |
| generateLine() | 0(1) |

Por último, para clonar el repositorio solo hay que ejecutar el comando git clone con la SSH key, y para ejecutar el programa solo se ejecuta el archivo main.py. Para usarlo, hay que tener en cuenta lo siguiente: el botón azul lo que hace es insertar péndulos, el botón cian elimina el último péndulo y el botón verde convierte la lista en circular, tirando hacia dos botones que se usan solo para moverse entre los nodos.