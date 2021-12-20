from connect_database import get_database_connection


def drop_tables(connection):
    """Poistaa "players"-tietokantataulun.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS players;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo "players"-tietokantataulun.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE players (
            playername TEXT PRIMARY KEY,
            points INTEGER
        );
    ''')

    connection.commit()


def initialize_database():
    """Alustaa "players"-tietokantataulun.
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
