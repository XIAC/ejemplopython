import sqlite3

DB_PATH = "juego.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS jugadores (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre    TEXT NOT NULL,
                creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS historial (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                jugador_id INTEGER NOT NULL,
                accion     TEXT NOT NULL,
                dinero     INTEGER,
                dignidad   INTEGER,
                hambre     INTEGER,
                fecha      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
            );
        """)


def crear_jugador(nombre):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("INSERT INTO jugadores (nombre) VALUES (?)", (nombre,))
        return cursor.lastrowid


def registrar_accion(jugador_id, accion, jugador):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO historial (jugador_id, accion, dinero, dignidad, hambre) VALUES (?, ?, ?, ?, ?)",
            (jugador_id, accion, jugador.dinero, jugador.dignidad, jugador.hambre),
        )


def obtener_historial(jugador_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute(
            "SELECT accion, dinero, dignidad, hambre, fecha FROM historial WHERE jugador_id = ? ORDER BY fecha",
            (jugador_id,),
        ).fetchall()
