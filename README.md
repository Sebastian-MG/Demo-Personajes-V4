# Demo-Personajes-v4

### Integrantes 
Juan Sebastian Mancera Gaitán 20171020047

 Luis Felipe Corredor 20171020056
 
 Pedro Enrique Barrera 20171020057
 


### Ejecucion y Librerias

 El ejecutable del juego es el archivo Launcher.py
 Juego realizado en Python 3 junto a las siguientes librerias:

copy => Prototype

pygame => ClasesJuego, Launcher, Game, Decorator, Composite, Pantalla

gc => Launcher, Game, Pantalla, StrategyJuego

os => Pantalla, Game

tkinter => Launcher

PIL => LAuncher

enum=> Tipos

functools => Launcher

math => Launcher

random => ClasesJuego, Launcher, Game, Decorator, Composite, Pantalla

Version 1:  Disponible aquí: https://github.com/Sebastian-MG/Demo-Personajes

Version 3:  Disponible aqui: https://github.com/Sebastian-MG/Demo-Personajes-v3


### Patrones De Diseño

##### Modulo Builder : 

Para la version 2 se amplio la clase Builder_Sprites para que construyera 4 objetos en diferentes direcciones, cada una agregada a un diccionario que era atributo propio privado de la clase Builder_Sprites, por su parte el modulo Builder_Sonidos no se expandió.
Entre la v2 y v3 el modulo solo fue modificado en un metodo en la clase Builder_Sprites.

Para version 4 se replanteo el llenado de los vectores en la clase Builder_Sprites dada la nueva funcionalidad planteada para esta version de ataque/defensa.

##### Modulo Abstract: (NO SE MODIFICO)

Se reemplaza el patrón abstract Factory que se habia planteado de forma diferente para la version 1, esta version 2 solo posee como dependencia el modulo Builder y su funcionamiento es realizar su contrucción a través de los Builders tomandolos como productos y almacenandolos en un directorio que es su atributo propio.

Para esta versión 2 la factoria no crea un personaje, solo crea las partes con las cuales el prototype realizara el armado de cada personaje.

Para Version 4, el codigo no tuvo que ser alterado aun con el replanteamiento del modulo builder.

#### Modulo ClasesJuego: 

Para versión 2 se replanteo el funcionamiento de las clases base haciendo que estas directamente fueran heredadas de la clase Sprite, se añadieron mas atributos para que la jugabilidad pudiera darse correspondiente a la extension de la clase Builder, en las 4 direcciones con velocidad en X,Y y métodos para que pudiera actualizarse en una pantalla que fuera otorgada.

Para version 3 se extendion la funcionalidad de las clases base de acuerdo a las nuevas funcionalidades del juego en esta version al igual que a los patrones implementados,concretamente a la clase Personaje se le añadieron atributos para los Decorados y para el Estado del personaje asi mismo se añadieron metodos para poder implementar estos patrones adecuadamente.

#### Modulo Prototype: (sin cambios)

Para version 2 se reestructuro el funcionamiento de la clase Prototype, ahora creandole dependencia a clasesJuego y siendo el encargado de fusionar lo traido a la clase Abstract y a la clase ClasesJuego creando un personaje totalmente jugable con los Sprite que traen las factorias de la clase Abstract.

Para version 3 se añadieron nuevos Prototipos debido a la extension realizada a la cantidad de personajes elegibles del juego.

Se crea un personaje prototipo,un arma prototipo y un escudo prototipo al acceder a las factorias y se inicializa un objeto estatico llamado ObjectFactory el cual provee los prototipos y realiza un método de fácil acceso para la creacion de los mismos.

#### Modulo Composite(Modulo de Prueba):  (sin cambios)

En este módulo se intentó recrear el concepto del patrón Composite graficando en pantalla un personaje que trae sus Builders directamente y los settea sin hacer uso de alguna Factoria o Prototype solo para comprobar el resultado de graficar en pantalla y sobreponer la sombra del porsonaje, el personaje y sus armas.

En version 3 se extendio la funcionalidad de este modulo basado en los nuevos patrones implementados como State Y Decorator para probar su graficacion de una manera segura sin necesidad de jugabilidad.

