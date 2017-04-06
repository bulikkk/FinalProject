from mysql.connector import connect

def scheduled_energy_regeneration():

    cnx = connect(user='root', password='coderslab', host='localhost', database='aaa_finaleproject')

    cursor = cnx.cursor()

    cursor.execute("UPDATE app_football_user SET energy=(energy + 1) WHERE energy < 10;")

    cnx.commit()

    cursor.close()
    cnx.close()
