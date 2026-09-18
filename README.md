<p align="center">
  <img src="./logo.png" alt="meini-style" width="140" />
</p>
<p align="center">
  <strong align="center">Salidas "Ejecutivas" para ejecutivos.</strong>
</p>
<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/moimene/meini-style?style=flat" alt="License"></a>
</p>

<p align="center">
  <strong title="Español" aria-label="Español">🇪🇸</strong> ·
  <a href=".github/readme/README.en.md" title="English" aria-label="English">🇬🇧</a>
</p>

## Instalación

Copia y pega en el prompt de tu CLI:

```text
Install the meini-style skill/plugin from https://github.com/moimene/meini-style, refer to the repo's AGENTS.md for instructions.
```

O consulta las [instrucciones de instalación](INSTALL.md) por runtime (Claude Code, Codex, Gemini CLI, Cursor, OpenCode, Pi y otros).

## Qué hace

Una skill para tu asistente de IA que convierte cada respuesta en una pieza de trabajo financiero, de inversión o jurídico: conclusión primero con su condición, hechos separados de inferencias, citas con localización exacta, números que cuadran, supuestos declarados, plazos computados, texto listo para insertar y una frontera explícita entre lo verificado y lo pendiente.

Es un fork de [i-have-adhd](https://github.com/ayghri/i-have-adhd), que optimiza la salida para que se pueda actuar sobre ella. `meini-style` conserva ese esqueleto (acción primero, sin preámbulo ni cierres, persistencia durante la sesión) y añade lo que un profesional de estos ámbitos necesita para poder usar la respuesta sin retrabajo.

## Qué cambia

<table>
<tr>
<td width="50%">

## Antes

> Buena pregunta. La responsabilidad de los administradores por deudas sociales es un tema complejo que depende de varios factores. En general, cuando una sociedad incurre en causa de disolución y los administradores no convocan la junta en el plazo legal, pueden llegar a responder de ciertas deudas. Habría que analizar el caso concreto y la fecha de las deudas. Es importante tener en cuenta que esto no constituye asesoramiento jurídico y conviene consultar con un profesional. Espero que sea útil.

</td>

<td width="50%">

## Después

> **Sí, responde solidariamente**, siempre que la deuda sea posterior a la causa de disolución (art. 367 LSC). Si es anterior, no.
>
> - **Hecho:** la causa de disolución consta desde el cierre de 2024 (patrimonio neto inferior a la mitad del capital, art. 363.1.e) LSC). **Punto abierto:** fecha exacta de la deuda reclamada.
> - **Plazo para convocar junta:** dos meses desde que concurre la causa (art. 365.1 LSC).
> - **Verificado:** arts. 363, 365 y 367 del RDL 1/2010, texto vigente.
> - **No verificado:** fecha de devengo de la deuda; exige la factura o el contrato.

</td>
</tr>
</table>

## Las reglas

12 reglas. Texto completo en [SKILL.md](./skills/meini-style/SKILL.md).

1. Conclusión primero, con su condición.
2. Etiqueta hecho, inferencia, criterio y punto abierto.
3. Cita con localización exacta y solo lo verificado.
4. Números con unidad, moneda, fecha y base.
5. Supuestos en bloque; sensibiliza el que manda.
6. Fechas, plazos y vigencia computados.
7. Riesgo graduado con causa y consecuencia.
8. Terminología exacta; los términos de arte no se traducen.
9. Pieza lista para insertar.
10. Alternativas ordenadas, recomendación primero.
11. Frontera de verificación explícita.
12. Sin relleno, sin descargos genéricos, sin preámbulo ni cierre.

## Por qué es más competente que la especificación general

| Situación | Skill general de salida | meini-style |
| --- | --- | --- |
| Norma citada | "La ley prevé un plazo de un mes" | Artículo, apartado, norma completa, versión vigente; lo no contrastado se marca como pendiente |
| Cifra | "El margen mejora alrededor de un 2%" | Valor, unidad (% o p.b.), moneda, fecha de cierre, base y cálculo; los totales cuadran |
| Plazo | "Tienen un mes para recurrir" | Dies a quo, regla de cómputo, dies ad quem y norma que fija la regla |
| Riesgo | "Riesgo regulatorio a vigilar" | Causa, probabilidad razonada, impacto y mitigación |
| Redacción | Describe la cláusula | Entrega la cláusula, en el registro del documento, con marcadores [●] |
| Límite de la respuesta | Descargo genérico | Líneas "Verificado" y "No verificado" con el acceso que resolvería cada punto |

## Ajustarla

Haz un fork, edita `skills/meini-style/SKILL.md` y sustituye tu copia:

```bash
claude plugin uninstall meini-style            # primero retira la copia instalada:
claude plugin marketplace remove meini-style   # fork y original comparten nombre
claude plugin marketplace add <tu-usuario>/meini-style
claude plugin install meini-style@meini-style
```

Reinicia el asistente y vuelve a invocar `/meini-style`.

## Evaluación

Los casos de `evals/cases.jsonl` cubren consulta jurídica, análisis de inversión, cómputo de plazos, revisión contractual, redacción y límites de verificación. El procedimiento de ejecución, medición y puntuación ciega está en [evals/README.md](evals/README.md).

## Créditos

Fork de [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT), de Ayoub Ghriss. La infraestructura multi-runtime, los hooks always-on y el harness de evaluación proceden de ese proyecto. El conjunto de reglas se ha reescrito para trabajo financiero, de inversión y jurídico.

## Licencia

[MIT](LICENSE).
