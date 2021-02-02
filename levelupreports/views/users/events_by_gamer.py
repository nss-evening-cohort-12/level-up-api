import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views import Connection

def event_host_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor

            db_cursor.execute("""
            select e.date,
                e.time,
                e.id as event_id,
                g.title as game_title,
                u.id as user_id,
                u.first_name || " " || u.last_name as user_full_name
            from levelupapi_event e
            join levelupapi_gamer gr on e.organizer_id = gr.id
            join auth_user u on gr.user_id = u.id
            join levelupapi_game g on e.game_id = g.id
            """)

            dataset = db_cur
