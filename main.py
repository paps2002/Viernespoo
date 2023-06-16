from cosas import *

def main():
    per1 = Persona('Jose', 19)
    print(Persona)
    print(Persona.descripcion)

    print('herencia Alumno---------------')

    al1 = Alumno('Jose', 19, '318145839', 'ICO')
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = 'Juan'
    print(al2)
    al2.dormir()

    print('Herencia profesor----------')
    profe1 = Profesor('Jesus', 30+16, 318145839, 'Ingenieria de software')
    print(profe1)
    profe1.dormir()

    print('Herencia ayudante profesor--------------')
    ayudante = AyudanteProfesor('Adrian', 20, '318145839', 'ICO', 62111919, 'Ingenieria de software', 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = 'Abreham'
    ayudante.dar_clase("POO")



main()