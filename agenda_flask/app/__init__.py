
from flask import Flask
import sqlite3
import os

def crear_app():
    app = Flask(__name__)

    def get_db():
        conn = sqlite3.connect('agenda.db')
        conn.row_factory = sqlite3.Row
        return conn

    with app.app_context():
        conn = get_db()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS actividades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha TEXT NOT NULL,
                completada INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    from app.routes import registrar_rutas
    registrar_rutas(app, get_db)

    return app
