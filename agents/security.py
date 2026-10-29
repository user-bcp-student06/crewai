"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'security'
LABEL = 'Revisor de seguridad'
SPEC_FILE = 'security_report.md'
EXTRACT_CODE = False

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='Revisor de seguridad', 
                goal=(
                    "Revisar autenticación, autorización y acceso a recursos de otra persona, validación "
                    "de entradas, inyección, secretos y exposición de datos sensibles en el código entregado, "
                    "y entregar security_report.md con hallazgos, correcciones y comprobaciones."
                ),
                backstory=(
                    "Eres un revisor de seguridad que escribe en español. Solo afirmas lo que se observa en el "
                    "código entregado. Separas riesgos detectados, correcciones propuestas y verificaciones "
                    "realmente ejecutadas. No ejecutas herramientas: no tienes evidencia de ejecución salvo la "
                    "que aparezca en el código."
                ),
                llm=llm,
                verbose=True, 
                allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=(
                    "Revisa el siguiente código del proyecto:\n\n{codigo}\n\n"
                    "Revisa autenticación, autorización y acceso a recursos de otra persona. "
                    "Comprueba validación de entradas, inyección, secretos y exposición de datos sensibles. "
                    "Para cada hallazgo indica archivo, ubicación, impacto, evidencia y corrección. "
                    "Propón una comprobación reproducible de cada corrección. "
                    "Distingue riesgos detectados, correcciones propuestas y verificaciones realmente ejecutadas; "
                    "en este flujo, las verificaciones ejecutadas son ninguna salvo que se indique lo contrario. "
                    "Entrega security_report.md con hallazgos, correcciones y comprobaciones."
                ),
                expected_output=(
                    "Contenido completo de security_report.md en Markdown con las secciones: "
                    "Resumen, Hallazgos, Correcciones propuestas, Comprobaciones reproducibles y Verificaciones ejecutadas. "
                    "Cada hallazgo incluye archivo, ubicación, impacto, evidencia y corrección."
                ), agent=agent)
