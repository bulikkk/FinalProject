from mysql.connector import connect

def scheduled_energy_regeneration():

    cnx = connect(user='bulikkk', password='qwer1234', host='127.0.0.1', database='football')

    cursor = cnx.cursor()

    cursor.execute("UPDATE app_football_user SET energy=(energy + 1) WHERE energy < 10;")

    cnx.commit()

    cursor.close()
    cnx.close()
