# Exemple de documentació del Procés de Recol·lecció de Dades per al Projecte de Curs dels Resultats d'una campanya telefònica per vendre un producte bancari

## 1. Fonts

**Identificació de Fonts:**
- Base de dades bank_dataset al GitHub de la ITACADEMY al directori projecteML (https://github.com/ITACADEMYprojectes/projecteML/blob/main/bank_dataset.CSV)

**Descripció de les Fonts:**
- Les dades bank dataset contenen característiques de l'individu i la variable target que identifica si el resultat de la campanya és o no és exitós. Són dades d'una campanya telefònica, amb trucades repetides a la mateixa persona, però no es pot identificar l’individu. Es recull el nombre de trucades total i la durada de la darrera trucada. Hi ha indicació dels temps des del contacte en una campanya anterior i del resultat de la campanya anterior.
  
## 2. Mètodes de recol·lecció de dades

**Procediments i Eines:**
- Dades en format CSV, emmagatzemada en el repositori de GitHub d'ITACADEMY. Aquesta tasca la fa el professor responsable del curs.

**Freqüència de Recol·lecció:**
- Totes les trucades de la campanya actual es comptabilitzen, als estudiants només ens arriba la versió final de les dades a analitzar amb la durada de la darrera trucada i el resultat en termes de contractació del dipòsit bancari a l'actual campanya. 
  
**Scripts de Descàrrega:**



```python
import pandas as pd

csv_url = "https://raw.githubusercontent.com/ITACADEMYprojectes/projecteML/main/bank_dataset.CSV"
df = pd.read_csv(csv_url)
print(df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 11162 entries, 0 to 11161
    Data columns (total 17 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   age        11152 non-null  float64
     1   job        11162 non-null  object 
     2   marital    11157 non-null  object 
     3   education  11155 non-null  object 
     4   default    11162 non-null  object 
     5   balance    11162 non-null  int64  
     6   housing    11162 non-null  object 
     7   loan       11162 non-null  object 
     8   contact    11162 non-null  object 
     9   day        11162 non-null  int64  
     10  month      11162 non-null  object 
     11  duration   11162 non-null  int64  
     12  campaign   11162 non-null  int64  
     13  pdays      11162 non-null  int64  
     14  previous   11162 non-null  int64  
     15  poutcome   11162 non-null  object 
     16  deposit    11162 non-null  object 
    dtypes: float64(1), int64(6), object(10)
    memory usage: 1.4+ MB
    None
    

## 3. Format i Estructura de les Dades

**Tipus de Dades:**
- Numèriques: `day`, `month`, `duration`, `campaign`, `pdays` i `previous`

- Categòriques: `job`, `marital`, `education`, `default`, `balance`, `housing`, `loan`, `contact`, `poutcome` i `deposit`

**Format d'Emmagatzematge:**

- Dades tabulars emmagatzemades en fitxer csv.

## 4. Limitacions de les dades

- Diferents Temps d'Actualització: El nombre de trucades telefòniques a un possible client representen un nombre diferencial segons si el client potencial està disponible o no. Hi ha dades d'una campanya actual i el temps des de la darrera trucada en una campanya anterior i si el resultat va ser exitós o no, aquestes darreres variables poden ser importants en el resultat de contractació del producte financer en una campanya posterior. No es disposa de les dades de durada de totes les trucades de la campanya actual, ni del moment del dia o dia de la setmana en que es van realitzar (seria útil per determinar la franja millor per fer la trucada), només de la darrera.
- El significat d'algunes característiques és desconegut i ni de lluny puc descobrir-lo sense emprar l'URL on trobar les metadades (https://archive.ics.uci.edu/dataset/222/bank+marketing).

## 5. Consideracions sobre Dades Sensibles

**Tipus de Dades Sensibles:**
- Informació Personal Identificable (PII): Cap
- Informació Financera Sensible: `housing`, `loan`
- Dades Comportamentals Sensibles:`contact`, `poutcome`, `pdays`, `previous`

**Mesures de Protecció:**
- **Anonimització i Pseudonimització:**
  - No cal aplicar cap hash per cap camp ni substitució per codis. Els autors han triat la supressió de les característiques d'identificació (telèfons, adreces, etc.)
- **Accés Restringit:**
  - Accés a dades sensibles no està restringit als estudiants del curs. Si fossin dades d'un projecte real, l'accés a dades sensibles seria restringit només a personal autoritzat amb necessitat de conèixer aquestes dades per a fins específics del projecte.
- **Compliment de Regulacions:**
  - Compliment amb la GDRP. L'organització bancària d'on provenen les dades és responsable del compliment de tots els principis de protecció de dades, així com de demostrar aquest compliment.


## 6. Enllaç al github

https://github.com/lidiamontero/Project-Machine-Learning/blob/main/Sprint4-T4-2.md
