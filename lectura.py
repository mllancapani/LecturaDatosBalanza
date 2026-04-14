import serial, time, re
import pyodbc

puerto 	= 'COM1'
rate 	= 9600
ser     = serial.Serial(puerto, rate,timeout=0)
i       = 0

print("Puerto = ",puerto)
print("Rate   = ",rate)
print("\nIniciando...")
print("\nLeyendo...")

conjunto_caract = ['utf-8','iso-8859-1','cp1252']

patron_peso = re.compile(r'^\s*([\d\.]+)\s*([A-Za-z]+)\s*$')

consulta = "UPDATE prod_pack_peso_balanza SET peso=? WHERE id='1'"

while 1:
        rawString = ser.readline()

        if not rawString:  # Si no hay datos, continuar
                continue

        for conjunto in conjunto_caract:
                try:
                        i += 1
                        lin = rawString.decode(conjunto)
                        #print(lin)
                        string = [item.strip() for item in lin.split(",")]
                        
                        pesos = [match.groups() for item in string if (match := patron_peso.match(item))]
                        #print(pesos)
                        if not pesos:
                                print("Sin datos")
                        else:
                                #print(f"{i} - {pesos}")
                                print(pesos[0][0])
                                try:
                                    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.3.68;DATABASE=nova;UID=sa;PWD=Marel.user')
                                except pyodbc.InterfaceError as e:
                                    print(e.args[0])
                                cursor = conn.cursor()
                                valores = pesos[0][0]
                                cursor.execute(consulta, valores)
                                conn.commit()
                                conn.close()
                                ser.reset_input_buffer()
                         
                except:
                        print('No se pudo decodificar')
                time.sleep(0.2)
        

print(rawString.name)
ser.close()
