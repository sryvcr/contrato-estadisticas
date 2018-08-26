import pandas as pd 
import numpy as np 

# Abrir archivos csv
datos2010=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2010.csv') #base datos 2010
datos2011=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2011.csv') #base datos 2011
datos2012=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2012.csv') #base datos 2012
datos2013=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2013.csv') #base datos 2013
datos2014=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2014.csv') #base datos 2014
datos2015=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2015.csv') #base datos 2015
datos2016=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2016.csv') #base datos 2016
datos2017=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2017.csv') #base datos 2017
datos2018=pd.read_csv('./base_datos_contratos/BASE_DE_DATOS_2018.csv') #base datos 2018


# convertir datos en un dataframe y reemplar datos NaN con espacios vacíos
d2010=pd.DataFrame(datos2010)
d2011=pd.DataFrame(datos2011)
d2012=pd.DataFrame(datos2012)
d2013=pd.DataFrame(datos2013)
d2014=pd.DataFrame(datos2014)
d2015=pd.DataFrame(datos2015)
d2016=pd.DataFrame(datos2016)
d2017=pd.DataFrame(datos2017)
d2018=pd.DataFrame(datos2018)


# Todo lo que sea NaN será 0
d2010=d2010.replace(np.nan,'0')
d2011=d2011.replace(np.nan,'0')
d2012=d2012.replace(np.nan,'0')
d2013=d2013.replace(np.nan,'0')
d2014=d2014.replace(np.nan,'0')
d2015=d2015.replace(np.nan,'0')
d2016=d2016.replace(np.nan,'0')
d2017=d2017.replace(np.nan,'0')
d2018=d2018.replace(np.nan,'0')
 
 
 # Todo lo que sea N/A y NR será cero
d2010=d2018.replace('N/A','0')
d2010=d2018.replace('NR','0')
d2011=d2011.replace('N/A','0')
d2011=d2011.replace('NR','0')
d2012=d2012.replace('N/A','0')
d2012=d2012.replace('NR','0')
d2013=d2013.replace('N/A','0')
d2013=d2013.replace('NR','0')
d2014=d2014.replace('N/A','0')
d2014=d2014.replace('NR','0')
d2015=d2015.replace('N/A','0')
d2015=d2015.replace('NR','0')
d2016=d2016.replace('N/A','0')
d2016=d2016.replace('NR','0')
d2017=d2017.replace('N/A','0')
d2017=d2017.replace('NR','0')
d2018=d2018.replace('N/A','0')
d2018=d2018.replace('NR','0')


# Columna 'Valor_recursos'

# Promedio y sumatoria recursos 2010
print('\n')
d2010['Valor_recursos']=d2010.Valor_recursos.astype(float)
numContratos2010 = d2010['Valor_recursos'].count()
print("Total contratos celebrados 2010:", numContratos2010)
promContratos2010 = d2010['Valor_recursos'].mean()
print("Promedio Valor Recursos 2010: $", '{:,}'.format(promContratos2010), "COP")
totalRecursos2010 = d2010['Valor_recursos'].sum()
print("Total Valor Recursos 2010: $", '{:,}'.format(totalRecursos2010), "COP")

# Promedio y sumatoria recursos 2011
print('\n')
d2011['Valor_recursos']=d2011.Valor_recursos.astype(float)
numContratos2011 = d2011['Valor_recursos'].count()
print("Total contratos celebrados 2011:", numContratos2011)
promContratos2011 = d2011['Valor_recursos'].mean()
print("Promedio Valor Recursos 2011: $", '{:,}'.format(promContratos2011), "COP")
totalRecursos2011 = d2011['Valor_recursos'].sum()
print("Total Valor Recursos 2011: $", '{:,}'.format(totalRecursos2011), "COP")

# Promedio y sumatoria recursos 2012
print('\n')
d2012['Valor_recursos']=d2012.Valor_recursos.astype(float)
numContratos2012 = d2012['Valor_recursos'].count()
print("Total contratos celebrados 2012:", numContratos2012)
promContratos2012 = d2012['Valor_recursos'].mean()
print("Promedio Valor Recursos 2012: $", '{:,}'.format(promContratos2012), "COP")
totalRecursos2012 = d2012['Valor_recursos'].sum()
print("Total Valor Recursos 2012: $", '{:,}'.format(totalRecursos2012), "COP")

