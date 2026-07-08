# Simulador de cajero automático
El sistema deberá simular operaciones básicas de un cajero automático. La solución podrá incluir validación de acceso mediante usuario y contraseña, consulta de saldo, extracción, depósitos y transferencias simples.
También podrá contemplarse control de saldo insuficiente, límites de extracción y registro básico de operaciones realizadas.

## Comisión K1.3 - Grupo C33 

## Integrantes: 
- Avalos, Lucas Alesandro.
- Jimenez, Agustina.
- Leguiza, Julia Estefania.
- Pabon, Ignacio.
- Roman, Lucas Agustin.

## Descripción general del sistema

El Simulador de Cajero Automático es una aplicación desarrollada en Python que se ejecuta por consola y simula las operaciones de una terminal bancaria interactiva. El sistema permite la autenticación de usuarios mediante credenciales, consulta de saldo, y la ejecución de transacciones básicas como extracciones de efectivo, depósitos y transferencias entre cuentas registradas. También, implementa la persistencia de datos a través de un archivo de texto local.
Durante el desarrollo se implementaron funciones, estructuras condicionales para la toma de decisiones financieras y estructuras repetitivas para los ciclos de validación de datos y la navegación de los menús de consola.

## FUNCIONALIDADES DEL SISTEMA
- Validación de acceso con usuario y contraseña.
- Inicialización automática del archivo de usuarios del sistema.
- Consulta de saldo actual disponible.
- Extracción de dinero con control de saldo insuficiente.
- Depósitos en cuenta.
- Transferencias entre usuarios.
- Menú interactivo con validación de opciones.

## INSTRUCCIONES DE EJECUCIÓN
1. Descargar o clonar este repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code o cualquier otro editor compatible con Python.
3. Abrir una terminal dentro de la carpeta del proyecto.
4. Ejecutar el archivo principal del sistema con el siguiente comando: python main.py (o python3 main.py en algunos sistemas operativos).
5. Una vez iniciado el programa, seguir las opciones del menú que se muestran en pantalla para utilizar el sistema.

## Utilización de inteligencia artificial
Durante el desarrollo del proyecto se utilizó Gemini como herramienta de apoyo para la creación del sistema. Fue utilizada para:
1. **Planificación estructural:** Definición de la estructura inicial del proyecto y su distribución en diferentes módulos funcionales.
2. **Consultas técnicas:** Resolución de dudas puntuales acerca del desarrollo de funciones específicas y el empleo de estructuras de control.
3. **Depuración de código:** Diagnóstico de fallos durante las pruebas, junto con alternativas para su resolución.
4. **Optimización general:** Sugerir mejoras en las validaciones, la modularización y la presentación del sistema.
 **Cabe destacar que cada una de las propuestas generadas por Gemini fueron analizadas, adaptadas e integradas por el grupo, asegurando la comprensión total de la lógica antes de su incorporación definitiva al repositorio.**
