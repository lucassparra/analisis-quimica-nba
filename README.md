# 🏀 NBA Alchemy: Optimizando la Química de Equipo con Machine Learning

> **Estado:** 🚧 En Desarrollo (Work in Progress)

## 📖 Sobre el Proyecto

El baloncesto moderno ha dejado atrás las 5 posiciones tradicionales (Base, Escolta, Alero, Ala-Pívot, Pívot). Hoy en día, un jugador de 2.10m puede ser el principal creador de juego y un base puede ser un especialista defensivo en el poste.

Este proyecto utiliza **Ciencia de Datos y Aprendizaje No Supervisado (Clustering)** para:
1.  **Redefinir los roles** de los jugadores basándose en su comportamiento estadístico real y no en su etiqueta de posición.
2.  Analizar la **química de alineaciones** para descubrir qué combinaciones de estos nuevos arquetipos maximizan el *Net Rating*.

El objetivo final es responder matemáticamente: *¿Qué mezcla de estilos crea el equipo más eficiente?*

## 🛠️ Tecnologías

* **Python**
* **Data Collection:** `nba_api`
* **Data Manipulation:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (K-Means Clustering)
* **Visualización:** `matplotlib`, `seaborn`

---

## 📊 Diccionario de Datos


Los datos utilizados en este análisis provienen del repositorio público:
> **NBA Stats (1947-present)** por *sumitrodatta*.  
> Disponible en: https://www.kaggle.com/sumitrodatta  
> Último acceso: Enero 2026.

### 🆔 Información General
| Atributo | Significado | Descripción |
| :--- | :--- | :--- |
| **season** | Temporada | Año de la temporada  |
| **lg** | Liga | Liga de origen (NBA, G-League, etc.). |
| **player** | Nombre | Nombre completo del jugador. |
| **player_id** | ID Único | Identificador numérico único del jugador en la base de datos oficial. |
| **age** | Edad | Edad del jugador al 1 de febrero de esa temporada. |
| **team** | Equipo | Abreviatura del equipo (ej: LAL, BOS). |
| **pos** | Posición | Posición nominal (PG, SG, SF, PF, C). *Nota: Esta es la etiqueta que intentamos mejorar con el modelo.* |

### ⏱️ Tiempo de Juego
| Atributo | Significado | Descripción |
| :--- | :--- | :--- |
| **g** | Partidos Jugados | Cantidad total de partidos en los que pisó la cancha. |
| **gs** | Partidos como Titular | Cantidad de partidos en los que inició en el quinteto titular (*Games Started*). |
| **mp** | Minutos Jugados | Total de minutos disputados en la temporada. |

### 🎯 Eficiencia y Estilo de Tiro
| Atributo | Significado | Descripción |
| :--- | :--- | :--- |
| **per** | Player Efficiency Rating | Métrica global que intenta resumir todo el aporte de un jugador en un solo número (ajustado por ritmo). La media de la liga es 15.00. |
| **ts_percent** | True Shooting % | Porcentaje de Tiro Verdadero. Mide la eficiencia de tiro combinando tiros de 2, triples y tiros libres. |
| **x3p_ar** | 3-Point Attempt Rate | Qué porcentaje de los tiros de campo del jugador son triples. Define si es un tirador exterior o interior. |
| **f_tr** | Free Throw Rate | Número de tiros libres intentados por cada tiro de campo intentado. Indica agresividad atacando el aro. |

### 🔄 Posesión, Rebote y Creación (Métricas de Estilo)
Estas variables son críticas para el algoritmo de Clustering.

| Atributo | Significado | Descripción |
| :--- | :--- | :--- |
| **usg_percent** | Usage Percentage | **% de Uso.** Estima el porcentaje de jugadas de equipo usadas por el jugador mientras está en pista (tiros, pérdidas o tiros libres). Define "quién manda". |
| **ast_percent** | Assist Percentage | Porcentaje de canastas de compañeros que fueron asistidas por el jugador mientras estaba en pista. |
| **tov_percent** | Turnover Percentage | Porcentaje de posesiones del propio jugador que terminan en pérdida de balón. |
| **orb_percent** | Offensive Rebound % | Porcentaje de rebotes ofensivos disponibles que captura el jugador. |
| **drb_percent** | Defensive Rebound % | Porcentaje de rebotes defensivos disponibles que captura el jugador. |
| **trb_percent** | Total Rebound % | Porcentaje total de rebotes disponibles capturados. |
| **stl_percent** | Steal Percentage | Estimación del porcentaje de posesiones rivales que terminan con un robo de este jugador. |
| **blk_percent** | Block Percentage | Estimación del porcentaje de tiros de 2 puntos del rival que son taponados por este jugador. |

### 🏆 Win Shares (Contribución a la Victoria)
Estimaciones de cuántas victorias aporta un jugador a su equipo.

| Atributo | Significado | Descripción |
| :--- | :--- | :--- |
| **ows** | Offensive Win Shares | Victorias contribuidas debido a su ofensiva. |
| **dws** | Defensive Win Shares | Victorias contribuidas debido a su defensa. |
| **ws** | Win Shares | Suma total de OWS + DWS. |
| **ws_48** | WS per 48 Min | Win Shares normalizadas por 48 minutos (un partido completo). Ideal para comparar jugadores con diferentes minutos. |

### ⚡ Box Plus/Minus (Impacto en Cancha)
Estima el rendimiento del jugador por cada 100 posesiones en comparación con un jugador promedio de la liga.

| Atributo | Significado | Descripción |
| :--- | :--- | :--- |
| **obpm** | Offensive Box Plus/Minus | Puntos ofensivos por encima/debajo del promedio por 100 posesiones. |
| **dbpm** | Defensive Box Plus/Minus | Puntos defensivos salvados por encima/debajo del promedio por 100 posesiones. |
| **bpm** | Box Plus/Minus | Suma de OBPM y DBPM. (0.0 es el promedio de la liga, +5.0 es nivel All-NBA). |
| **vorp** | V.O.R.P. | *Value Over Replacement Player*. Convierte el BPM en una estimación de contribución total, comparando al jugador con un "jugador de reemplazo" teórico (nivel bajo de banquillo). |

---