#### Modulo Decorator    (sin cambios)
En este módulo se crea de manera lógica el funcionamiento del patrón Decorator aunque durante la ejecución este no es utilizado.

En version 3 se simplifica la implementacion del patron al Decorator al crear un metodo de la clase Personaje que es padre de los Decoradores para poder ejecutar el patron de manera adecuada.

#### Modulo Flyweight (sin cambios)

Se crea una clase Peso_Ligero que diera facil acceso a los prototipos del módulo Prototype y que los posicionara en pantalla de una manera más dinámica y de fácil acceso al programador.

En version 3 se reemplaza la dependencia de la clase Prototype ahora añadida una depedencia a la clase añadida Cadena de Responsabilidad, asi el posicionamiento y devolucion de un tipo especifico de personaje se hizo mas dinamica.

#### Modulo Tipos  (NO SE MODIFICO)

En este módulo se crea una clase Enum la cual provee los tipos de personaje disponibles en el juego para que fuera facilmente extensible la cantidad de personajes que se pueden seleccionar.

#### Modulo Game 

Reemplaza al módulo DemoJuegos de la versión 1, ahora este  módulo no crea clases, solo posee el método main el cual ejecuta el juego a partir de un personaje seleccionable, se extendieron los procesos para crear una orda de personajes mas amplia con diferentes tipos de personajes y la jugabulidad se extendió en metodos para la capacidad que ahora provee los Builders referente a las 4 direcciones en las que se puede desplazar el personaje.

Se creo un método de ordenamiento en pantalla probado en el módulo Composite para que los personajes pudieran ser graficados en pantalla, de manera lógica en la cual los personajes  que estuviesen al fondo no se sobrepusieran sobre los personajes mas cercanos a la parte frontal.

Para v3 se extiendo lafuncionalidad de este Modulo para que la jugabilidad el State dentro del personaje jugable fuera alterado cada que se presionaba una tecla de direccion, ademas se añadio un decorador no visual al personaje que puede ser activado con la tecla P.

Para v4 se replantea la funcionalidad completa de este modulo, ahora su papel es ser "Facade" entre un objeto pantalla y un objeto Strategy.

#### Modulo Launcher (Sin cambios)

Este módulo trae todos los tipos disponibles en el Enum del modulo tipos y crea una matriz en pantalla para que el usuario pueda seleccionar el tipo de personaje con el cual quiere jugar, es decir settea la seleccion del usuario al Modulo Game para que el juego comience aplicando los principios Open-Close y Single Responsability.

#### Modulo State (Sin cambios)

Con este modulo se trato de dejar de sobrecargar de condicionales al personaje del modulo clases juegos creando un state para cada vez que el personaje cambia de direccion asi la graficacion del personaje no depende directamente sino del estado en el que se encuenta,ademas  intenta emular el funcionamiento del patron Observer al tener un personaje que sabe internamente cuando cambia sin necesidad de que el state tenga que hacer un condicional si se encuentra en la direccion.


#### Modulo Cadema de Responsabilidad   (sin cambios)

Se generaron objetos tipo cadena de responsabilidad que accedian a los prototipos de manera dinamica siendo  pasado el tipo de prototipo requerido en el primer eslabon de la cadena y este iba redirigiendo hasta hallar el tipo requerido y devolver este tipo a la clase que lo necesitara.


#### Modulo Strategy 

Para esta version 4 la jugabilidad no depende del modulo game sino de un patron Strategy aplicado en este modulo, en el cual se puede pasar de una estrategia de jugabilidad real a una de pausado.

#### Modulo Pantalla

Para version 4 se creo una clase pantalla que acumula los metodos y atributos que en versiones anteriores se ponian en el modulo Game, de esta manera se pueden crear nuevas pantallas durante  la ejecucion, lo cual sera util para aplicar en patron Memento version 5, lo cual flexibiliza la manera de utilizar el patron strategy incluido en esta version.

### Diagrama de Clases

![diag2](https://github.com/Sebastian-MG/Demo-Personajes-V4/blob/master/Class4.1.png)
