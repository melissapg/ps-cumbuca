<center>

# Soluções em ANSI-SQL

</center>

As soluções descritas aqui foram criadas como auxílio de raciocínio para as perguntas levantadas.

1. [Questão](#1-questão)
2. [Questão](#2-questão)
3. [Questão](#3-questão)
4. [Questão](#4-questão)

<br>

## 1. Questão
#### Porcentagem dos voos que atrasam mais de 5 min. por mês e companhia aérea. Qual foi o pior mês para <i>Delta Air Lines Inc.</i>?
```sql
WITH t AS (
SELECT
      flights.month,
	  airlines.name,
	  (SUM(CASE 
	        WHEN flights.total_delay > 5
		    THEN 1
		    ELSE 0
	  	END) * 100) / COUNT(flights.flight) AS "percentage_delays"
FROM
	  flights
LEFT JOIN
	  airlines ON airlines.carrier = flights.carrier
GROUP BY
	  flights.month, 
	  airlines.name
ORDER BY 
	  airlines.month
)

SELECT
	  month,
	  max(percentage_delays)
FROM
	  t
WHERE
	  airlines.name = 'Delta Air Lines Inc.'
```

<br>

## 2. Questão
#### Quantidade de aviões distintos e voos realizados por fabricante. Qual fabricante possui menos voos?
```sql
SELECT
		planes.manufacturer,
		COUNT(DISTINCT planes.tailnum) AS "planes",
		COUNT(flights.flight) AS "flights"
FROM
		flights
LEFT JOIN
		planes ON planes.tailnum = flights.tailnum 
GROUP BY
		planes.manufacturer
HAVING
		MIN(COUNT(flights.flight))
```

<br>

## 3. Questão
#### Empresa que mais realizou voos com aviões da <i>Airbus</i>.
```sql
SELECT
		airlines.name,
		COUNT(flights.flight) AS "flights"
FROM
		flights
LEFT JOIN
		airlines ON airlines.carrier = flights.carrier
LEFT JOIN
		planes ON plane.tailnum = flights.tailnum
WHERE
		planes.manufacturer = 'AIRBUS'
GROUP BY
		airlines.name
HAVING
		MAX(COUNT(flights.flight))
```

<br>

## 4. Questão
#### Quantidade de voos que os aeroportos receberam entre 18h00 e 22h00 no dia 03-Março.
```sql
SELECT
		airports.name,
		COUNT(flights.flight) as "flights"
FROM
		flights
LEFT JOIN
		airports ON airports.faa = flights.dest
WHERE
		flights.month = 3
   AND
		flights.day = 3
   AND
		flights.arr_time BETWEEN 18 AND 22
GROUP BY
		airports.name
```