# Promedio y sumatoria recursos 2013
print('\n')
d2018['Valor_recursos']=d2013.Valor_recursos.astype(float)
numContratos2013 = d2013['Valor_recursos'].count()
print("Total contratos celebrados 2013:", numContratos2013)
promContratos2013 = d2013['Valor_recursos'].mean()
print("Promedio Valor Recursos 2013: $", '{:,}'.format(promContratos2013), "COP")
totalRecursos2013 = d2013['Valor_recursos'].sum()
print("Total Valor Recursos 2013: $", '{:,}'.format(totalRecursos2013), "COP")

# Promedio y sumatoria recursos 2014
print('\n')
d2014['Valor_recursos']=d2014.Valor_recursos.astype(float)
numContratos2014 = d2014['Valor_recursos'].count()
print("Total contratos celebrados 2014:", numContratos2014)
promContratos2014 = d2014['Valor_recursos'].mean()
print("Promedio Valor Recursos 2014: $", '{:,}'.format(promContratos2014), "COP")
totalRecursos2014 = d2014['Valor_recursos'].sum()
print("Total Valor Recursos 2014: $", '{:,}'.format(totalRecursos2014), "COP")

# Promedio y sumatoria recursos 2015
print('\n')
d2015['Valor_recursos']=d2015.Valor_recursos.astype(float)
numContratos2015 = d2015['Valor_recursos'].count()
print("Total contratos celebrados 2015:", numContratos2015)
promContratos2015 = d2015['Valor_recursos'].mean()
print("Promedio Valor Recursos 2015: $", '{:,}'.format(promContratos2015), "COP")
totalRecursos2015 = d2015['Valor_recursos'].sum()
print("Total Valor Recursos 2015: $", '{:,}'.format(totalRecursos2015), "COP")

# Promedio y sumatoria recursos 2016
print('\n')
d2016['Valor_recursos']=d2016.Valor_recursos.astype(float)
numContratos2016 = d2016['Valor_recursos'].count()
print("Total contratos celebrados 2016:", numContratos2016)
promContratos2016 = d2016['Valor_recursos'].mean()
print("Promedio Valor Recursos 2016: $", '{:,}'.format(promContratos2016), "COP")
totalRecursos2016 = d2016['Valor_recursos'].sum()
print("Total Valor Recursos 2016: $", '{:,}'.format(totalRecursos2016), "COP")

# Promedio y sumatoria recursos 2017
print('\n')
d2017['Valor_recursos']=d2017.Valor_recursos.astype(float)
numContratos2017 = d2017['Valor_recursos'].count()
print("Total contratos celebrados 2017:", numContratos2017)
promContratos2017 = d2017['Valor_recursos'].mean()
print("Promedio Valor Recursos 2017: $", '{:,}'.format(promContratos2017), "COP")
totalRecursos2017 = d2017['Valor_recursos'].sum()
print("Total Valor Recursos 2017: $", '{:,}'.format(totalRecursos2017), "COP")

# Promedio y sumatoria recursos 2018
print('\n')
d2018['Valor_recursos']=d2018.Valor_recursos.astype(float)
numContratos2018 = d2018['Valor_recursos'].count()
print("Total contratos celebrados 2018:", numContratos2018)
promContratos2018 = d2018['Valor_recursos'].mean()
print("Promedio Valor Recursos 2018: $", '{:,}'.format(promContratos2018), "COP")
totalRecursos2018 = d2018['Valor_recursos'].sum()
print("Total Valor Recursos 2018: $", '{:,}'.format(totalRecursos2018), "COP")

# Estadísticas contratos entre 2010 y 2018
print('\n')
totalContratos = (numContratos2010 + numContratos2011 + numContratos2012 + numContratos2013 + 
    numContratos2014 + numContratos2015 + numContratos2016 + numContratos2017 + numContratos2018)
print("Total contratos celebrados entre 2010 y 2018:", totalContratos)
totalRecursos = (totalRecursos2010 + totalRecursos2011 + totalRecursos2012 + totalRecursos2013 + 
    totalRecursos2014 + totalRecursos2015 + totalRecursos2016 + totalRecursos2017 + totalRecursos2018)
print("Total recursos entre 2010 y 2018: $", '{:,}'.format(totalRecursos), "COP")
print('\n')